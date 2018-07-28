/**
 * @author weicc
 * @create 2018-07-28 23:07
 * https://leetcode.com/problems/reverse-integer/description/
 **/
public class Reverse_Integer {
    public static int reverse(int x) {

        if(x==0){
            return 0;
        }
        int[] arr = new int[10];
        int index = 0;

        while (x >= 10 || x <= -10) {
            arr[index++] = x % 10;
            x /= 10;
        }
        arr[index] = x;
        while (arr[index] == 0 && index >= 0) {
            index--;
        }
        double d = 0;
        for (int i = 0; i <= index; i++) {
            d += arr[i] * Math.pow(10, index - i);
        }
        if(d>Integer.MAX_VALUE||d<Integer.MIN_VALUE){
            return 0;
        }
        return (int) d;
    }
    public static int reverse2(int x)
    {
        int result = 0;

        while (x != 0)
        {
            int tail = x % 10;
            int newResult = result * 10 + tail;
            //if ((newResult - tail) / 10 != result)
            //{ return 0; }
            result = newResult;
            x = x / 10;
        }

        return result;
    }

    public static void main(String[] args) {

        System.out.println(reverse2(1111111119));

    }
}
