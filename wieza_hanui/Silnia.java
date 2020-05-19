import java.util.Scanner;

public class Silnia {
	
    // metoda main, standardowo od niej sie zaczyna wlasciwe
    // wykonywanie programu
	public static void main(String[] args) {
        // deklaracja zmiennej
        int liczba;
        Scanner sc = new Scanner(System.in);
		
        // czytanie zmiennej ze standardowego wejscia
        liczba = sc.nextInt();
        // wypisanie wyniku do standardowego wyjscia
        System.out.println(silnia(liczba));
	}

    // definicja metody rekurencyjnej obliczajacej silnie
    public static int silnia(int n) {
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

}
