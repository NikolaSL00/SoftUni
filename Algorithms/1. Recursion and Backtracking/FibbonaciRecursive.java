import java.util.Scanner;

public class FibbonaciRecursive {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int res = calcFibbonaci(n);
        System.out.println(res);
    }

    private static int calcFibbonaci(int n) {
        if (n <= 1) {
            return 1;
        }

        return calcFibbonaci(n - 1) + calcFibbonaci(n - 2);
    }
}
