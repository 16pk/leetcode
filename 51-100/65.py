# -*- coding: utf-8 -*-
# __author__ = 'LiuHJ'
# __project__ = 'leetcode'

#

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.remove_blank(s)
        if len(s) == 0:
            return False
        idx = 0
        while (idx < len(s)) and (s[idx] != 'e'):
            idx += 1
        if idx == len(s):
            return self.is_float(s)
        else:
            return self.is_float(s[:idx]) and self.is_expo(s[idx + 1:])

    def is_float(self, s):
        if len(s) == 0:
            return False
        n_dot = 0
        if s[0] in {'+', '-'}:
            idx = 1
        else:
            idx = 0
        if len(s[idx:]) == 0 or s[idx:] == '.':
            return False
        while idx < len(s) and (n_dot <= 1):
            if (s[idx] >= '0') and (s[idx] <= '9'):
                idx += 1
            elif s[idx] == '.':
                n_dot += 1
                idx += 1
            else:
                return False
        if (idx == len(s)) and (n_dot <= 1):
            return True
        else:
            return False

    def is_expo(self, s):
        if len(s) == 0:
            return False
        if s[0] in {'+', '-'}:
            idx = 1
        else:
            idx = 0
        if len(s[idx:]) == 0:
            return False
        while idx < len(s):
            if (s[idx] >= '0') and (s[idx] <= '9'):
                idx += 1
            else:
                return False
        return True

    def remove_blank(self, s):
        head = 0
        tail = len(s)
        while (head < tail) and (s[head] == ' '):
            head += 1
        while (head < tail) and (s[tail - 1] == ' '):
            tail -= 1
        if tail > head:
            return s[head:tail]
        else:
            return ''