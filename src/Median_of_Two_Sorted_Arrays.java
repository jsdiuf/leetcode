/**
 * @author weicc
 * @create 2018-07-27 17:58
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.

   Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

   You may assume nums1 and nums2 cannot be both empty.



   Example 1:

   nums1 = [1, 3]
   nums2 = [2]

   The median is 2.0
   Example 2:

   nums1 = [1, 2]
   nums2 = [3, 4]

   The median is (2 + 3)/2 = 2.5

   https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 **/
public class Median_of_Two_Sorted_Arrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int len1 = nums1.length;
        int len2 = nums2.length;
        int i = 0, j = 0;

        int prenum = 0;
        int lastnum = 0;

        while (true) {
            if ((i + j < ((len1 + len2) / 2 + 1)) && (j < len2) && (i == len1 || nums1[i] > nums2[j])) {
                prenum = lastnum;
                lastnum = nums2[j];
                j++;
                continue;
            }

            if ((i + j < ((len1 + len2) / 2 + 1)) && (i < len1) && (j == len2 || nums1[i] <= nums2[j])) {
                prenum = lastnum;
                lastnum = nums1[i];
                i++;
                continue;
            }
            break;
        }
        if ((len1 + len2) % 2 == 0) {
            return ((double) prenum + (double) lastnum) / 2;
        } else {
            return (double) lastnum;
        }
    }


    public static void main(String[] args) {
        int[] arr1 = {};
        int[] arr2 = {2, 2};
        System.out.println(findMedianSortedArrays(arr1, arr2));
    }
}
