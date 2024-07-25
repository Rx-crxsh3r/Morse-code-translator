# all_the symbols
symbols = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "@"
}

# Reverse the symbols dictionary for Morse to English translation
morse_to_english = {v: k for k, v in symbols.items()}

# the user has to type a word
ignore = False
error = False
output = ""
purpose = input("What would you like to do, boss? ")

def e_m(output):
    ask = input("Please type what you would like to be translated to Morse code: ")
    length = len(ask)
    for i in range(length):
        if ask[i] in symbols.keys():
            output = output + " " + symbols.get(ask[i])
        else:
            output = output + " " + "####"
            global error  # Declare error as global to modify it inside the function
            error = True
    return output

def m_e(output):
    global error  # Declare error as global to modify it inside the function
    ask = input("Please type the Morse code to be translated to English (use spaces between letters and '@' for spaces between words): ")
    words = ask.split(' @ ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_to_english.keys():
                output += morse_to_english[letter]
            else:
                output += "####"
                error = True
        output += " "
    return output.strip()

if purpose.lower() == "bored":
    print("Imagine being bored haha... pls call me :(")
    ignore = True
elif purpose.lower() == "morse to english":
    output = m_e(output)
elif purpose.lower() == "english to morse":
    output = e_m(output)

if not ignore:
    if error:
        print("The '####' represent an invalid character entered")
        print(output)
    else:
        print(output)
