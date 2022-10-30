import java.util.Scanner;

public class BiteFillerRecursion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Integer[] memory = new Integer[n];

        fillVector(memory, 0);
    }

    private static void fillVector(Integer[] memory, int vecIndex) {
        if (vecIndex >= memory.length) {
            print(memory);
            return;
        }

        for (int i = 0; i <= 1; i++) {
            memory[vecIndex] = i;
            fillVector(memory, vecIndex + 1);
        }
    }

    private static void print(Integer[] memory) {
        for (Integer integer : memory) {
            System.out.print(integer);
        }
        System.out.println();
    }
}
