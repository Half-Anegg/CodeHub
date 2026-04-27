class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterList=[]
        for word in strs:
            skip=False
            i=0
            for wordList in letterList:
                sameAmount=0
                for letter in word:
                    if letter in wordList[0]:
                        sameAmount+=1
                if sameAmount == len(word) == len(wordList[0]):
                    letterList[i].append(word)
                    skip=True
                    break
                i+=1
            if skip==True:
                continue
            else:
                letterList.append([word])
        return letterList