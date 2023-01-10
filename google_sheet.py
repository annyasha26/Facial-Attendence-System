import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('drivetest.json', scope)
client = gspread.authorize(creds)

sheet_names = {
    "L3C1":"18zP9egNpLXPaCNOYIm9Q-TROBL4eczQA6JF7xbvJmrg",
    "L3C2":"1bRprUS2MMZi0HludK7ofRQaxLQnHgdvVR-yGHzZfizE",
    "L3C3":"1I4rcbVBwyBAXmxwXReZx1z7Y4gIdz1d9stIHQnhuyS4",
    "L3C4":"1_ZaKdcnUnEKPpXJeHzOkc6q6-HR4c6uzGTb4ETPLurs",
    "L3C5":"1tatds8Ow9Vs6ViVy20SdGbjV9-Y1OomjJHWkuX1YRSE",
    "L3C6":"10_1N5lNHEERRpCcih-XxQeARTeNifl57HNrMun4RnTQ"
}

# g_sheet = client.open_by_key("18zP9egNpLXPaCNOYIm9Q-TROBL4eczQA6JF7xbvJmrg")
g_sheet_subject_sheet_name = {
    "Artificial Intelligence":"CU6051NT",
    "Advanced Database": "CC6001NT",
    "Application Development":"CS6004NT"

}

def get_google_sheet_for_a_section(section):
    return client.open_by_key(sheet_names.get(section))


worksheet= None
def get_sheet_name(section,subject):
    global worksheet
    g_sheet = get_google_sheet_for_a_section(section)
    worksheet =  g_sheet.worksheet(g_sheet_subject_sheet_name.get(subject))


def invoke_present(student_id,current_index):
    row_value = worksheet.find(student_id).row
    worksheet.update(f"{current_index}{row_value}","P")



