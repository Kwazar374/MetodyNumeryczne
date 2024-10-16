import pandas as pd
import matplotlib.pyplot as plt

# Wczytywanie danych z pliku CSV
blad_float = pd.read_csv('NUM_01/blad_float.csv')

# Przykladowe kolumny z pliku CSV
h = blad_float['h']  # Zakladamy, ze 'h' jest w pierwszej kolumnie
blad_przod_float = blad_float['blad_przod']  # Zakladamy, ze 'blad_przod' jest w drugiej kolumnie
blad_centralna_float = blad_float['blad_centralna']  # Zakladamy, że 'blad_centralna' jest w trzeciej kolumnie

# Funkcja do rysowania wykresu dla float
def wykres_float():
    plt.figure(figsize=(10, 6))  # Ustalamy rozmiar wykresu
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.title('Błąd przybliżenia pochodnej funkcji (float)')
    plt.xlabel('h')
    plt.ylabel("$|D_hf - f'|$")

    # Rysowanie wykresow z cienszymi liniami i mniejszymi markerami
    plt.loglog(h, blad_przod_float, label='Pochodna w przód', marker='o', markersize=5, linewidth=1)
    plt.loglog(h, blad_centralna_float, label='Pochodna centralna', marker='s', markersize=5, linewidth=1)

    plt.legend()
    plt.savefig('wykres_blad_float.png')  # Zapisujemy wykres jako plik PNG
    plt.show()  # Wyswietlamy wykres

# Wywolanie funkcji rysujacej wykres
wykres_float()
