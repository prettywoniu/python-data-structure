def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # keys = d.keys()
    # sorted_keys = sorted(keys)
    # return (sorted_keys[0], sorted_keys[-1])

    # min(), max() can be used on strings
    # Uppercase comes before lowercase
    #return (min(keys), max(keys))

    # min(), max() on dictioanry
    # By default compare the keys
    return (min(d), max(d))