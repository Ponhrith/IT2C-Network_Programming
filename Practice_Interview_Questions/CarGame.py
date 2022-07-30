car_started = False



while True:
    command = input("Type a Command: ").lower()
    
    if command == 'start':
        if car_started == True:
            print("Car is already started")
        else:
            print("Car Started")
            car_started = True
    elif command == "stop":
        if car_started == True:
            print("Car Stopped")
            car_started = False
        else:
            print("Car is already stopped")
    elif command == "left":
        if car_started == True:
            print("Car Turned to the Left")
        else:
            print("Car isn't even started")
    elif command == "right":
        if car_started == True:
            print("Car Turned to the Right")
        else:
            print("Car isn't even started")
    elif command == "drift":
        if car_started == True:
            print("Car Drifted")
        else:
            print("Car isn't even started")
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