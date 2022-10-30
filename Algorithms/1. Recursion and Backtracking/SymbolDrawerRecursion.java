import java.util.Scanner;

public class SymbolDrawerRecursion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        drawer(n);
    }

    private static void drawer(int n) {

        for (int i = 0; i < n; i++) {
            System.out.print("*");
        }

        if (n > 0) {
            System.out.println();
        }

        if (n > 0) {
            drawer(n - 1);
        }

        for (int i = 0; i < n; i++) {
            System.out.print("#");
        }

        if (n > 0) {
            System.out.println();
        }
    }
}
