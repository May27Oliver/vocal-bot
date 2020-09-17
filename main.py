def recur(k):
    if(k > 0):
        return (k + recur(k-1))
    else:return 0
print(recur(4))