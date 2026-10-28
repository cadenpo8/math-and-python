import math

def trig_calc():
    
    angle_radian = input("Would you like it in Degrees (D) or radians (R)? ")
    if angle_radian.lower().startswith('r'):
        angle_radians = float(input("what is the radians amount? "))
        
        sine_value_r = math.sin(angle_radians)
        cosine_value_r = math.cos(angle_radians)
        tan_value_r = math.tan(angle_radians)
        
        
        rep_sin_r = 1 / sine_value_r
        rep_cos_r = 1 / cosine_value_r
        rep_tan_r = 1 / tan_value_r
        
        print("sin(" + str(angle_radians) + ") = " + str(sine_value_r))
        print("cos(" + str(angle_radians) + ") = " + str(cosine_value_r))
        print("tan(" + str(angle_radians) + ") = " + str(tan_value_r))
        
        print("csc(" + str(angle_radians) + ") = " + str(rep_sin_r))
        print("sec(" + str(angle_radians) + ") = " + str(rep_cos_r))
        print("cot(" + str(angle_radians) + ") = " + str(rep_tan_r))
        
        
    elif angle_radian.lower().startswith('d'):
        angle_degrees = float(input("What angle? "))
        angle_deg = math.radians(angle_degrees)
        
        sine_value_d = math.sin(angle_deg)
        cosine_value_d = math.cos(angle_deg)
        tan_value_d = math.tan(angle_deg)
        
        
        rep_sin_d = 1 / sine_value_d
        rep_cos_d = 1 / cosine_value_d
        rep_tan_d = 1 / tan_value_d
        
        print("sin(" + str(angle_degrees) + ") = " + str(sine_value_d))
        print("cos(" + str(angle_degrees) + ") = " + str(cosine_value_d))
        print("tan(" + str(angle_degrees) + ") = " + str(tan_value_d))
        
        print("csc(" + str(angle_degrees) + ") = " + str(rep_sin_d))
        print("sec(" + str(angle_degrees) + ") = " + str(rep_cos_d))
        print("cot(" + str(angle_degrees) + ") = " + str(rep_tan_d))
        
        
    else:
        print("invalid input, try again")
        return

trig_calc()
