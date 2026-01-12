# Zadanie 1
class Drukarka:
    def __init__(self):
        self.queue = []

    def dodaj_zadanie(self, dokument):
        self.queue.append(dokument)

    def drukuj(self):
        return self.queue.pop(0)

    def ile_czeka(self):
        return len(self.queue)


drukarka = Drukarka()
drukarka.dodaj_zadanie("CV.pdf")
drukarka.dodaj_zadanie("Zdjęcie.jpg")
drukarka.dodaj_zadanie("Raport.docx")

print(drukarka.drukuj())
print(drukarka.ile_czeka())
print(drukarka.drukuj())
print(drukarka.ile_czeka())

# Zadanie 2

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def dodaj_na_poczatek(self, value):
        self.head = Node(value, self.head)

    def dodaj_na_koniec(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def szukaj(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def usun(self, value):
        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def do_listy(self):
        wynik = []
        current = self.head
        while current:
            wynik.append(current.value)
            current = current.next
        return wynik

def usun_duplikaty(ll):
    memo = []
    for i in ll.do_listy():
        if i not in memo:
            memo.append(i)
        else:
            ll.usun(i)


ll = LinkedList()
for x in [1, 2, 2, 3, 1, 4]:
    ll.dodaj_na_koniec(x)

usun_duplikaty(ll)
print(ll.do_listy())

# Zadanie 3

from collections import OrderedDict

class LRUCache:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.cache = OrderedDict()

    def get(self, klucz):
        if klucz not in self.cache:
            return None

        self.cache.move_to_end(klucz)
        return self.cache[klucz]

    def put(self, klucz, wartosc):
        if klucz in self.cache:
            self.cache.move_to_end(klucz)

        self.cache[klucz] = wartosc

        if len(self.cache) > self.pojemnosc:
            self.cache.popitem(last=False)

# Test
cache = LRUCache(pojemnosc=2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))

cache.put("c", 3)
print(cache.get("b"))
print(cache.get("c"))