/**
 * @author weicc
 * @create 2018-07-28 19:10
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 * <p>
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * <p>
 * Write the code that will take a string and make this conversion given a number of rows:
 * <p>
 * string convert(string s, int numRows);
 * Example 1:
 * <p>
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * Example 2:
 * <p>
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * <p>
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 * 锯齿状
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
