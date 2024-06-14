import gspread
from oauth2client.service_account import ServiceAccountCredentials


def export_to_google_sheets(data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Your Google Sheet Name').sheet1  # Open the first sheet
    # Append data to the sheet
    sheet.append_row(data)
