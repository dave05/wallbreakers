class Solution:
    def numJewelsInStones(self, J, S):
        jewels_count=dict()
        count=0
        for ch in S:
            jewels_count[ch]=jewels_count.get(ch,0)+1
       # print(jewels_count)
        for ch in J:
            if ch in jewels_count:
                count+=jewels_count[ch]

        return count
