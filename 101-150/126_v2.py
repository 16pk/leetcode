#!/usr/bin/env python
# encoding: utf-8
"""
@author: hongjian.liu
@date:   2018/5/7
"""
import json
import collections
import time


class Solution(object):
    def findLadders(self, start_word, end_word, word_list):
        word_set = set(word_list)
        if end_word not in word_set:
            return []
        used_word_set = [{start_word}, {end_word}]
        half_results = [[[start_word]], [[end_word]]]
        flop = 0
        parents = collections.defaultdict(list)
        while not bool(used_word_set[0] & used_word_set[1]):
            meta_set = set()
            new_que_list = []
            for crt_que in half_results[flop]:
                tgt_word = crt_que[-1]
                if tgt_word in parents:
                    for new_word in parents[tgt_word]:
                        new_que_list.append(crt_que + [new_word])
                else:
                    for ii in range(len(tgt_word)):
                        for pp in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = tgt_word[:ii] + pp + tgt_word[ii + 1:]
                            if (pp == tgt_word[ii]) or (new_word in used_word_set[flop]):
                                continue
                            if new_word in word_set:
                                parents[tgt_word].append(new_word)
                                meta_set.add(new_word)
                                new_que_list.append(crt_que + [new_word])
            used_word_set[flop].update(meta_set)
            if not bool(new_que_list):
                return []
            half_results[flop] = new_que_list
            flop = (flop + 1) % 2
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
