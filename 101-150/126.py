#!/usr/bin/env python
# encoding: utf-8
"""
@author: hongjian.liu
@date:   2018/5/7
"""
import logging
import json
import collections
import string
import time


class Solution(object):
    def findLadders(self, start_word, end_word, word_dict):
        if end_word not in word_dict:
            return []
        used_word_set = [{start_word}, {end_word}]
        half_results = [[[start_word]], [[end_word]]]
        head_tail = 0
        while not bool(used_word_set[0] & used_word_set[1]):
            meta_set = set()
            meta_dict = {}
            new_que_list = []
            for crt_que in half_results[head_tail]:
                tgt_word = crt_que[-1]
                if tgt_word in meta_dict:
                    for new_word in meta_dict[tgt_word]:
                        new_que_list.append(crt_que + [new_word])
                else:
                    meta_dict[tgt_word] = []
                    for new_word in word_dict:
                        if new_word in used_word_set[head_tail]:
                            continue
                        if self.is_similar(new_word, tgt_word):
                            meta_set.add(new_word)
                            new_que_list.append(crt_que + [new_word])
                            meta_dict[tgt_word].append(new_word)
            used_word_set[head_tail].update(meta_set)
            if not bool(new_que_list):
                return []
            half_results[head_tail] = new_que_list
            head_tail = (head_tail + 1) % 2
        connected_word_set = used_word_set[0] & used_word_set[1]
        result = []
        for connected_word in connected_word_set:
            idx_0 = self.search_queue_endded_with_target_word(half_results[0], connected_word)
            idx_1 = self.search_queue_endded_with_target_word(half_results[1], connected_word)
            for first_half in idx_0:
                for second_half in idx_1:
                    result.append(half_results[0][first_half] + list(reversed(half_results[1][second_half]))[1:])
        return result

    def search_queue_endded_with_target_word(self, queue_list, word):
        target = []
        for idx in range(len(queue_list)):
            if queue_list[idx][-1] == word:
                target.append(idx)
        return target

    def is_similar(self, word1, word2):
        idx, n_diff = 0, 0
        if word1 == word2:
            return False
        while (n_diff <= 1) and (idx < len(word1)):
            if word1[idx] != word2[idx]:
                n_diff += 1
            idx += 1
        if n_diff == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    start_word = "nanny"
    end_word = "aloud"
    with open('word_list.json') as fp:
        word_list = json.load(fp)
    print(len(word_list))
    sample = Solution()
    tic = time.clock()
    print(sample.findLadders(start_word, end_word, word_list))
    toc = time.clock()
    print(toc - tic)
