from typing import List
from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Bfreq = Counter()
        for word in B:
            Bfreq |= Counter(word)

        if sum(Bfreq.values()) > 10:
            return []
        return [word for word in A if not Bfreq - Counter(word)]


# words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
# words2 = ["e", "o"]

# words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
# words2 = ["l", "e"]

# words1 = ["amazon","apple","facebook","google","leetcode"]
# words2 = ["lo","eo"]

words1 = ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"]
words2 = ["c", "cc", "b"]


s1 = Solution()
res=s1.wordSubsets(words1, words2)

print(res)