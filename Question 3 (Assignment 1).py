def lookup(dictionary, search_term):
    matches = []

    # Convert search term to lowercase for case-insensitive comparison
    search_term = search_term.lower()

    # Loop through dictionary keys
    for key in dictionary:
        if search_term in key.lower():
            matches.append(key)

    # Check number of matches
    if len(matches) == 0:
        raise KeyError("search term not found")
    elif len(matches) > 1:
        raise KeyError("multiple keys found")
    else:
        key = matches[0]
        return key, dictionary[key]