def steps(n):
    for i in range(n):
        row = '#' * (i + 1) + ' ' * (n - i - 1)
        print(row)

# Przykłady użycia
steps(2)
print("\n")
steps(3)
print("\n")
steps(4)