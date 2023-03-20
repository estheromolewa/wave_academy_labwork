"""
Write an emoji converter program
"""
if __name__ == "__main__":
    mood = {"Happy": "\U0001F603", "Sad":  "\U0001F61E", "Lovely": "\U0001F60D", "Funny": "\U0001F602", "Tired" : "\U0001F62B", "Angry": "\U0001F620"}
    feeling = input("How are you feeling? ") 
    print("I am feeling", mood[feeling.capitalize()])
    

