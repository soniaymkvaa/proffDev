"""my part of todo project for interacting with csv in order to terminal commands"""
import csv
import time
from datetime import datetime
def open_csv_calendar(filepath):
    calendar_notes = []
    with open(filepath,'r') as csvfile:
        calendar = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in calendar:
            calendar_notes.append(row)
    return calendar_notes

def create_note(name, need_list,deadline,file):
    note = [str(datetime.now()),name,need_list,deadline,str(1)]
    today = check_day(note)
    if today:
        priority = ask_priority()
        note[4] = str(priority)
    calendar_notes = open_csv_calendar(file)
    calendar_notes.append(note)
    with open(file,'w') as csvfile:
        for task in calendar_notes:
            csvfile.write(','.join(task) + '\n')

def ask_priority():
        print("Give a priority to this task")
        priority = input()
        return priority   
# def ask_priority():
#     pass
# def check_day(note):
#     return False
if __name__ == "__main__":
    create_note('new one', 'nothing', '2021-12-20 12:42:46.433451','calendar.csv')
