import numpy as np
import matplotlib.pyplot as plt

# Parametry
N = 200  # Rozmiar macierzy
d_values = [2, 3, 4, 0.5]  # Przykładowe wartości d
b = np.arange(1, N + 1)  # Wektor wyrazów wolnych
tolerance = 1e-12  # Warunek stopu
max_iterations = 500  # Maksymalna liczba iteracji

# Funkcja do tworzenia wstęgowej reprezentacji macierzy
def create_band_matrix(N, d):
    bands = np.zeros((5, N))
    bands[2, :] = d  # Główna przekątna
    bands[1, 1:] = 0.5  # Pierwsza nadprzekątna
    bands[3, :-1] = 0.5  # Pierwsza podprzekątna
    bands[0, 2:] = 0.1  # Druga nadprzekątna
    bands[4, :-2] = 0.1  # Druga podprzekątna
    return bands

# Funkcja do mnożenia macierzy wstęgowej przez wektor
def band_matrix_vector_multiply(bands, x):
    N = len(x)
    result = np.zeros_like(x)
    result += bands[2] * x  # Główna przekątna
    result[1:] += bands[1, 1:] * x[:-1]  # Pierwsza nadprzekątna
    result[:-1] += bands[3, :-1] * x[1:]  # Pierwsza podprzekątna
    result[2:] += bands[0, 2:] * x[:-2]  # Druga nadprzekątna
    result[:-2] += bands[4, :-2] * x[2:]  # Druga podprzekątna
    return result

# Metoda Jacobiego
def jacobi_band(bands, b, x0, max_iterations, tolerance):
    D_inv = 1.0 / bands[2]  # Odwrotność głównej przekątnej
    x = x0.copy()
    errors = []
    for _ in range(max_iterations):
        R_x = band_matrix_vector_multiply(bands, x) - bands[2] * x  # R * x
        x_new = D_inv * (b - R_x)
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tolerance:
            break
        x = x_new
    return x, errors

# Metoda Gaussa-Seidela
def gauss_seidel_band(bands, b, x0, max_iterations, tolerance):
    x = x0.copy()
    N = len(b)
    errors = []
    for _ in range(max_iterations):
        x_old = x.copy()
        for i in range(N):
            sum1 = 0.0
            sum2 = 0.0
            if i > 0:
                sum1 = bands[3, i-1] * x[i-1]  # Pierwsza podprzekątna
            if i > 1:
                sum1 += bands[4, i-2] * x[i-2]  # Druga podprzekątna
            if i < N-1:
                sum2 = bands[1, i+1] * x[i+1]  # Pierwsza nadprzekątna
            if i < N-2:
                sum2 += bands[0, i+2] * x[i+2]  # Druga nadprzekątna
            x[i] = (b[i] - sum1 - sum2) / bands[2, i]
        error = np.linalg.norm(x - x_old, ord=np.inf)
        errors.append(error)
        if error < tolerance:
            break
    return x, errors

# Obliczenia i wizualizacja
results = {}
for d in d_values:
    bands = create_band_matrix(N, d)
    x_exact = np.linalg.solve(np.diag(bands[2]) +
                              np.diag(bands[1, 1:], 1) +
                              np.diag(bands[3, :-1], -1) +
                              np.diag(bands[0, 2:], 2) +
                              np.diag(bands[4, :-2], -2), b)
    x0 = np.zeros(N)  # Punkt startowy
    
    # Metoda Jacobiego
    x_jacobi, errors_jacobi = jacobi_band(bands, b, x0, max_iterations, tolerance)
    
    # Metoda Gaussa-Seidela
    x_gs, errors_gs = gauss_seidel_band(bands, b, x0, max_iterations, tolerance)
    
    # Zapis wyników
    results[d] = {
        "x_exact": x_exact,
        "x_jacobi": x_jacobi,
        "x_gs": x_gs,
        "errors_jacobi": errors_jacobi,
        "errors_gs": errors_gs,
    }
    
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
    print(f"Rozwiązanie dokładne:\n{x_exact}")
    print(f"Rozwiązanie Jacobiego:\n{x_jacobi}")
    print(f"Rozwiązanie Gaussa-Seidela:\n{x_gs}")
    print(f"Norma końcowego błędu Jacobiego: {errors_jacobi[-1]}")
    print(f"Norma końcowego błędu Gaussa-Seidela: {errors_gs[-1]}")
