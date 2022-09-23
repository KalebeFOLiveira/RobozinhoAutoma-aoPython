import time
import pickle
import os.path
from __future__ import print_function
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds=None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds=pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow=InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds=flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service=build('gmail', 'v1', credentials=creds)
    results=service.users().messages().list(useId='me', labelIds=['INBOX']).execute()
    messages=results.get('messages', [])
    message_count=int(input("Quantas mensagens você quer ver?"))
    if not messages:
        print('Nenhuma mensagem encontrada.')
    else:
        print('Mensagens:')
        for message in messages[:message_count]:
            msg=service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
            print("\n")
            time.sleep(2)
if __name__=='__main__':
    main()