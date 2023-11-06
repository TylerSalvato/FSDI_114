def myFunction(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    string1 = string1.replace(" ")
    string2 = string2.replace(" ")
    if length(string1) != length(string2):
        return False

    dict1 = {}
    dict2 = {}

        
    for letter in string1:
        if (letter < 'a' or letter > 'z') and (letter < 'A' or letter > 'Z'):
            continue 
        if letter not in dict1:
            dict1[letter] = 0 
        dict1[letter] += 1
        for letter in dict2: 
        if (letter < 'a' or letter > 'z') and (letter < 'A' or letter > 'Z'):
            continue 
        if letter not in dict1:
            dict1[letter] = 0 
        dict1[letter] += 1
    
    return dict1 == dict2
