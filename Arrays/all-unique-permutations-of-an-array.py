#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        ans = []
        def dfs(cur,d):
            if not d :
                ans.append(cur)
                return 
            for i in d:
                dummy = d.copy()
                if dummy[i]==1:
                    del dummy[i]
                else:
                    dummy[i]-=1
                dfs(cur+[i],dummy)
        dict = {}
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        dfs([],dict)
        return sorted(ans)







