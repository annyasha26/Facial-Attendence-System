import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('drivetest.json', scope)
client = gspread.authorize(creds)
g_sheet = client.open_by_key("18zP9egNpLXPaCNOYIm9Q-TROBL4eczQA6JF7xbvJmrg")

g_sheet_subject_sheet_name = {
    "Artificial Intelligence":"CU6051NT",
    "Advanced Database": "CC6001NT",
    "Application Development":"CS6004NT"

}

worksheet= None
def get_sheet_name(subject):
    global worksheet
    worksheet =  g_sheet.worksheet(g_sheet_subject_sheet_name.get(subject))


# worksheet = g_sheet.worksheet("CU6051NT")

# print(records_data)

def invoke_present(student_id,current_index):
    row_value = worksheet.find(student_id).row
    worksheet.update(f"{current_index}{row_value}","P")



