command = ""
started = False
while True:
    command = input("> "). lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = False
        print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = True
        print("Car stopped.")

    elif command == "help":
        print("\n"
              "start - to start the car\n"
              "stop - to stop the car\n"
              "quit - to quit\n"
              "        ")
    elif command == "help":
        print("Sorry, I don't understand that!")

