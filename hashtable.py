class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
        """
        key är nyckeln som anvands vid hashningen
        data är det objekt som ska hashas in
        """
        self.key = key
        self.data = data
        self.next = None

class Hashtable:

    def __init__(self, size):
        """
        size: hashtabellens storlek
        """
        self.size = size
        self.list = [None] * size

    def store(self, key, data):
        """
        key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen.
        """
        index = self.hashfunction(key) % self.size
        node = HashNode(key, data)
        print(str(index) + ",")
        #print("Hej")
        if self.list[index] == None:
            #print("None in list")
            self.list[index] = node
        else:
            current = self.list[index]
            if current.key == key:
                current.data = data
            else:
                found = False
                while current.next:
                    current = current.next
                    if current.key == key:
                        current.data = data
                        found = True
                        break
                if not found:
                    current.next = node

    def search(self, key):
        """
        key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError
        """
        hashvalue = self.hashfunction(key)
        index = hashvalue % self.size
        #print(index)
        current = self.list[index]
        if current != None:
            while current:
                if current.key == key:
                    return current.data
                else:
                    current = current.next
            raise KeyError
        else:
            raise KeyError

    def hashfunction(self, key):
        """
        key är nyckeln
        Beräknar hashfunktionen för key
        """
        self.number = ""
        i = 5
        for self.letter in key:
            i +=1
            self.number = self.number + str((ord(self.letter) * 16**i))
        return int(self.number)

import csv
drama_dict = Hashtable(500)
with open("kdrama.csv", newline="") as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in linereader:
        drama_dict.store(row[0], row[1:])

