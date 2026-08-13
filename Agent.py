occupency = False

while(True):
    occupency = bool(int(input("Checking for occupency(1/0): ")))
    if occupency == True or occupency == False:
        break
    else:
        print("Please enter valid inputs")

while occupency:

    while True:
        lumin = int(input("Is there Suffient Natural Light?(1/0) "))

        if lumin == 1 or lumin == 0:
            break
        else:
            print("Invalid Input")
    
    lumin = bool(lumin)

    if not lumin:
        print("Turning ON Lights\n")
   
    while True:
        room_temp = int(input("Current Room temperature: "))
        if room_temp>(-20) and room_temp<50:
            break
        else:
            print("Invalid Input")
    if room_temp>=32:
        print("Turning Off fans")
        print("Turning On AC set temperature to 24 C at full blast\n")
    elif room_temp<22:
        print("Turning Off fans & AC")
        print("Turning On Heater\n")
    elif room_temp in range(23,26):
        print("Turning off heater and AC")
        print("Turning on fans\n")
    aqi = -1
    while True:
        aqi = int(input("Enter Room AQI: "))
        if aqi>0 and aqi<1000:
            break
        else:
            print("Invalid Input")
   
    if aqi>=65:
        print("Turning on Air Purifier\n")
    elif aqi<=45:
        print("Turing Off Air purifier\n")
   
    slpmode = input("Do you want to enter sleep-mode:")
   
    if slpmode.lower() == 'yes':
        print("Turning lights off")
        if room_temp>=26:
            print("Turning Off fans")
            print("Turning On AC set temperature to 24 C at 40% power consumption\n")
        elif room_temp<22:
            print("Turning Off fans")
            print("Turning On Heater at 40% power consumption\n")
        elif room_temp in range(23,26):
            print("Turning off heater and AC")
            print("Turning on fans\n")
    elif slpmode.lower() == 'no':
        print()
    else:
        print("Invalid Input")
           
    while(True):
        occupency = bool(int(input("Checking for occupency(1/0): ")))
        if occupency == False or occupency == True:
            break
        else:
            print("Please enter valid inputs")
           
print("Turning of System")
print("Good Day!!")