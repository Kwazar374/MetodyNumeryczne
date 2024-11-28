import numpy as np
import matplotlib.pyplot as plt

# Parametry
N = 200  # Rozmiar macierzy
d_values = [2, 3, 4, 0.5]  # Przykładowe wartości d (w tym problematyczna wartość d=0.5)
b = np.arange(1, N + 1)  # Wektor wyrazów wolnych: [1, 2, ..., N]
tolerance = 1e-6  # Warunek stopu
max_iterations = 500  # Maksymalna liczba iteracji

# Tworzenie macierzy o strukturze podanej w zadaniu
def create_matrix(N, d):
    A = np.zeros((N, N))
    np.fill_diagonal(A, d)
    np.fill_diagonal(A[:-1, 1:], 0.5)
    np.fill_diagonal(A[1:, :-1], 0.5)
    np.fill_diagonal(A[:-2, 2:], 0.1)
    np.fill_diagonal(A[2:, :-2], 0.1)
    return A

# Metoda Jacobiego
def jacobi(A, b, x0, max_iterations, tolerance):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = x0.copy()
    errors = []
    for _ in range(max_iterations):
        x_new = (b - np.dot(R, x)) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tolerance:
            break
        x = x_new
    return x, errors

# Metoda Gaussa-Seidela
def gauss_seidel(A, b, x0, max_iterations, tolerance):
    x = x0.copy()
    errors = []
    N = len(b)
    for _ in range(max_iterations):
        x_new = x.copy()
        for i in range(N):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tolerance:
            break
        x = x_new
    return x, errors

# Obliczenia i wizualizacja
for d in d_values:
    A = create_matrix(N, d)
    x_exact = None
    try:
        x_exact = np.linalg.solve(A, b)  # Rozwiązanie dokładne
    except np.linalg.LinAlgError:
        print(f"Macierz dla d = {d} jest osobliwa lub źle uwarunkowana!")

    x0 = np.zeros(N)  # Punkt startowy

    # Metoda Jacobiego
    x_jacobi, errors_jacobi = jacobi(A, b, x0, max_iterations, tolerance)
    
    # Metoda Gaussa-Seidela
    x_gs, errors_gs = gauss_seidel(A, b, x0, max_iterations, tolerance)
    
    # Wykresy różnic
    plt.figure(figsize=(12, 6))
    plt.plot(errors_jacobi, label="Jacobi", marker="o", markersize=3)
    plt.plot(errors_gs, label="Gauss-Seidel", marker="s", markersize=3)
    plt.yscale("log")
    plt.title(f"Zbieżność metod iteracyjnych dla d = {d}")
    plt.xlabel("Liczba iteracji")
    plt.ylabel("Błąd (norma ∞)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Wyniki końcowe
    print(f"--- d = {d} ---")
    if x_exact is not None:
        print(f"Rozwiązanie dokładne:\n{x_exact}")
    print(f"Rozwiązanie Jacobiego:\n{x_jacobi}")
    print(f"Rozwiązanie Gaussa-Seidela:\n{x_gs}")
    print(f"Norma końcowego błędu Jacobiego: {errors_jacobi[-1]}")
    print(f"Norma końcowego błędu Gaussa-Seidela: {errors_gs[-1]}")
