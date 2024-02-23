#Using hashmap
#TC: O(n*k)
#SC: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for character in word:
                count[ord(character) - ord("a")] += 1

            grp[tuple(count)].append(word)
        
        return grp.values()