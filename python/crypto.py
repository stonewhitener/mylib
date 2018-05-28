import string


def rot(s, n):
    """
    Caesar cipher
    """
    cipher = ''
    for c in s:
        if c in string.ascii_lowercase:
            cipher += string.ascii_lowercase[(string.ascii_lowercase.find(c) + n) % len(string.ascii_lowercase)]
        elif c in string.ascii_uppercase:
            cipher += string.ascii_uppercase[(string.ascii_uppercase.find(c) + n) % len(string.ascii_uppercase)]
        else:
            cipher += c
    return cipher
