#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
//////////////////////////////////////////////////////////////////
// Funkcja f(x) = sin(x^3)
template<typename T>
T funkcja(T x) {
    return sin(pow(x, 3));
}
//////////////////////////////////////////////////////////////////
// Dokladna pochodna funkcji f(x) = sin(x^3): f'(x) = 3x^2 * cos(x^3)
template<typename T>
T dokladna_pochodna_funkcji(T x) {
    return 3 * pow(x, 2) * cos(pow(x, 3));
}
//////////////////////////////////////////////////////////////////
// Funkcja liczaca pochodna w przod
template<typename T>
T pochodna_w_przod(T (*funkcja)(T), T h, T x)
{
    return ((funkcja(x + h) - funkcja(x)) / h);
}
//////////////////////////////////////////////////////////////////
// Funkcja liczaca pochodna centralna
template<typename T>
T pochodna_centralna(T (*funkcja)(T), T h, T x)
{
    return ((funkcja(x + h) - funkcja(x - h)) / (2 * h));
}
//////////////////////////////////////////////////////////////////
// Funkcja obliczajaca blad bezwzgledny
template<typename T>
T blad_bezwzgledny(T wartosc_przyblizona, T wartosc_dokladna)
{
    return std::fabs(wartosc_przyblizona - wartosc_dokladna);
}
//////////////////////////////////////////////////////////////////
// Funkcja generujaca logarytmicznie rozmieszczone wartosci h
template<typename T>
std::vector<T> generuj_h(T h_min, T h_max, int liczba_krokow) {
    std::vector<T> wartosci_h(liczba_krokow);
    T log_min = std::log10(h_min);
    T log_max = std::log10(h_max);
    T delta = (log_max - log_min) / (liczba_krokow - 1);

    for (int i = 0; i < liczba_krokow; i++) {
        wartosci_h[i] = std::pow(10, log_min + i * delta);
    }

    return wartosci_h;
}
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
int main(int argc, char *argv[])
{
    // Parametry pracy programu
    constexpr double x = 0.2; // Punkt w ktorym liczona jest pochodna
    constexpr int liczba_krokow = 300; // Liczba krokow h
    constexpr double h_min = 1e-16; // Minimalna wartosc h
    constexpr double h_max = 1.0; // Maksymalna wartosc h

    // Generowanie wartosci h w skali logarytmicznej
    std::vector<float> h_float = generuj_h<float>(static_cast<float>(h_min), static_cast<float>(h_max), liczba_krokow);
    std::vector<double> h_double = generuj_h<double>(h_min, h_max, liczba_krokow);

    // Wynikowa dokladna pochodna w punkcie x = 0.2
    const float dokladna_pochodna_float = dokladna_pochodna_funkcji<float>(x);
    const double dokladna_pochodna_double = dokladna_pochodna_funkcji<double>(x);

    // Pliki wyjsciowe z wynikami
    std::ofstream plik_wynikowy_float("blad_float.csv");
    std::ofstream plik_wynikowy_double("blad_double.csv");

    // Naglowki kolumn
    plik_wynikowy_float << "h,blad_przod,blad_centralna\n";
    plik_wynikowy_double << "h,blad_przod,blad_centralna\n";

    // Analiza dla typu float
    std::cout << "Analiza dla typu float...\n";
    for (const auto & h : h_float)
    {
        float wynik_przod = pochodna_w_przod<float>(funkcja<float>, h, x);
        float wynik_centralna = pochodna_centralna<float>(funkcja<float>, h, x);
        float blad_przod = blad_bezwzgledny<float>(wynik_przod, dokladna_pochodna_float);
        float blad_centralna = blad_bezwzgledny<float>(wynik_centralna, dokladna_pochodna_float);
        plik_wynikowy_float << h << "," << blad_przod << "," << blad_centralna << "\n";
    }

    // Analiza dla typu double
    std::cout << "Analiza dla typu double...\n";
    for (const auto & h : h_double)
    {
        double wynik_przod = pochodna_w_przod<double>(funkcja<double>, h, x);
        double wynik_centralna = pochodna_centralna<double>(funkcja<double>, h, x);
        double blad_przod = blad_bezwzgledny<double>(wynik_przod, dokladna_pochodna_double);
        double blad_centralna = blad_bezwzgledny<double>(wynik_centralna, dokladna_pochodna_double);
        plik_wynikowy_double << h << "," << blad_przod << "," << blad_centralna << "\n";
    }

    // Zamkniecie plikow
    plik_wynikowy_float.close();
    plik_wynikowy_double.close();

    std::cout << "Wyniki zostaly zapisane do plikow blad_float.csv oraz blad_double.csv\n";
}
//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////