import numpy as np

def inverse_power_method(A, num_iterations=100, tolerance=1e-6):
    """
    Metoda potęgowa do znajdowania najmniejszej wartości własnej i odpowiadającego jej wektora własnego.
    
    Parameters:
        A (ndarray): Kwadratowa macierz rzeczywista.
        num_iterations (int): Maksymalna liczba iteracji.
        tolerance (float): Tolerancja do sprawdzenia zbieżności.

    Returns:
        eigenvalue (float): Najmniejsza wartość własna.
        eigenvector (ndarray): Odpowiadający jej wektor własny.
    """
    # Losowy wektor początkowy
    n = A.shape[0]
    y = np.random.rand(n)
    y /= np.linalg.norm(y)  # Normalizacja

    eigenvalue = None

    for _ in range(num_iterations):
        # Rozwiązywanie układu równań A @ x = y
        y_next = np.linalg.solve(A, y)

        # Normalizacja wektora
        y_next /= np.linalg.norm(y_next)

        # Przybliżona największa wartość własna A^{-1}
        eigenvalue_next = np.dot(y_next, y)  # Iloczyn skalarny

        # Sprawdzenie zbieżności
        if eigenvalue is not None and np.abs(eigenvalue_next - eigenvalue) < tolerance:
            break

        y = y_next
        eigenvalue = eigenvalue_next

    # Najmniejsza wartość własna macierzy A
    smallest_eigenvalue = 1 / eigenvalue

    return smallest_eigenvalue, y

# Przykład użycia
if __name__ == "__main__":
    # Symetryczna macierz wejściowa
    A = np.array([[4, 1],
                  [1, 3]])
    
    smallest_eigenvalue, eigenvector = inverse_power_method(A)
    
    print("Najmniejsza wartość własna:", smallest_eigenvalue)
    print("Odpowiadający jej wektor własny:", eigenvector)
