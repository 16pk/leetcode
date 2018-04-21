# -*- coding: utf-8 -*-
# __author__ = 'LiuHJ'
# __project__ = 'leetcode'

"""
This is not a good solution as it does merge two arrays into a sorted array more than just trying to find median value.
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        kk = (len1 + len2) // 2
        kk0 = (len1 + len2 - 1) // 2
        idx1, idx2 = 0, 0
        count = 0
        new_array = []
        while (idx1 < len1) and (idx2 < len2) and (idx1 + idx2 <= kk):
            if count / 2 == count // 2:
                pre2 = idx2
                idx2 = find_first_ge_idx(nums2, pre2, len2 - 1, nums1[idx1])
                print('idx1', idx1, 'idx2', idx2)
                new_array = new_array + nums2[pre2:idx2] + [nums1[idx1]]
                idx1 = idx1 + 1
            else:
                pre1 = idx1
                idx1 = find_first_ge_idx(nums1, pre1, len1 - 1, nums2[idx2])
                print('idx1', idx1, 'idx2', idx2)
                new_array = new_array + nums1[pre1:idx1] + [nums2[idx2]]
                idx2 = idx2 + 1
            count = count + 1
        if idx1 == len1:
            new_array = new_array + nums2[idx2:len2]
        elif idx2 == len2:
            new_array = new_array + nums1[idx1:len1]
        return (new_array[kk] + new_array[kk0]) / 2


def find_first_ge_idx(array, head, tail, target):
    if array[tail] < target:
        return len(array)
    elif array[head] >= target:
        return head
    while tail > head + 1:
        mid = (head + tail) // 2
        if array[mid] < target:
            head = mid
        else:
            tail = mid
    return tail

class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        kk = (m + n) // 2
        head = 0
        tail = m
        flag = False
        while not flag:
            mid = (head+tail) // 2
            if (mid>0) and nums1[mid-1] > nums2[kk-mid]:
                tail = mid-1
                continue
            if (mid<m) and nums1[mid] < nums2[kk-mid-1]:
                head = mid+1
                continue
            if mid==0:
                left_max = nums2[kk-1]
            elif kk-mid==0:
                left_max = nums1[mid-1]
            else:
                left_max = max(nums1[mid-1], nums2[kk-mid-1])
            if mid==m:
                right_min = nums2[kk-m]
            elif kk-mid==n:
                right_min = nums1[mid]
            else:
                right_min = min(nums1[mid], nums2[kk-mid])
            if (m + n) % 2 == 0:
                return (right_min + left_max) / 2
            else:
                return right_min
array1 = [1, 2]
array2 = [3, 4]
sample = Solution2()
print(sample.findMedianSortedArrays(array1, array2))