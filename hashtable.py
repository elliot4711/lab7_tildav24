from linkedQFile import LinkedQ


class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
        """
        key är nyckeln som anvands vid hashningen
        data är det objekt som ska hashas in
        """
        self.key = key
        self.data = data

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
        if self.list[index] == None:
            self.list[index] = node
        else: 
            self.que = LinkedQ()
            if isinstance(self.list[index], LinkedQ):
                if not self.list[index].isEmpty():
                    value = self.list[index].dequeue()
                    self.que.enqueue(value)
                self.que.enqueue(node)
                self.list[index] = self.que
            else:
                self.que.enqueue(self.list[index])
                self.que.enqueue(node)
                self.list[index] = self.que

    def search(self, key):
        """
        key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError
        """
        hashvalue = self.hashfunction(key)
        index = hashvalue % self.size

        if self.list[index] != None:
            if isinstance(self.list[index], LinkedQ):
                thing = self.list[index].dequeue()
                while self.hashfunction(thing.key) != hashvalue:
                    thing = self.list[index].dequeue()
                return thing.data
            else:
                return self.list[index]
        else:
            raise KeyError

    def hashfunction(self, key):
        """
        key är nyckeln
        Beräknar hashfunktionen för key
        """
        self.number = ""
        for self.letter in key:
            self.number = self.number + str(ord(self.letter))
        return int(self.number)

import csv
drama_dict = Hashtable(500)
with open("kdrama.csv", newline="") as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in linereader:
        drama_dict.store(row[0], row[1:])

print(drama_dict.search("The bride of Habaek"))
#print(drama_dict.search("Hej"))