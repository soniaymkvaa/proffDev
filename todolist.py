import todo
def main():
    # here will be a function that shows all the deadlines
    # name, 
    running = True
    while running:
        command = input()
        command = command.split(' ')
        if command[0] == 'create':
            todo.create_note(*command[1:3],' '.join(command[3:5]), 'calendar.csv')     
    # def ask_priority():
    #     print("Give a priority to this task")
    #     priority = input()
    #     return priority

if __name__ == "__main__":
    main()
