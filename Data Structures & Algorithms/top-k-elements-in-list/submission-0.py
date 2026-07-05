class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1


        d_sorted_list = sorted(d.items(), key=lambda x:x[1], reverse=True)
        return [i[0] for i in d_sorted_list][:k]