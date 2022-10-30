import java.util.Arrays;
import java.util.Scanner;

public class ArraySumRecursion {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = Arrays.stream(scanner.nextLine().split("\\s+"))
                .mapToInt(Integer::parseInt)
                .toArray();

        int res = summer(arr, 0);

        System.out.println(res);
    }

    private static int summer(int[] array, int index) {

        if (index == array.length - 1) {
            return array[index];
        }

        return array[index] + summer(array, index + 1);
    }

}
