def sequence():
    first = int(input("What is the first number? "))
    second = int(input("What is the second number? "))
    term_num = int(input("What term would you like to find? (3, 4, 5) "))
    g_a = input("arithmetic or geometric? ")
    
    another = True
    if g_a.lower().startswith('a'):
        while another == True:
            term_num = int(term_num)
            difference = second - first
            number = difference * term_num
            part2 = number - difference
            answer = first + part2
            str(answer)
            print(answer)
            term_num = input("Next term? ")
            if term_num.isalpha():
                another = False
        
    elif g_a.lower().startswith('g'):
        term_num = int(term_num)
        ratio = second / first
        answer = first * (ratio ** (term_num - 1))
        str(answer)
        print(answer)
        term_num = input("Next term? ")
        if term_num.isalpha():
            another = False
            
sequence()
