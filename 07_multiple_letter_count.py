def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # letter_count = {letter:count += 1 for letter in phrase}
    freq_counter = {}
    for letter in phrase:
        # if(freq_counter.get(letter) == None):
        #     freq_counter[letter] = 1
        # else:
        #     freq_counter[letter] += 1
        freq_counter[letter] = freq_counter.get(letter,0) + 1
    return freq_counter

