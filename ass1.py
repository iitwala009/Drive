light = False
ac = False
fan = False
curtains = False
door = False

while True:
    print("\n--- HOME AUTOMATION SYSTEM ---")
    print("1. Turn ON Light")
    print("2. Turn OFF Light")
    print("3. Turn ON AC")
    print("4. Turn OFF AC")
    print("5. Turn ON Fan")
    print("6. Turn OFF Fan")
    print("7. Open Curtains")
    print("8. Close Curtains")
    print("9. Open Door/Gate")
    print("10. Close Door/Gate")
    print("11. Exit System")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if light:
            print("Light is already ON")
        else:
            light = True
            print("Light turned ON")

    elif choice == 2:
        if not light:
            print("Light is already OFF")
        else:
            light = False
            print("Light turned OFF")

    elif choice == 3:
        if ac:
            print("AC is already ON")
        else:
            ac = True
            print("AC turned ON")

    elif choice == 4:
        if not ac:
            print("AC is already OFF")
        else:
            ac = False
            print("AC turned OFF")

    elif choice == 5:
        if fan:
            print("Fan is already ON")
        else:
            fan = True
            print("Fan turned ON")

    elif choice == 6:
        if not fan:
            print("Fan is already OFF")
        else:
            fan = False
            print("Fan turned OFF")

    elif choice == 7:
        if curtains:
            print("Curtains are already OPEN")
        else:
            curtains = True
            print("Curtains OPENED")

    elif choice == 8:
        if not curtains:
            print("Curtains are already CLOSED")
        else:
            curtains = False
            print("Curtains CLOSED")

    elif choice == 9:
        if door:
            print("Door/Gate is already OPEN")
        else:
            door = True
            print("Door/Gate OPENED")

    elif choice == 10:
        if not door:
            print("Door/Gate is already CLOSED")
        else:
            door = False
            print("Door/Gate CLOSED")

    elif choice == 11:
        print("Home Automation System stopped")
        break

    else:
        print("Invalid choice")
