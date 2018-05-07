# -*- coding: utf-8 -*-
# __author__ = 'LiuHJ'
# __project__ = 'leetcode'
import json
import collections
import string
import time


class Solution(object):
    def findLadders(self, start_word, end_word, word_list):
        word_set = set(word_list)
        word_set.add(start_word)
        if end_word not in word_set:
            return []
        used_word = [{start_word}, {end_word}]
        layers = [[{start_word}], [{end_word}]]
        flop = 0
        parents = collections.defaultdict(set)
        while not (layers[0][-1] & layers[1][-1]):
            next_layer = set()
            for crt_word in layers[flop][-1]:
                for new_word in self.similar_word(crt_word, word_set):
                    parents[crt_word].add(new_word)
                    if new_word not in used_word[flop]:
                        next_layer.add(new_word)
            if not next_layer:
                return []
            layers[flop].append(next_layer)
            used_word[flop].update(next_layer)
            flop = (flop + 1) % 2
        overlapped = layers[0][-1] & layers[1][-1]
        for crt_word in overlapped:
            for new_word in self.similar_word(crt_word, word_set):
                parents[crt_word].add(new_word)
        results = [[w] for w in overlapped]
        for n_layer in reversed(range(len(layers[0]) - 1)):
            results = [[w] + w_seq for w_seq in results for w in layers[0][n_layer] & parents[w_seq[0]]]
        for n_layer in reversed(range(len(layers[1]) - 1)):
            results = [w_seq + [w] for w_seq in results for w in layers[1][n_layer] & parents[w_seq[-1]]]
        return results

    def similar_word(self, word, word_set):
        for ii in range(len(word)):
            for cc in string.ascii_lowercase:
                new_word = word[:ii] + cc + word[ii + 1:]
                if (new_word not in word_set) or (cc == word[ii]):
                    continue
                yield new_word


if __name__ == '__main__':
    # start_word = "nanny"
    # end_word = "aloud"
    # with open('word_list.json') as fp:
    #     word_list = json.load(fp)
    start_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(len(word_list))
    sample = Solution()
    tic = time.clock()
    print(sample.findLadders(start_word, end_word, word_list))
    toc = time.clock()
    print(toc - tic)
