# our language -> any vowel becomes g

def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translate += "G"
            else:
                translate += "g"
        else:
            translate += letter
    return translate        


print(translate(input("Enter a phrase: ")))