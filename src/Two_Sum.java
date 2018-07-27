import java.util.HashMap;
import java.util.Map;

/**
 * @author weicc
 * @create 2018-07-27 9:53
 *
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.

   You may assume that each input would have exactly one solution, and you may not use the same element twice.

   Example:

   Given nums = [2, 7, 11, 15], target = 9,

   Because nums[0] + nums[1] = 2 + 7 = 9,
   return [0, 1].

   https://leetcode.com/problems/two-sum/description/
 **/
public class Two_Sum {
    public static int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            if (map.containsKey(target - numbers[i])) {
                result[1] = i ;
                result[0] = map.get(target - numbers[i]);
                return result;
            }
            map.put(numbers[i], i);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr={1,2,3,4,5};
        int target=96;
        int[] re=twoSum(arr,target);
        System.out.println(re[0]+" "+re[1]);
    }
}
