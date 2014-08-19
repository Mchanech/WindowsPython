import ctypes

def spitback():

# Todo: check for OS
    prompt1 = input("What would you call this?\n")
    prompt2 = input("What would you like to be notified of?\n")
    prompt3 = input("Is it important? ")
    prompt3 = prompt3.lower()

    if prompt3 == "y" or prompt3 == "yes":
        priority = 3
    elif prompt3 == "n" or prompt3 == "no":
        priority = 4
    else:
        print("Please choose either 'yes' or 'no'.")
        prompt3 = input("Is it important?")

    # Pops under. This is a feature not a bug.
    ctypes.windll.user32.MessageBoxW(0,prompt2,prompt1,priority)
