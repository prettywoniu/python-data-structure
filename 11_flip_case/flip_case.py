def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = list(phrase)
    # for i in range(0, len(lst)):
    #     if lst[i].lower() == to_swap.lower():
    #         if lst[i].islower():
    #             lst[i] = lst[i].upper()
    #         else:
    #             lst[i] = lst[i].lower()

    lst = [char.swapcase() if char.lower() == to_swap.lower() else char for char in lst]

    return ''.join(lst)

    # to_swap = to_swap.lower()
    # result = ''

    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     result += ltr

    # return result