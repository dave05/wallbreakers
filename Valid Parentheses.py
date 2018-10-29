'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    tokens=[['(',')'],['[',']'],['{','}']]
    def isCloseTerm(self, ch):
        for pair in self.tokens:
            if ch ==pair[1]:
                return True
        return False
    def openTerm(self,ch):
        for pair in self.tokens:
            if ch==pair[1]:
                return pair[0]
    def isValid(self, s):
        stack=[]
        for ch in s:
            if self.isCloseTerm(ch):
                if len(stack)==0 or self.openTerm(ch)!=stack.pop():
                    return False
            else:
                stack.append(ch)
        if len(stack)!=0:
            return False
        return True



        """
        :type s: str
        :rtype: bool
        """
        
