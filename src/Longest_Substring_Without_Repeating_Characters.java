import java.util.HashMap;
import java.util.Map;

/**
 * @author weicc
 * @create 2018-07-27 15:19
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
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
                //如果i指向的字符在很前面 如果不加和j取最大  j很容易跑到前面去了
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
        }
        return len;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcba"));
    }
}
