class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n=0
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                if magazine.count(ransomNote[i])>=ransomNote.count(ransomNote[i]):
                    n+=1
        if len(ransomNote)==n:
            return True
        else:
            return False