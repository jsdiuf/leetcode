/**
 * @author weicc
 * @create 2018-07-29 0:48
 * https://leetcode.com/problems/string-to-integer-atoi/description/
 **/
public class Atoi {
    public static int myAtoi(String str) {

        double result = 0;
        int i = 0;
        int len = str.length();

        while (i < len && str.charAt(i) == ' ') {
            i++;
        }
        if (i == len) {
            return 0;
        }

        boolean positive = true;
        if (str.charAt(i) == '-') {
            i++;
            positive = false;
        } else if (str.charAt(i) == '+') {
            i++;
        }
        while (i < len && str.charAt(i) - '0' >= 0 && str.charAt(i) - '0' <= 9) {
            result = (result * 10 + (str.charAt(i) - '0'));
            i++;
        }
        if(!positive){
            result*=-1;
        }
        if (Integer.MIN_VALUE >= result ) {
            return Integer.MIN_VALUE;
        }
        if (result >= Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        }
        return (int) result;
    }

    public static void main(String[] args) {
        System.out.println(myAtoi("-"));
    }
}
