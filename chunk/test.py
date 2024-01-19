def chunk(array, size):
    # Tworzymy pustą listę na wynikowe podtablice
    result = []

    # Iterujemy po oryginalnej tablicy
    for i in range(0, len(array), size):
        # Tworzymy podtablicę o rozmiarze 'size' i dodajemy do wynikowej listy
        result.append(array[i:i + size])

    return result

# Przykłady użycia
result1 = chunk([1, 2, 3, 4], 2)
result2 = chunk([1, 2, 3, 4, 5], 2)
result3 = chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)
result4 = chunk([1, 2, 3, 4, 5], 4)
result5 = chunk([1, 2, 3, 4, 5], 10)

print(result1)  # Powinno zwrócić [[1, 2], [3, 4]]
print(result2)  # Powinno zwrócić [[1, 2], [3, 4], [5]]
print(result3)  # Powinno zwrócić [[1, 2, 3], [4, 5, 6], [7, 8]]
print(result4)  # Powinno zwrócić [[1, 2, 3, 
