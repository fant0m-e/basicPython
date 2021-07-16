def translate(phrase):
    translation = "" # will be added to below
    for letter in phrase: # goes through each letter one at a time, checking for the following
        if letter.lower() in "aeiou": # checks for upper or lowercase vowels
            if letter.isupper(): # checking for uppercase vowel
                translation = translation + "G" # making g uppercase to match uppercase vowel
            else: # otherwise
                translation = translation + "g" # adding a normal g in place of vowel
        else: # otherwise
            translation = translation + letter # adds the letter instead of g, as the letter wasn\t a vowel
    return translation # returns the final translation, all letters added

print(translate(input("Enter a phrase: "))) # asks for input (phrase) and runs translate function
