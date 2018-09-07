"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-9-7 9:11
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
https://leetcode.com/problems/longest-valid-parentheses/solution/
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        ...()()...
        ...(())(())...
        """
        if not s:
            return 0
        L = len(s)

        ans = []
        maxL = 0
        for i in range(1, L):
            if s[i - 1] == "(" and s[i] == ")":
                ans.append([i - 1, i])
                maxL = 2
        if not maxL:
            return 0

        def helper1():
            change = False
            for i in range(len(ans)):
                while ans[i][0] - 1 >= 0 and ans[i][1] + 1 < L and s[ans[i][0] - 1] == "(" and s[ans[i][1] + 1] == ")":
                    ans[i][0] -= 1
                    ans[i][1] += 1
                    change = True
            return change

        def helper2():
            change = False
            for i in range(len(ans) - 1, 0, -1):
                if ans[i][0] == ans[i - 1][1] + 1:
                    ans[i - 1][1] = ans[i][1]
                    del ans[i]
                    change = True
            return change

        while 1:
            if not helper1() and not helper2():
                break

        for e in ans:
            maxL = max(maxL, e[1] - e[0] + 1)

        return maxL

    #stack
    def longestValidParentheses2(self, s):
        stk = []
        stk.append(-1)
        l = len(s)
        r = 0
        for i in range(l):
            if s[i] == "(":
                stk.append(i)
            else:
                stk.pop()
                if len(stk) != 0:
                    r = max(r, i - stk[-1])
                else:
                    stk.append(i)
            print(stk)
        return r

    """  dp
    //1
       int longestValidParentheses(string s) {
            if(s.length() <= 1) return 0;
            int curMax = 0;
            vector<int> longest(s.size(),0);
            for(int i=1; i < s.length(); i++){
                if(s[i] == ')'){
                    if(s[i-1] == '('){
                        longest[i] = (i-2) >= 0 ? (longest[i-2] + 2) : 2;
                        curMax = max(longest[i],curMax);
                    }
                    else{ // if s[i-1] == ')', combine the previous length.
                        if(i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                            longest[i] = longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                            curMax = max(longest[i],curMax);
                        }
                    }
                }
                //else if s[i] == '(', skip it, because longest[i] must be 0
            }
            return curMax;
        }
    
    
    //2
    int longestValidParentheses(string s) {
        if(s.length() <= 1) return 0;
        int curMax = 0;
        vector<int> longest(s.size(),0);
        for(int i=1; i < s.length(); i++){
            if(s[i] == ')' && i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                    longest[i] = longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                    curMax = max(longest[i],curMax);
            }
        }
        return curMax;
    }
    """


s = Solution()
print(s.longestValidParentheses2(")(()())"))
