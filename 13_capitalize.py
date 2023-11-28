def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    # Can use phrase.capitalize()
    first_upper_letter = phrase[0].upper()
    rest_of_phrase = phrase[1:]

    return first_upper_letter + rest_of_phrase

