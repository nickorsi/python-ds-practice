def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # Rename truthy to item, not all elements in list are truthy
    return [truthy for truthy in lst if truthy]