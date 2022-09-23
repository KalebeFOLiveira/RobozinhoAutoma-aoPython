import email
from Google import Create_Service
import json

ARQUIVO_CLIENTE = 'credentials.json'
API_NOME = 'gmail'
VERSAO_DA_API = 'v1'
ESCOPOS = ['https://mail.google.com/']
service = Create_Service(ARQUIVO_CLIENTE,API_NOME,VERSAO_DA_API,ESCOPOS)
# user_id = 
print(service.users().getProfile(userId='me').execute())
print(service.users().messages().list(userId='me').execute())
message = service.users().messages().get(userId='me',id ='18337b9e8d734848').execute()
s1 = json.dumps(message)
d2 = json.loads(s1)
print(d2)
list (email)
while{message.titulo!=titulocodigo?}
list money=nova lista