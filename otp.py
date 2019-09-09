from googleapiclient.discovery import build
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
SCOPES = ['https://www.googleapis.com/auth/dialogflow']
creds = None
flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
creds = flow.run_local_server()
service = build('dialogflow', 'v2',credentials="")
collection = service.Listintents()
nested_collection = service.featured().stamps()
request = collection.list(cents=5)
response = request.execute()
print(json.dumps(response, sort_keys=True, indent=4))