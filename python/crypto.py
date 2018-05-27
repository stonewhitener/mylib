import string


def rot(s, n):
    return ''.join(
        string.ascii_uppercase[(string.ascii_uppercase.find(s[i]) + n) % len(string.ascii_uppercase)]
        if s[i] in string.ascii_uppercase
        else string.ascii_lowercase[(string.ascii_lowercase.find(s[i]) + n) % len(string.ascii_lowercase)]
        if s[i] in string.ascii_lowercase
        else s[i]
        for i in range(len(s))
    )
