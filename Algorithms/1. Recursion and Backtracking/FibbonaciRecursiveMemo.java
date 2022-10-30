import java.util.HashMap;
import java.util.Scanner;

public class FibbonaciRecursiveMemo {

    public static HashMap<Integer, Long> resMap = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Integer n = scanner.nextInt();

        resMap.put(0,0l);
        resMap.put(1,1l);

        Long res = calcFibbonaci(n);
        System.out.println(res);
    }

    private static Long calcFibbonaci(Integer n) {
        if (resMap.containsKey(n)) {
            return resMap.get(n);
        } else {
            Long value = calcFibbonaci(n - 1) + calcFibbonaci(n - 2);
            resMap.put(n, value);
            return value;
        }
    }
}
