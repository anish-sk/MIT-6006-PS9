def decode_message(A):
    """
    Return the first half of the longest palindrome subsequence of string A
    """
    dp={}
    n=len(A)
    ans=""
    for i in range(n):
        dp[(i,i)]=A[i]
    for i in range(n-1,-1,-1):
        #dp[(i,i)]=1
        for j in range(i+1,n):
            if A[i] == A[j]:
                ans = ans + A[i]
                if(j==i+1):
                    dp[(i,j)]=A[i]+A[j]
                else:
                    dp[(i,j)]=A[i]+dp[(i+1,j-1)]+A[j]
            else:
                if len(dp[(i+1,j)]) > len(dp[(i,j-1)]):
                    dp[(i,j)]=dp[(i+1,j)]
                else:
                    dp[(i,j)]=dp[(i,j-1)]
    ans=dp[(0,n-1)]
    l=len(ans)
    #print(ans)
    return ans[0:(l+1)//2]
