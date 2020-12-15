def capitalize_first(string):
    words = string.split()
    n = 0
    for word in words:
        if  any(p in words[n-1] for p in '.?!'):
            words[n] = word.title()
        n += 1
    return " ".join(words)

