def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    #get a count of each number
    #return the number with the biggest count

    counter = {}
    for num in nums:
        counter[num]= nums.count(num)

    #max_count = max(counter)
    biggest = (0,0)
    for key, value in (counter.items()):
        biggest = (key,value) if value > biggest[1] else biggest
    return biggest[0]

