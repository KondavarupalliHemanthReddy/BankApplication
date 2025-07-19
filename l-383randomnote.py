class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d={}
        for i in ransomNote:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=0
        for i,j in d.items():
            if j<=magazine.count(i):
                res+=1
        if len(d)==res:
            return True
        return False