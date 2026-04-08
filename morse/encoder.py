"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE


def encode_word(word):
    word = word.upper()

    letters = []
    for char in word:
        if char in MORSE:
            letters.append(MORSE[char])

    return " ".join(letters)


def encode(text):
    text = text.upper()

    clean_text = ""
    for char in text:
        if char.isalpha() or char == " ":
            clean_text += char

    words = clean_text.split()

    encoded_words = []
    for word in words:
        encoded_words.append(encode_word(word))

    return "|".join(encoded_words)


if __name__ == "__main__":
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
