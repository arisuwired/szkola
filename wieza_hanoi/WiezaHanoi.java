import java.util.Scanner;

public class WiezaHanoi {

    public static void main(String[] args) {
        // tworzymy skaner do czytania ilosci dyskow
        Scanner sc = new Scanner(System.in);

        // czytamy ilosc dyskow
        int wielkoscWiezy = sc.nextInt();
        // wykonujemy rekurencyjne rozwiazanie Hanoi dla n dyskow
        rozwiazHanoi(wielkoscWiezy, "a", "b", "c");
        
        // zamykamy scanner (w tym przypadku raczej niepotrzebne,
        // ale wypada dla dobrego stylu)
        sc.close();
    }

    public static void rozwiazHanoi(int n, String src, String dst, String aux) {
        // warunek stopu
        if (n > 0) {
            // za pomoca metologii divide and conquer przenosimy n-1 dyskow
            // ze stosu zrodlowego (src) do stosu pomocniczego (aux)
            rozwiazHanoi(n-1, src, aux, dst);
            // przenosimy n-ty dysk z stosu src do stosu dst (koncowego)
            System.out.println("Dysk " + n + " z " + src + " do " + dst);
            // znowu za pomoca dzielenia i zwyciezania przenosimy n-1 dyskow
            // (wszystkie ze stosu) aux do stosu src
            rozwiazHanoi(n-1, aux, dst, src);
        }
    }
    
}
