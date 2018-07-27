import java.util.HashMap;
import java.util.Map;

/**
 * @author weicc
 * @create 2018-07-27 15:19
 * <p>
 * Given a string, find the length of the longest substring without repeating characters.
 * <p>
 * Examples:
 * <p>
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * <p>
 * Given "bbbbb", the answer is "b", with the length of 1.
 * <p>
 * Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
 * "pwke" is a subsequence and not a substring.
 **/
public class Longest_Substring_Without_Repeating_Characters {
    public static int lengthOfLongestSubstring(String s) {

        if ("".equals(s)) {
            return 0;
        }
        int len = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0, j = 0; i < s.length(); i++) {
            map.put(s.charAt(i), i);
            len = Math.max(len, i - j + 1);


            if (map.containsKey(s.charAt(i))) {
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
        }
        return len;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcba"));
    }
}
