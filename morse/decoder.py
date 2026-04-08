"""
This module provides functions to decode Morse code into text.
"""

from morse.mapping import MORSE

# reverse mapping: morse → harf
REVERSE_MORSE = {value: key for key, value in MORSE.items()}


def decode_word(morse_word):
    """Decode a single Morse word into text."""
    letters = morse_word.split()
    decoded_letters = []

    for letter in letters:
        if letter in REVERSE_MORSE:
            decoded_letters.append(REVERSE_MORSE[letter])

    return "".join(decoded_letters)


def decode(morse_text):
    """Decode Morse code into text."""
    words = morse_text.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)
