def variable_x_val():
    print("Only write the coefficient, the term x will be included in the final answer.")
    
    v1 = int(input("What is the first coefficient?: "))
    p1 = int(input("What power would you like to raise x to?: "))
    
    v1_new = v1 * p1
    p1 = p1 - 1
    
    operator1 = input("Would you like to +, -, /, * ?: ")
    while operator1 not in ['+', '-', '*', '/']:
        print("Invalid operator. Please enter one of +, -, *, or /.")
        operator1 = input("Would you like to +, -, /, * ?: ")
    
    v2 = int(input(str(v1) + "x^" + str(p1) + "  What would the second coefficient be?: "))
    p2 = int(input(str(v1) + "x^" + str(p1) + "  What would the second power of x be?: "))
    
    v2 = v2 * p2
    p2 = p2 - 1
    
    
    x_yn = input("Would you like an x value? (y or n): ")
    
    if x_yn.lower().startswith("y"):
        random_number = input("Would you like a random number y or n, if not an x value will be \n" 
        "asked later? ")
        if random_number.lower().startswith("y"):
            random_num_gen = random.randint(3, 20)
            print("your random x value is " + str(random_num_gen))
            if operator1 == '+':
                true_value = v1_new * random_num_gen ** p1 + v2 * random_num_gen ** p2
            elif operator1 == '-':
                true_value = v1_new * random_num_gen ** p1 - v2 * random_num_gen ** p2
            elif operator1 == '*':
                true_value = v1_new * random_num_gen ** p1 * v2 * random_num_gen ** p2
            elif operator1 == '/':
                true_value = v1_new * random_num_gen ** p1 / (v2 * random_num_gen ** p2)
            print(true_value)
        
        elif random_number.lower().startswith("n"):
            if x_yn.lower().startswith("y"):
                x_value = int(input("What would you like the value to be? "))
            
                if operator1 == '+':
                    true_value = v1_new * x_value ** p1 + v2 * x_value ** p2
                elif operator1 == '-':
                    true_value = v1_new * x_value ** p1 - v2 * x_value ** p2
                elif operator1 == '*':
                    true_value = v1_new * x_value ** p1 * v2 * x_value ** p2
                elif operator1 == '/':
                    true_value = v1_new * x_value ** p1 / (v2 * x_value ** p2)
                print(true_value)
    
    elif x_yn.lower().startswith("n"):
            # When no x value is entered, it will simplify the expression fully
            if operator1 == '+':
                # Simplify first term
                if p1 == 0:
                    term1 = str(v1_new)
                elif p1 == 1:
                    term1 = str(v1_new) + "x"
                else:
                    term1 = str(v1_new) + "x^" + str(p1)
            
                # Simplify second term
                if p2 == 0:
                    term2 = str(v2)
                elif p2 == 1:
                    term2 = str(v2) + "x"
                else:
                    term2 = str(v2) + "x^" + str(p2)
            
                print(term1 + " + " + term2)
        
            elif operator1 == '-':
                # Simplify first term
                if p1 == 0:
                    term1 = str(v1_new)
                elif p1 == 1:
                    term1 = str(v1_new) + "x"
                else:
                    term1 = str(v1_new) + "x^" + str(p1)
            
                # Simplify second term
                if p2 == 0:
                    term2 = str(v2)
                elif p2 == 1:
                    term2 = str(v2) + "x"
                else:
                    term2 = str(v2) + "x^" + str(p2)
            
                print(term1 + " - " + term2)
        
            elif operator1 == '*':
                # Simplify first term
                if p1 == 0:
                    term1 = str(v1_new)
                elif p1 == 1:
                    term1 = str(v1_new) + "x"
                else:
                    term1 = str(v1_new) + "x^" + str(p1)
            
                # Simplify second term
                if p2 == 0:
                    term2 = str(v2)
                elif p2 == 1:
                    term2 = str(v2) + "x"
                else:
                    term2 = str(v2) + "x^" + str(p2)
            
                print(term1 + " * " + term2)
        
            elif operator1 == '/':
                # Simplify first term
                if p1 == 0:
                    term1 = str(v1_new)
                elif p1 == 1:
                    term1 = str(v1_new) + "x"
                else:
                    term1 = str(v1_new) + "x^" + str(p1)
            
                # Simplify second term
                if p2 == 0:
                    term2 = str(v2)
                elif p2 == 1:
                    term2 = str(v2) + "x"
                else:
                    term2 = str(v2) + "x^" + str(p2)
            
                print(term1 + " / " + term2)
                
variable_x_val()
