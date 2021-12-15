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
    calendar_notes = open_csv_calendar(file)
    today = check_day(note,calendar_notes)
    if today:
        priority = ask_priority()
        note[4] = str(priority)
    calendar_notes.append(note)
    with open(file,'w') as csvfile:
        for task in calendar_notes:
            csvfile.write(','.join(task) + '\n')

def ask_priority():
        print("Give a priority to this task")
        priority = input()
        return priority

def check_day(note:list,calendar_notes):
    deadlines = []
    for each in calendar_notes:
        if str(each[3].split()[0]) == str(note[3].split()[0]):
            deadlines.append(each)
    deadlines.sort(key=lambda lst: lst[4])
    return True if len(deadlines) == 0 else False

def show_deadlines(note:list):
    deadlines = []
    for each in note:
        if each[3].split()[0] == str(datetime.now()).split()[0]:
            deadlines.append(each)
    deadlines.sort(key=lambda lst: lst[4])
    for each in deadlines:
        print(f'The {each[1]} event with priority {each[4]} is assigned on today. The needlist is: {each[2]}')    
# def ask_priority():

# def delete_note(name,file):



if __name__ == "__main__":
    create_note('new one', 'nothing', '2021-12-20 12:42:46.433451','calendar.csv')
