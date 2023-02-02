class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        def verify(cur, nxt, dic):
            i = 0
            while i < len(cur) and i < len(nxt):
                if dic[cur[i]] != dic[nxt[i]]:
                    if dic[cur[i]] > dic[nxt[i]]:
                        return False
                    break
                i+=1
            else:
                if len(cur) > len(nxt):
                    return False
            return True
        for i in range(len(words)-1):
            if not verify(words[i], words[i+1], dic):
                return False
        return True
        
        