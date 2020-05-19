// importowanie biblioteki z podstawowymi funkcjami wejscia/ wyjscia
#include <stdio.h>

// deklaracja funkcji - jedynie co to robi, to mowi kompilatorowi ze gdzies
// dalej bedzie jej definicja
int silnia(int n);

// funkcja main, standardowo od niej sie zaczyna wlasciwe wykonywanie programu
int main() {
    // deklaracja zmiennej
    int liczba;

    // czytanie zmiennej ze standardowego wejscia
    scanf("%d", &liczba);
    // wypisanie wyniku do standardowego wyjscia
    printf("%d\n", silnia(liczba));
    // zakonczenie wykonywania programu. Program zwraca 0 sugerujac tym ze
    // wykonywanie zakonczylo sie prawidlowo
    return 0;
}

// definicja funkcji rekurencyjnej obliczajacej silnie
int silnia(int n) {
    // punkt stopu funkcji rekurencyjnej, w tym momencie przestaja byc
    // wywolywane kolejne funkcje 
    if (n <= 1)
        return 1;
    // nastepna linijka mnozy n * silnia z jeden mniej od n.
    // na przyklad silnie z 4 mozna sobie wyobrazi w nastepujacy sposob:
    // krok 1: (4 * (silnia(3)))
    // krok 2: (4 * (3 * (silnia(2))))
    // krok 3: (4 * (3 * (2 * silnia(1))))
    // krok 4: (4 * (3 * (2 * 1)))
    // krok 5: (4 * (3 * 2))
    // krok 6: (4 * 6)
    // wynik: 24
    return n * silnia(n-1);
}
