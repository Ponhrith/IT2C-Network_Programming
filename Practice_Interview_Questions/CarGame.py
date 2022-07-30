while True:
    command = input("Type a Command: ")
    
    if command.lower() == 'start':
        print("Car Started")
    elif command.lower() == "stop":
        print("Car Stopped")
    elif command.lower() == "left":
        print("Car Turned to the Left")
    elif command.lower() == "right":
        print("Cara Turned to the Right")
    elif command.lower() == "drift":
        print("Car Drifted")
    elif command.lower() == "help":
        print("""
              Start: To Start the Car
              Stop: To Stop the Car
              Left: To Turn the Car to the Left
              Right: To Turn the Car to the Right
              Drift: To Drift the Car
              Exit: to Quit the Game
              """)
    elif command.lower()== "exit":
        break
    else:
        print("Unknown Command\nType 'help' for a List of Commands")