def Input_Example(): #Define code as a function
    prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
    speed=input(prompt)
    if int(speed) <= 10:
        print("Slow bird")
    if int(speed) > 10:
        print("Fast bird")
    prompt="Would you like to continue?\n"
    restart=input(prompt)
    if (restart=='Yes' or restart=='yes'):
        Input_Example()
    if (restart=='No' or restart=='no'):    
        exit           
Input_Example() #Start of code runs 'main' fuction    

    
