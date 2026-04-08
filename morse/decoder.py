from morse.mapping import MORSE

# reverse mapping
REVERSE = {value: key for key, value in MORSE.items()}


def decode_word(morse_word):
    """
    Decodes a single morse word into text.
    """
    letters = morse_word.split(" ")

    decoded = []
    for letter in letters:
        if letter in REVERSE:
            decoded.append(REVERSE[letter])

    return "".join(decoded)


def decode(morse):
    """
    Decodes morse code into text.
    Words are separated by | and letters by space.
    """
    words = morse.split("|")

    decoded_words = []
    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)
