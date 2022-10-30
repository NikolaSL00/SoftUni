import java.util.Scanner;

public class FactorialRecursion {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int res = calcFactorial(n);
        System.out.println(res);
    }

    // n * n-1
    private static int calcFactorial(int n) {
        if (n == 1) {
            return 1;
        }

        return n * calcFactorial(n - 1);
    }
}
