# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '
}

def string_to_morse(input_string):
    morse_code = ''  # Initialize an empty string to store Morse code
    for char in input_string.upper():  # Convert the input string to uppercase and iterate through each character
        if char in MORSE_CODE_DICT:  # Check if the character exists in the Morse code dictionary
            morse_code += MORSE_CODE_DICT[char] + ' '  # Add the Morse code for the character followed by a space
        else:
            morse_code += ' '  # If the character is not in the dictionary, add a space
    return morse_code.strip()  # Remove any trailing space and return the Morse code string

if __name__ == "__main__":
    user_input = input("Enter a string to convert to Morse Code: ")
    result = string_to_morse(user_input)
    print(f"Morse Code: {result}")
