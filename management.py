from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from UI_Files.management_ui import Ui_MainWindow

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText
import datetime
import main

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']

class ManagementPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.management_window = Ui_MainWindow()
        self.management_window.setupUi(self)
        self.events = None
        self.events_list = []

        self.management_window.tableWidget.setColumnWidth(0, 200)
        self.management_window.tableWidget.setColumnWidth(1, 200)
        self.management_window.tableWidget.setColumnWidth(2, 500)
        self.management_window.tableWidget.setColumnWidth(3, 200)

        self.management_window.pushButtonSearch.clicked.connect(self.search)
        self.management_window.pushButtonAllEvents.clicked.connect(self.print_all_events)
        self.management_window.pushButtonSendMail.clicked.connect(self.send_email)
    
        self.management_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.management_window.pushButtonExit.clicked.connect(self.app_exit)


    def load_events(self):
        if self.events is None:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            service = build('calendar', 'v3', credentials=creds)

            now = datetime.datetime.utcnow().isoformat() + 'Z'  # Add 'Z' to indicate UTC time

            events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=2,  # Increased maxResults for more events
                                                singleEvents=True, orderBy='startTime').execute()
            self.events = events_result.get('items', [])

    def make_events_list(self):
        self.load_events()
        if not self.events_list:
            for event in self.events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                formatted_start = datetime.datetime.fromisoformat(start).strftime("%d-%m-%Y %H:%M") if 'T' in start else start
                attendees = event.get('attendees', [])
                participant_emails = ", ".join([attendee['email'] for attendee in attendees if 'email' in attendee])
                organizer_email = event['organizer'].get('email', 'Unknown')

                self.events_list.append([event.get('summary', 'No Title'), formatted_start, participant_emails, organizer_email])
            
    def search(self):
        self.make_events_list()
        input_text = self.management_window.lineEditSearch.text().lower()
        if input_text == '':
            self.management_window.lineEditSearch.setPlaceholderText("Enter the text to search!")
            return 
        filtered_events_list = []
        for event in self.events_list:
            if input_text in event[0].lower():
                filtered_events_list.append(event)

        main.print_table(self.management_window, filtered_events_list)
                
    def print_all_events(self):
        self.make_events_list()
        main.print_table(self.management_window, self.events_list)
        
    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_message(self, service, user_id, message):
        try:
            sent_message = service.users().messages().send(userId=user_id, body=message).execute()
            print(f"Message Id: {sent_message['id']}")
            return sent_message
        except Exception as error:
            print(f"An error occurred: {error}")

    def send_email(self):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        sender_email = 'workspacevit4@gmail.com'
        if self.events:
            for event in self.events:
                attendees = event.get('attendees', [])
                for attendee in attendees:
                    email = attendee.get('email')
                    if email:
                        subject = f"Upcoming Event: {event.get('summary', 'No Title')}"
                        body = f"Dear {attendee.get('displayName', 'Participant')},\n\nYou are invited to {event.get('summary', 'an event')}.\n\nBest regards,\nYour Team"
                        message = self.create_message(sender_email, email, subject, body)
                        self.send_message(service, 'me', message)

    def back_menu(self):
        from menu import MenuPage
        self.open_menu_window = MenuPage(True) 
        self.hide()  
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
