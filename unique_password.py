"""
This program would generate 15 unique password characters
"""

if __name__ == "__main__":

    import random as r

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    numbers = "123456789"
    symbols = "#()?<>@{}[]&*$^_-?/|\:;"

    print("Follow the instructions below")
    alpha = int(input("What is the number of alphabets you want in your password: "))
    capital_l = int(input("What is the number of capital letters in your password: "))
    num = int(input("What is the number of times you want to use numbers: "))
    symbol = int(input("What is the number of times you want to use symbols: "))
 
    if (alpha + capital_l + num + symbol) == 15:
        print("You are doing well, the total number of your password is accurate")
        
        increment = 0
        letters = []
        while increment < alpha:
            random_letters = r.choice(alphabets)
            letters.append(random_letters)
            increment += 1

        print()
        digits = []
        count = 0
        while count < num:
            random_num = r.choice(numbers)
            digits.append(random_num)
            count += 1

        print()
        step_size = 0
        sym = []
        while step_size < symbol:
            random_sym = r.choice(symbols)
            sym.append(random_sym)
            step_size += 1
            
        print()
        counter = 0
        caplocks = []
        while counter < capital_l:
            random_cap = r.choice(capital_letter)
            caplocks.append(random_cap)
            counter += 1
    
        print("Here is your password:", letters + digits + sym + caplocks)
    
    else:
        print("The length of your password is not 15 in total, you should recheck your password")

