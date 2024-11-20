import numpy as np

# Macierz wejściowa
A = np.array([
    [1, 1],
    [1, -1],
    [1, 1]
], dtype=float)

# Funkcja Grama-Schmidta (modyfikowana)
def modified_gram_schmidt(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for i in range(n):
        v = A[:, i]
        R[i, i] = np.linalg.norm(v)
        Q[:, i] = v / R[i, i]  # Normalizacja

        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            A[:, j] -= R[i, j] * Q[:, i]  # Aktualizacja reszty wektorów
    
    return Q, R

# Implementacja rozkładu Grama-Schmidta
Q_gs, R_gs = modified_gram_schmidt(A.copy())

# Rozkład za pomocą funkcji NumPy
Q_np, R_np = np.linalg.qr(A)

# Weryfikacja wyników
print("Macierz Q (Grama-Schmidt):")
print(Q_gs)

print("\nMacierz R (Grama-Schmidt):")
print(R_gs)

print("\nMacierz Q (NumPy):")
print(Q_np)

print("\nMacierz R (NumPy):")
print(R_np)

print("\nSprawdzenie rozkładu (Grama-Schmidt):", np.allclose(A, np.dot(Q_gs, R_gs), atol=1e-8))
print("Sprawdzenie rozkładu (NumPy):", np.allclose(A, np.dot(Q_np, R_np), atol=1e-8))
