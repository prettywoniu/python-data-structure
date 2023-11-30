def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # first_names = [name['first'] for name in people]
    # last_names = [name['last'] for name in people]

    # names = []
    # for i in range(0, len(first_names)):
    #     name = f"{first_names[i]} {last_names[i]}"
    #     names.append(name)

    # return names

    # Use comprehension
    return [f"{person['first']} {person['last']}" for person in people]