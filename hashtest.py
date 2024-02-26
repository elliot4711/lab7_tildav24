def hashfunction(key):
    """
    key är nyckeln
    Beräknar hashfunktionen för key
    """
    number = ""
    for letter in key:
        number = number + str(ord(letter))
    return number

print(int(hashfunction("The King: Eternal Monarch")) % 10000)