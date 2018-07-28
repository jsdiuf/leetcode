/**
 * @author weicc
 * @create 2018-07-28 15:39
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 **/
public class LongestPalindrome {
    public static String longestPalindrome(String s) {

        if ("".equals(s)) {
            return "";
        }

        char[] arr=s.toCharArray();
        int left=0,right=1;
        int step = s.length() * 2 - 1;
        int len = s.length();
        boolean move = false;
        for (int index = 0; index < step; index++) {
            int i = 0, j = 0;
            if ((index & 1) == 0) {
                i = index / 2;
                j = i;
            } else {
                i = index / 2;
                j = i + 1;
            }
            while (i >= 0 && j < len && arr[i]==arr[j]) {
                i--;
                j++;
                move = true;
            }
            if (move && j-i-1>right-left) {
                left=i+1;
                right=j;
            }
            move = false;

        }

        return s.substring(left,right);
    }

    /**
     * 动态规划
     * https://www.cnblogs.com/coderJiebao/p/Algorithmofnotes30.html
     */

    public static String longestPalindrome2(String s) {
        if ("".equals(s)) {
            return "";
        }

        char [] arr=s.toCharArray();
        int len = s.length();
        int[][] dp = new int[len][len];
        int left=0,right=1;
        //找出長度為1或2的回文
        for (int i = 0; i < len; i++) {

            //dp[i][j] means 从i到j的子字符串为回文
            dp[i][i] = 1;
            if (i<len-1&&arr[i]==arr[i + 1]) {
                dp[i][i + 1] = 1;
                left=i;
                right=i+2;
            }
        }

        //先从步长3 开始增长到len
        for(int step=3;step<=len;step++){
            for(int i=0;i<=len-step;i++){
                //两头相等且中间为回文 。。记录
                if(arr[i]==arr[i+step-1]&&dp[i+1][i+step-2]==1){
                    dp[i][i+step-1]=1;
                    left=i;
                    right=i+step;
                }
            }
        }


        return s.substring(left,right);
    }

    public static String longestPalindrome3(String string) {
        //-----------------------------------
        //转换字符串
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("#");
        for (int i = 0; i < string.length(); i++) {
            stringBuilder.append(string.charAt(i));
            stringBuilder.append("#");
        }
        //-----------------------------------
        int rightIndex = 0;
        int centerIndex = 0;
        //求len中的最大
        int answer = 0;
        //answer最大时的中心
        int index = 0;
        int len[] = new int[stringBuilder.length() ];
        for (int i = 1; i < stringBuilder.length(); i++) {
            //当rightIndex > i，那么我们就在rightIndex - i 与len[2 * centerIndex - i](len[j])，取得最小值
            //因为当i + len[j] < rightIndex时，我们就把len[i]更新为len[j]
            //但是如果i + len[j] >= rightIndex时，我们暂且将len[i]定更新为rightIndex - i,超出的部分需要我们一个一个的匹配
            if (rightIndex > i) {
                len[i] = Math.min(rightIndex - i, len[2 * centerIndex - i]);
            } else {
                len[i] = 1;
            }
            //一个一个匹配
            //要么是超出的部分，要么是i > rightIndex
            while(i - len[i] >= 0 && i + len[i] < stringBuilder.length() && stringBuilder.charAt(i - len[i]) == stringBuilder.charAt(i + len[i])) {
                len[i]++;
            }
            //当 len[i] + i > rightIndex,我们需要更新centerIndex和rightIndex
            //至于为什么会这样做，理解一下rightIndex和centerIndex的含义
            if(len[i] + i > rightIndex) {
                rightIndex = len[i] + i;
                centerIndex = i;
            }
            if(len[i] > answer) {
                answer = len[i];
                index = i;
            }
        }
        //截取字符串
        //为什么index - answer + 1,因为len[i] - 1才是原来的回文字符串长度，而answer记录的是len中最大值
        return stringBuilder.substring(index - answer + 1, index + answer).replace("#", "");
    }

    public static void main(String[] args) {
        System.out.println(longestPalindrome("aaaa"));
        //System.out.println("wer".substring(2,3));
        //char a='1';
        //char b='1';
       // System.out.println(a==b);
    }

}
