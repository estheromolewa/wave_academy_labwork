"""
Write a program that keep asking for a number until you enter a negative number 
At the end print the sum of all entered numbers 
"""
if __name__ == "__main__":
    sum = 0
    num = int(input("Enter a non negative number: "))
    while num >= 0:
        sum += num
        print(sum)
        num = int(input("Enter a non negative number: "))
    print(f"The sum of non negative numbers is {sum}")