while True:
    command = input("Type a Command: ").lower()
    
    if command == 'start':
        print("Car Started")
    elif command == "stop":
        print("Car Stopped")
    elif command == "left":
        print("Car Turned to the Left")
    elif command == "right":
        print("Cara Turned to the Right")
    elif command == "drift":
        print("Car Drifted")
    elif command == "help":
        print("""
              Start: To Start the Car
              Stop: To Stop the Car
              Left: To Turn the Car to the Left
              Right: To Turn the Car to the Right
              Drift: To Drift the Car
              Exit: to Quit the Game
              """)
    elif command == "exit":
        break
    else:
        print("Unknown Command\nType 'help' for a List of Commands")