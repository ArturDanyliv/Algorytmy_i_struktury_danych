class Queue:
    def __init__(self):
        self.queue = []

    def add(self, element):
        # Dodaj element na koniec kolejki
        self.queue.append(element)

    def remove(self):
        # Sprawdź, czy kolejka nie jest pusta
        if not self.is_empty():
            # Zdejmij element z początku kolejki i zwróć go
            return self.queue.pop(0)
        else:
            print("Kolejka jest pusta.")

    def is_empty(self):
        # Sprawdź, czy kolejka jest pusta
        return len(self.queue) == 0

# Przykłady użycia
q = Queue()
q.add(1)
q.add(2)
q.add(3)

print(q.remove())  # Zwraca 1
print(q.remove())  # Zwraca 2
print(q.remove())  # Zwraca 3
print(q.remove())  # Kolejka jest pusta
