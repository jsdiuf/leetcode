"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-10-21 12:16
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name == typed:
            return True
        if not name or not typed:
            return False
        name = list(name)
        typed = list(typed)
        l1, l2 = [[name[0], 1]], [[typed[0], 1]]

        for i in range(1, len(name)):
            if name[i] == l1[-1][0]:
                l1[-1][1] += 1
            else:
                l1.append([name[i], 1])
        for i in range(1, len(typed)):
            if typed[i] == l2[-1][0]:
                l2[-1][1] += 1
            else:
                l2.append([typed[i], 1])
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if l1[i][0] == l2[i][0] and l1[i][1] <= l2[i][1]:
                continue
            return False
        return True


s = Solution()
print(s.isLongPressedName("leelee", "lleeelee"))
