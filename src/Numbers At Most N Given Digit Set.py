"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-9 12:19
We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.



Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.


Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
"""


class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        D = [int(i) for i in D]
        L = len(D)
        ans = 0
        T = N
        arr = []
        while T >= 10:
            arr.append(T % 10)
            T //= 10
            ans += L
            L *= len(D)
        arr.append(T)
        arr = arr[::-1]

        def findleast(e):
            ret = 0
            for i in D:
                if e > i:
                    ret += 1
                else:
                    return ret
            return ret

        for i in range(len(arr)):
            lc = findleast(arr[i])
            if lc == 0 and arr[i] not in D:
                return ans
            if lc > 0:
                ans += lc * (len(D) ** (len(arr) - i - 1))
                if arr[i] not in D:
                    return ans
        return ans + 1 if arr[-1] in D else ans


s = Solution()
print(s.atMostNGivenDigitSet(['1', '7'], 231))
