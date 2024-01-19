class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # Sprawdzamy, czy nowa wartość jest mniejsza czy większa od bieżącej
        if data < self.data:
            # Jeżeli mamy lewe poddrzewo, rekurencyjnie wywołujemy insert na lewym dziecku
            if self.left is not None:
                self.left.insert(data)
            else:
                # Jeżeli nie mamy lewego dziecka, tworzymy nowy węzeł
                self.left = Node(data)
        elif data > self.data:
            # Jeżeli mamy prawe poddrzewo, rekurencyjnie wywołujemy insert na prawym dziecku
            if self.right is not None:
                self.right.insert(data)
            else:
                # Jeżeli nie mamy prawego dziecka, tworzymy nowy węzeł
                self.right = Node(data)

    def contains(self, data):
        # Sprawdzamy, czy bieżący węzeł ma wartość równą szukanej
        if self.data == data:
            return self
        # Jeżeli szukana wartość jest mniejsza, idziemy w lewo
        elif data < self.data and self.left is not None:
            return self.left.contains(data)
        # Jeżeli szukana wartość jest większa, idziemy w prawo
        elif data > self.data and self.right is not None:
            return self.right.contains(data)
        else:
            # Jeżeli nie ma dzieci do sprawdzenia, wartość nie istnieje w drzewie
            return None

# Przykłady użycia
root = Node(10)
root.insert(5)
root.insert(15)

# Sprawdzamy, czy drzewo zawiera wartość 5
result = root.contains(5)
if result:
    print(f"Znaleziono węzeł z wartością {result.data}")
else:
    print("Nie znaleziono węzła.")
