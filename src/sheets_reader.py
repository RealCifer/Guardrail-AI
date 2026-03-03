import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1


def fetch_pending_rows():
    """
    Fetch rows where Status is empty or 'Pending'
    """
    records = sheet.get_all_records()
    
    filtered = []
    for index, row in enumerate(records, start=2):
        if row["Status"] in ("", "Pending"):

            row["Mobile"] = str(row["Mobile"])

            row["_row_number"] = index
            filtered.append(row)

    return filtered


def update_status(row_number, column_name, value):
    """
    Update a specific cell by column name
    """
    headers = sheet.row_values(1)
    col_index = headers.index(column_name) + 1
    sheet.update_cell(row_number, col_index, value)