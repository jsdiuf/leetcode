"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-13 11:15
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around:
for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be
a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
"""
import queue
import time


class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        deadends = set(deadends)
        visited = set()
        if "0000" in deadends:
            return -1
        slots = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        def getallpath(str):
            path = []
            for i in range(4):
                index = slots.index(str[i])
                path.append(str[:i] + slots[index - 1] + str[i + 1:])
                path.append(str[:i] + slots[(index + 1) % 10] + str[i + 1:])
            return path

        q = queue.Queue()
        q.put([target, 0])
        visited.add(target)
        while not q.empty():
            s = q.get()
            if s[0] == "0000":
                return s[1]
            path = getallpath(s[0])
            for p in path:
                if p not in visited and p not in deadends:
                    q.put([p, s[1] + 1])
                    visited.add(p)
        return -1


s = Solution()
print(time.time())
print(s.openLock(["2022", "0230", "1330", "2033", "2113", "2113", "2102", "3013", "0120", "3021"], "3102"))
print(time.time())
