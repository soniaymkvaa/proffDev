"""my part of todo project for interacting with csv in order to terminal commands"""

import csv
from datetime import datetime


def open_csv_calendar(filepath: str) -> list:
    """
    open csv file and read notes from it
    >>> open_csv_calendar('calendar.csv')
    [['2021-12-15 11:42:46.433451', 'Birthday', 'nothing', '2021-12-17 15:42:46.433451', '1'], \
['2021-12-13 11:42:46.433451', 'shoping', 'money', '2021-12-20 12:42:46.433451', '1'], \
['2021-12-15 12:08:45.535348', 'new one', 'nothing', '2021-12-20 12:42:46.433451', '1']]
    """
    calendar_notes = []
    with open(filepath, "r") as csvfile:
        calendar = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in calendar:
            calendar_notes.append(row)
    return calendar_notes


def create_note(name: str, need_list: str, deadline: str, file: str) -> None:
    """
    create new note
    """
    note = [str(datetime.now()), name, need_list, deadline, str(1)]
    calendar_notes = open_csv_calendar(file)
    today = check_day(note, calendar_notes)
    if today:
        priority = ask_priority()
        note[4] = str(priority)
    calendar_notes.append(note)
    with open(file, "w") as csvfile:
        for task in calendar_notes:
            csvfile.write(",".join(task) + "\n")


def show_notes(file: str) -> None:
    """
    print each line in note
    """
    calendar_notes = open_csv_calendar(file)
    for note in calendar_notes:
        print(
            f"date: {note[0]} ]name: {note[1]} need: {note[2]} deadline: {note[3]} priority: {note[4]}\n"
        )


def ask_priority() -> str:
    """
    ask priority to the task
    """
    print("Give a priority to this task")
    priority = input()
    return priority


def check_day(note: list, calendar_notes: list) -> bool:
    """
    check if you have othes notes with same deadline
    >>> check_day(['2021-12-15 11:42:46.433451', 'Birthday', 'nothing', '2021-12-17 15:42:46.433451', '1'],\
[['2021-12-15 11:42:46.433451', 'Birthday', 'nothing', '2021-12-17 15:42:46.433451', '1']])
    True
    """
    deadlines = []
    for each in calendar_notes:
        if str(each[3].split()[0]) == str(note[3].split()[0]):
            deadlines.append(each)
    deadlines.sort(key=lambda lst: lst[4])
    return True if len(deadlines) == 0 else False


def show_deadlines(note: list) -> None:
    """
    print all deadlines
    """
    deadlines = []
    for each in note:
        if each[3].split()[0] == str(datetime.now()).split()[0]:
            deadlines.append(each)
    deadlines.sort(key=lambda lst: lst[4])
    for each in deadlines:
        print(
            f"The {each[1]} event with priority {each[4]} is assigned on today. The needlist is: {each[2]}"
        )


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())

