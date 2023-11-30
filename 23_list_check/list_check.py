def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # for item in lst:
    #     if not isinstance(item, list):
    #         return False
    # return True

    # Use all() with a generator comprehension
    # all(): Returns True if all items in an iterable (list, tuple, dictionary) are true, 
    #        otherwise it returns False.
    #        If the iterable object is empty, returns True.
    #
    return all(isinstance(item, list) for item in lst)