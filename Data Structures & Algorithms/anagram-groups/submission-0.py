class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for i in strs:
            count = [0]*26 # create a new array for 26 alphabets which will store pattern everytime
            for s in i:
                count[ord(s)-ord('a')]+=1
            ans[tuple(count)].append(i)
        return list(ans.values())
        