"""
@version: python3.5
@author: jsdiuf
@contact: weichun713@foxmail.com
@time: 2018-8-3 15:22
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list=[]

    def gen(self,list,n):

        if n==0:
            return

        t=[]
        for e in list:
