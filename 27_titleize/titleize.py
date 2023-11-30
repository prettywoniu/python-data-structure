def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    words = phrase.split(' ')

    return ' '.join([w.capitalize() for w in words])
    # return ' '.join([s.capitalize() for s in phrase.split(' ')])

    # there's a built-in method for this!
    #return phrase.title()
