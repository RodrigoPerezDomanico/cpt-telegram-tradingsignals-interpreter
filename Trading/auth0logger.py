from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'
def _getRange():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                        range=RANGE_NAME).execute()
    values = result.get('values', [])
    row=len(values)+1
    RANGE_NAME=str(f'A{row}:O{row}')
    return RANGE_NAME

def logg_in(SPREADSHEET_ID,RANGE_NAME,action,NEW_LINE=[]):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        if action=='read':
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                        range=RANGE_NAME).execute()
            values = result.get('values', [])
            if not values:
                print('No data found.')
                return

            # print('Name, Major:')
            # print (values)
            return values
        elif action=='write':
            values=['1','2','3']
            body={'values':values}
            result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
            valueInputOption='RAW', body=body).execute()



            RANGE_NAME=_getRange(SPREADSHEET_ID, RANGE_NAME)
            result = sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                        range=RANGE_NAME).execute()
            # values = result.get('values', [])
            return result
    except HttpError as err:
        print(err)
# SPREADSHEET_ID='13kVXlWzeprpben1PAnR-qsbiWLKrM4cS4F3fdKJcrrA'
# RANGE_NAME="Hoja 1!A1:A"
# logg_in(SPREADSHEET_ID, RANGE_NAME)