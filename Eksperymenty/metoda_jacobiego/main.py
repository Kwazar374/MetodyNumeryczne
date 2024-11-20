import numpy as np

def jacobi_method(A, b, tol=1e-10, max_iterations=100):
    """
    Rozwiązuje układ równań liniowych Ax = b metodą Jacobiego.

    Parametry:
    - A: macierz współczynników (macierz kwadratowa, np.array)
    - b: wektor wynikowy (np.array)
    - tol: tolerancja zbieżności (przybliżenie dokładności do rozwiązania)
    - max_iterations: maksymalna liczba iteracji

    Zwraca:
    - x: przybliżony wektor rozwiązania
    - k: liczba wykonanych iteracji
    """
    # Inicjalizacja zmiennych
    n = A.shape[0]                    # Liczba zmiennych (rozmiar macierzy A)
    x = np.zeros(n)                    # Wektor początkowy (same zera)
    x_new = np.zeros(n)                # Wektor do przechowywania nowego przybliżenia

    for k in range(max_iterations):
        # Iteracja Jacobiego
        for i in range(n):
            # Suma części poza przekątną
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            # Aktualizacja elementu x_new[i]
            x_new[i] = (b[i] - s) / A[i][i]

        # Sprawdzenie warunku zbieżności ||x_new - x|| < tol
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1  # Zwraca rozwiązanie i liczbę iteracji

        # Aktualizacja wektora x
        x = x_new.copy()

    # Jeśli przekroczono maksymalną liczbę iteracji
    raise ValueError("Metoda Jacobiego nie zbiega się po maksymalnej liczbie iteracji")

# Przykład użycia
A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = np.array([-1, 2, 3])
x, iterations = jacobi_method(A, b, 1)

print("Rozwiązanie x:", x)
print("Liczba iteracji:", iterations)
