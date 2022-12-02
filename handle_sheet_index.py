import json
sheet_name_path = "./sheet_names.json"
import ast

def get_current_index(subject,section="L3C1"):
    with open(sheet_name_path,"r+") as f:
        a= json.load(f)
        section_sheet = ast.literal_eval(a[subject])
        return section_sheet[section]
        
        
# get_current_index("Artificial Intelligence")


def update_col_index(subject,section):
    with open(sheet_name_path,"r+") as f:
        a= json.load(f)
        print("old a value",a)
        section_sheet = ast.literal_eval(a[subject])
        col_index = section_sheet[section]
        col_index = chr(ord(col_index)+1)
        section_sheet[section] = col_index
        print("stirng transfrom",str(section_sheet))

        a[subject] = str(section_sheet)
        print("updated value of a",a)
        f.seek(0)
        json.dump(a,f)
        print("sucessfully written")






