from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import os

# Hangi kapsamları (scopes) kullanacağınızı belirtin
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    creds = None

    # Önceki kimlik doğrulama bilgilerini kontrol edin
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Kimlik doğrulama bilgileri doğru değilse veya süresi dolmuşsa yeniden doğrulama yapın
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except FileNotFoundError:
                print("Hata: credentials.json dosyası bulunamadı.")
                return None

        # Yeni kimlik doğrulama bilgilerini kaydet
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def main():
    # Kimlik doğrulama yapın
    credentials = authenticate()

    if credentials is None:
        return

    # Drive API'sini kullanarak servisi oluşturun
    service = build('drive', 'v3', credentials=credentials)

    # Drive'daki dosyaları listele
    results = service.files().list(
        pageSize=15, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('Drive\'da hiç dosya bulunamadı.')
    else:
        print('Drive\'daki dosyalar:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    main()