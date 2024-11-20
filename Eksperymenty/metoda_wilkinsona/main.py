import numpy as np

def wilkinson_power_method(A, p, num_iterations=100, tolerance=1e-6):
    """
    Metoda potęgowa Wilkinsona z przesunięciem p.
    
    Parameters:
        A (ndarray): Kwadratowa macierz rzeczywista.
        p (float): Współczynnik przesunięcia.
        num_iterations (int): Maksymalna liczba iteracji.
        tolerance (float): Tolerancja do sprawdzenia zbieżności.

    Returns:
        shifted_eigenvalue (float): Największa wartość własna przesuniętej macierzy.
        eigenvalue (float): Największa wartość własna oryginalnej macierzy.
        eigenvector (ndarray): Odpowiadający jej wektor własny.
    """
    # Modyfikacja macierzy A -> A' = A - pI
    n = A.shape[0]
    I = np.eye(n)
    A_shifted = A - p * I

    # Losowy wektor początkowy
    y = np.random.rand(n)
    y /= np.linalg.norm(y)  # Normalizacja

    shifted_eigenvalue = None

    for _ in range(num_iterations):
        # Mnożenie wektora przez zmodyfikowaną macierz
        y_next = A_shifted @ y

        # Normalizacja wektora
        y_next /= np.linalg.norm(y_next)

        # Przybliżona największa wartość własna zmodyfikowanej macierzy
        shifted_eigenvalue_next = np.dot(y_next, A_shifted @ y_next)

        # Sprawdzenie zbieżności
        if shifted_eigenvalue is not None and np.abs(shifted_eigenvalue_next - shifted_eigenvalue) < tolerance:
            break

        y = y_next
        shifted_eigenvalue = shifted_eigenvalue_next

    # Oryginalna wartość własna (dodanie przesunięcia)
    eigenvalue = shifted_eigenvalue + p

    return shifted_eigenvalue, eigenvalue, y

# Przykład użycia
if __name__ == "__main__":
    # Symetryczna macierz wejściowa
    A = np.array([[4, 1],
                  [1, 4]])

    # Przesunięcie p
    p = 3.5

    shifted_eigenvalue, eigenvalue, eigenvector = wilkinson_power_method(A, p)

    print("Przesunięta największa wartość własna:", shifted_eigenvalue)
    print("Największa wartość własna oryginalnej macierzy:", eigenvalue)
    print("Odpowiadający jej wektor własny:", eigenvector)
