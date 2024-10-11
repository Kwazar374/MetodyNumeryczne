// Funkcja liczaca pochodna w przod
template<typename T>
T pochodna_w_przod(T (*funkcja)(T), T h, T x)
{
    return ((funkcja(x + h) - funkcja(x)) / h);
}
// Funkcja liczaca pochodna centralna
template<typename T>
T pochodna_centralna(T (*funkcja)(T), T h, T x)
{
    return ((funkcja(x + h) - funkcja(x - h)) / (2 * h));
}
// Funkcja obliczajaca blad bezwzgledny
// Wybor precyzji
// Generowanie wykresu
