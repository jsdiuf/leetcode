/**
 * @author weicc
 * @create 2018-07-28 19:10
 * https://leetcode.com/problems/zigzag-conversion/description/
 **/
public class ZigZag {
    public static String convert(String s, int numRows) {

        if (numRows == 1 || s.length() <= numRows || "".equals(s)) {
            return s;
        }

        char[] arr = s.toCharArray();
        int len = s.length();
        int interval = numRows * 2 - 2;
        StringBuffer buf = new StringBuffer();

        for (int i = 0; i < numRows; i++) {
            buf.append(arr[i]);
            int step = i;
            boolean isleft = true;
            while (true) {
                int add = isleft ? (interval - i * 2) : i * 2;
                isleft = isleft ? false : true;
                if (add == 0) {
                    continue;
                }
                step += add;
                if (step >= len) {
                    break;
                }
                buf.append(arr[step]);
            }
        }
        return buf.toString();
    }

    public static void main(String[] args) {
        System.out.println(convert("PAYPALISHIRING", 100));
    }
}
