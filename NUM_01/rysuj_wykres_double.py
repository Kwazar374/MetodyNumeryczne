import pandas as pd
import matplotlib.pyplot as plt

# Wczytywanie danych z pliku CSV
blad_double = pd.read_csv('NUM_01/blad_double.csv')

# Przykladowe kolumny z pliku CSV
h = blad_double['h']  # Zakladamy, ze 'h' jest w pierwszej kolumnie
blad_przod_double = blad_double['blad_przod']  # Zakladamy, ze 'blad_przod' jest w drugiej kolumnie
blad_centralna_double = blad_double['blad_centralna']  # Zakladamy, ze 'blad_centralna' jest w trzeciej kolumnie

# Funkcja do rysowania wykresu dla double
def wykres_double():
    plt.figure(figsize=(10, 6))  # Ustalamy rozmiar wykresu
    plt.grid(True, which='both', linestyle='--', linewidth=0.7)
    plt.title('Błąd przybliżenia pochodnej funkcji (double)')
    plt.xlabel('h')
    plt.ylabel("$|D_hf - f'|$")

    # Rysowanie wykresow z cienszymi liniami i mniejszymi markerami
    plt.loglog(h, blad_przod_double, label='Pochodna w przód', marker='o', markersize=5, linewidth=1)
    plt.loglog(h, blad_centralna_double, label='Pochodna centralna', marker='s', markersize=5, linewidth=1)

    plt.legend()
    plt.savefig('wykres_blad__double.png')  # Zapisujemy wykres jako plik PNG
    plt.show()  # Wyswietlamy wykres

# Wywolanie funkcji rysujacej wykres
wykres_double()
