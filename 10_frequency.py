def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    # sum = 0
    # for num in lst:
    #     if num == search_term:
    #         sum+=1

    result = sum(1 for num in lst if num == search_term)
    return result