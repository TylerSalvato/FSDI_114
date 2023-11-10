def myFunction(string1, string2):
    # Preprocess the strings
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    # Check if the lengths are equal
    if len(string1) != len(string2):
        return False

    # Create dictionaries to store letter counts
    dict1 = {}
    dict2 = {}

    # Populate dict1
    for letter in string1:
        if 'a' <= letter <= 'z':
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1

    # Populate dict2
    for letter in string2:
        if 'a' <= letter <= 'z':
            if letter in dict2:
                dict2[letter] += 1
            else:
                dict2[letter] = 1

    # Compare the dictionaries
    return compare_dictionaries(dict1, dict2)

def compare_dictionaries(dict1, dict2):
    # Compare the dictionaries as you previously defined
    # (I've used your provided compare_dictionaries function)
    for letter in dict1:
        if (letter < 'a' or letter > 'z') and (letter < 'A' or letter > 'Z'):
            continue
        if letter not in dict2:
            return False
        if dict1[letter] != dict2[letter]:
            return False

    for letter in dict2:
        if (letter < 'a' or letter > 'z') and (letter < 'A' or letter > 'Z'):
            continue
        if letter not in dict1:
            return False
        if dict1[letter] != dict2[letter]:
            return False

    return True