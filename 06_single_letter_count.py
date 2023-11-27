def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    word_upper_case = word.upper()
    letter_upper_case = letter.upper()
    letter_count = 0

    for letter in word_upper_case:
        if letter == letter_upper_case:
            letter_count += 1
    return letter_count