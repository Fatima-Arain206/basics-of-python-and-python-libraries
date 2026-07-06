import pandas as pd
''' convert a dictionary into a excel file '''
# Fatima, yeh aap ki 8 keys wali dictionary hai
student_records = {
    "name": ["Fatima", "Ali", "Ayesha", "Zain"],
    "age": [20, 22, 21, 23],
    "city": ["Karachi", "Lahore", "Islamabad", "Badin"],
    "roll_num": [101, 102, 103, 104],
    "gpa": [3.8, 3.5, 3.9, 3.2],
    "department": ["CS", "SE", "CS", "IT"],
    "semester": [4, 6, 4, 8],
    "is_graduated": [False, False, False, True]
}

# Verification ke liye check karte hain ke kya sab ki length equal hai?
# for key, value in student_records.items():
#     print(f"Key: '{key}' ki list mein {len(value)} items hain.")

# make a data frame
data_f = pd.DataFrame(student_records)
# there should be a data frame
data_f.to_excel('Dict_Frame_into_excel.xlsx',index=True)
