class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        for index, item in enumerate(strs):
            if index == 0:
                commonPrefix = item
            if not commonPrefix:
                break
            if len(commonPrefix) > len(item):
                commonPrefix = commonPrefix[:len(item)]
            for i, letter in enumerate(item):
                if len(commonPrefix) <= i:
                    break
                if commonPrefix[i] != letter:
                    commonPrefix = commonPrefix[:i]

        return commonPrefix
        
        