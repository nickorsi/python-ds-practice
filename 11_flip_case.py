def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped_phrase = ""
    # Iterate through phrase
    for letter in phrase:
        # Determine if letter.upper is same as to_swap.upper
        if letter.upper() == to_swap.upper():
            # Use .swapcase on letter and replace in phrase_list
            swapped_phrase += letter.swapcase()
        # Otherwise just push in letter
        else:
            swapped_phrase = swapped_phrase + letter
    # Return joined phrase_list
    return swapped_phrase
