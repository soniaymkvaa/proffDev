import todo


def main() -> None:
    """handles main loop and general work and input in terminal"""
    running = True
    while running:
        command = input()
        command = command.split(" ")
        if command[0] == "create":
            todo.create_note(*command[1:3], " ".join(command[3:5]), "calendar.csv")
        elif command[0] == "show":
            todo.show_notes("calendar.csv")
        elif command[0] == "exit":
            quit()


if __name__ == "__main__":
    main()
