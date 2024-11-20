from functools import reduce
import time
import matplotlib.pyplot as plt

# Funkcja LU4D - rozkład LU dla macierzy 4-diagonalnej
def LU4D(n):
    # Inicjalizacja przekątnych czterodiagonalnej macierzy
    matrix = []
    matrix.append([0] + [0.3] * (n - 1))  # Dolna przekątna (pod główną)
    matrix.append([1.01] * n)  # Główna przekątna
    matrix.append([0.2 / i for i in range(1, n)] + [0])  # Górna przekątna (nad główną)
    matrix.append([0.15 / (i * i * i) for i in range(1, n - 1)] + [0] + [0])  # Górna przekątna (2. nad główną)

    # Wektor prawej strony
    x = list(range(1, n + 1))

    # Faktoryzacja LU na czterech przekątnych
    for i in range(1, n):
        if i < n - 1:
            matrix[0][i] /= matrix[1][i - 1]
            matrix[1][i] -= matrix[0][i] * matrix[2][i - 1]
            matrix[2][i] -= matrix[0][i] * matrix[3][i - 1]
        elif i == n - 1:
            matrix[0][i] /= matrix[1][i - 1]
            matrix[1][i] -= matrix[0][i] * matrix[2][i - 1]

    # Rozwiązywanie układu LUx = b
    for i in range(1, n):
        x[i] -= matrix[0][i] * x[i - 1]

    x[n - 1] /= matrix[1][n - 1]
    x[n - 2] = (x[n - 2] - matrix[2][n - 2] * x[n - 1]) / matrix[1][n - 2]

    for i in range(n - 3, -1, -1):
        x[i] = (x[i] - matrix[3][i] * x[i + 2] - matrix[2][i] * x[i + 1]) / matrix[1][i]

    # Wyznacznik przez iloczyn głównej przekątnej
    determinant = reduce(lambda a, b: a * b, matrix[1])

    return x, determinant

# Główne parametry
N = 300
num_repeats = 100  # Liczba powtórzeń dla uśrednienia
times = []
sizes = list(range(5, N + 1, 1))

# Wyznaczanie wyniku i wyznacznika dla N = 300
wynik, wyznacznik = LU4D(N)
print("Wyznacznik:", wyznacznik)
print("Wynik:", wynik)

# Pomiar czasu dla różnych rozmiarów N
for n in sizes:
    repeat_times = []
    for _ in range(num_repeats):
        start_time = time.time()
        LU4D(n)
        end_time = time.time()
        repeat_times.append(end_time - start_time)

    # Średni czas dla danego N
    avg_time = sum(repeat_times) / num_repeats
    times.append(avg_time)

# Rysowanie wykresu czasów
plt.figure(figsize=(12, 6))
plt.plot(sizes, times, marker='o', linestyle='-', color="b")
plt.xlabel('Rozmiar macierzy (N)')
plt.ylabel('Średni czas wykonania (sekundy)')
plt.title('Czas wykonania w funkcji rozmiaru macierzy N')
plt.grid(True)
plt.show()
