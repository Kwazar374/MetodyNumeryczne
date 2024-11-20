import numpy as np

def power_method(A, num_iterations=100, tolerance=1e-6):
    """
    Metoda potęgowa do znajdowania największej wartości własnej i odpowiadającego jej wektora własnego.
    
    Parameters:
        A (ndarray): Kwadratowa macierz rzeczywista.
        num_iterations (int): Maksymalna liczba iteracji.
        tolerance (float): Tolerancja do sprawdzenia zbieżności.

    Returns:
        eigenvalue (float): Przybliżona największa wartość własna.
        eigenvector (ndarray): Odpowiadający jej wektor własny.
    """
    # Losowy wektor początkowy (możesz wybrać dowolny inny, byle nie zerowy)
    n = A.shape[0]
    y = np.random.rand(n)
    y /= np.linalg.norm(y)  # Normalizacja wektora

    eigenvalue = None

    for _ in range(num_iterations):
        # Mnożenie wektora przez macierz
        y_next = A @ y

        # Normalizacja wektora
        y_next /= np.linalg.norm(y_next)

        # Przybliżona wartość własna (iloczyn skalarny z macierzą)
        eigenvalue_next = np.dot(y_next, A @ y_next)

        # Sprawdzenie zbieżności
        if eigenvalue is not None and np.abs(eigenvalue_next - eigenvalue) < tolerance:
            break

        y = y_next
        eigenvalue = eigenvalue_next

    return eigenvalue, y

# Przykład użycia
if __name__ == "__main__":
    # Symetryczna macierz wejściowa
    A = np.array([[4, 1],
                  [1, 3]])
    
    eigenvalue, eigenvector = power_method(A)
    
    print("Największa wartość własna:", eigenvalue)
    print("Odpowiadający jej wektor własny:", eigenvector)