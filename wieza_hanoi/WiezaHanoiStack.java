import java.util.Stack;
import java.util.Scanner;

public class WiezaHanoiStack {
    
    // definiujemy trzy stosy ktore skladaja sie ze zmiennych typu Integer,
    // potrzebne sa do algorytmu
    static Stack<Integer> a = new Stack<Integer>();
    static Stack<Integer> b = new Stack<Integer>();
    static Stack<Integer> c = new Stack<Integer>();

    public static void main(String[] args) {
        // tworzymy skaner do czytania ilosci dyskow
        Scanner sc = new Scanner(System.in);

        // czytamy ilosc dyskow
        int wielkoscWiezy = sc.nextInt();
        // wypelniamy stos A dyskami po kolei od najwiekszego (n-1)
        // do najmniejszego (0)
        for (int i = wielkoscWiezy; i-- > 0;)
            a.push(i);
        // printujemy aktualny stan stosow przed algorytmem
        printHanoi(a, b, c);
        // wykonujemy rekurencyjne rozwiazanie Hanoi dla n dyskow
        rozwiazHanoi(wielkoscWiezy, a, b, c);
        
        // zamykamy scanner (w tym przypadku raczej niepotrzebne,
        // ale wypada dla dobrego stylu)
        sc.close();
    }

    public static void rozwiazHanoi(int n, Stack<Integer> src, Stack<Integer> dst, Stack<Integer> aux) {
    // warunek stopu
    if (n > 0) {
        // za pomoca metologii divide and conquer przenosimy n-1 dyskow
        // ze stosu zrodlowego (src) do stosu pomocniczego (aux)
        rozwiazHanoi(n-1, src, aux, dst);
        // przenosimy n-ty dysk z stosu src do stosu dst (koncowego)
        dst.push(src.pop());
        // printujemy aktualny stan stosow po przeniesieniu
        printHanoi(a, b, c);
        // znowu za pomoca dzielenia i zwyciezania przenosimy n-1 dyskow
        // (wszystkie ze stosu) aux do stosu src
        rozwiazHanoi(n-1, aux, dst, src);
        }
    }
    
    public static void printHanoi(Stack<Integer> a, Stack<Integer> b, Stack<Integer> c) {
        System.out.println("A " + a.toString());
        System.out.println("B " + b.toString());
        System.out.println("C " + c.toString());
        System.out.println();
    }

}
