import json
from Google import Create_Service

ARQUIVO_CLIENTE = 'credentials.json'
API_NOME = 'gmail'
VERSAO_DA_API = 'v1'
ESCOPOS = ['https://mail.google.com/']
service = Create_Service(ARQUIVO_CLIENTE,API_NOME,VERSAO_DA_API,ESCOPOS)

emails = service.users().messages().list(userId='me').execute()

# print(service.users().getProfile(userId='me').execute())

print(emails['messages'][0]['id'])

# print(service.users().messages().get(userId='me',id = emails['messages'][11]['id']).execute()['snippet'])

while(emails['messages'][0]['id'] != '0999'):
    print(emails['messages'][0]['id'])
    print(service.users().messages().get(userId='me',id = emails['messages'][0]['id']).execute()['snippet'])
    emails = service.users().messages().list(userId='me').execute()
# for item in emails['messages']:
#     print(service.users().messages().get(userId='me',id = item['id']).execute()['id'])
#     print(service.users().messages().get(userId='me',id = item['id']).execute()['snippet'])
    
