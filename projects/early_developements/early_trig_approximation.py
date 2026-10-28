def trig_calc():
    trig_function = input("What trig function would you like to use (only basic for now, cos, sin, tan): ")
    degrees = float(input("what degrees would you like the function to have: "))
    over_90 = "Sorry cant do that right now do less than 90 degrees"
    print("Please be aware, this calculator is not 100% acurate and is just an esitmate ")
    
    
    # Sine fomrula estimates
    under_33_s = .017
    under_45_s = 0.016
    over_45_s = .007
    
    
    # Cosine formula estimates
    under_33_c = 1 - (.005 * degrees)
    under_45_c = .95 - (.02 * degrees)
    over_45_c = .07 - (.008 * degrees)
    
    
    # Tangent formula estimates
    under_33_t = .017 * degrees
    under_45_t = (.03 * degrees) - .5
    over_45_t = (.1 * degrees) - 3
    
    
    # Making the code for estimate
    if trig_function.lower().startswith("s"):
        if degrees < 33:
            s_val_33 = under_33_s * degrees
            print(s_val_33)
        elif 33 < degrees < 45:
            s_val_45 = under_45_s * degrees
            print(s_val_45)
        elif 90 > degrees > 45:
            s_value_90 = (over_45_s * over_45_s) + .35
            print(s_value_90)
        elif degrees > 89:
            print(over_90)
    elif trig_function.lower().startswith("c"):
        if degrees < 33:
            print(under_33_c)
        elif 33 < degrees < 45:
            print(under_45_c)
        elif 90 > degrees > 45:
            print(over_45_c)
        elif degrees > 89:
            print(over_90)
    elif trig_function.lower().startswith("t"):
        if degrees < 33:
            print(under_33_t)
        elif 33 < degrees < 45:
            print(under_45_t)
        elif 90 > degrees > 45:
            print(over_45_t)
        elif degrees > 89:
            print(over_90)
    else:
        print("Please rerun the program and try again, you function was wrong ")
    
trig_calc()
