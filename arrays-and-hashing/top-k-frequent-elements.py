from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums))]
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num, count in hashmap.items():
            freq[count - 1].append(num)

        top_k = []
        for i in range(len(freq) - 1, -1, -1):
            for value in freq[i]:
                top_k.append(value)
                if len(top_k) == k:
                    return top_k