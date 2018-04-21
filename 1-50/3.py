# -*- coding: utf-8 -*-
# __author__ = 'LiuHJ'
# __project__ = 'leetcode'

class Solution:
    """Longest Substring Without Repeating Characters"""
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_dict = {}
        max_l = 0
        crt_l = 0
        for idx, char in enumerate(s):
            if (char not in letter_dict) or (letter_dict[char] < idx-crt_l):
                crt_l = crt_l + 1
            else:
                max_l = max(max_l, crt_l)
                crt_l = idx-letter_dict[char]
            letter_dict[char] = idx
        return max(max_l, crt_l)