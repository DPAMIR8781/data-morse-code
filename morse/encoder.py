"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE


def encode_word(word):
    """Encode a single word into Morse code."""
    word = word.upper()

    letters = []
    for char in word:
        if char in MORSE:
            letters.append(MORSE[char])

    return " ".join(letters)


def encode(text):
    """Encode text into Morse code."""
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
    example_text = "abc"
    encoded_text = encode_word(example_text)
    print(f"Encoded word '{example_text}' to Morse code: '{encoded_text}'")

    example_text = "abc ABC"
    encoded_text = encode(example_text)
    print(f"Encoded '{example_text}' to Morse code: '{encoded_text}'")
