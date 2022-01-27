def groupSort(arr):
    # Write your code here
    freq = dict()
    for e in arr:
        if e in freq:
            freq[e]+=1
        else:
            freq[e]=1
    
    res = []
    
    for k,v in freq.items():
        res.append([k,v])
    res.sort(reverse=True,key = lambda x:x[1])
    # print(res)
    # for i in range(len(res)-1):
    #     for j in range(i+1,len(res)):
    #         if res[j][1]==res[i][1]:
    #             if res[j][0]<=res[i][0]:
    #                 res[j][0],res[i][0] = res[i][0],res[j][0]
    l=0
    r=l+1
    fin = list()
    
    while l<len(res) and r<len(res):
        if res[r][1]==res[l][1]:
            r+=1
        else:
            temp = res[l:r]
            temp.sort()
            fin = fin + temp
            l=r
            r+=1
    if l==0 and r==len(res):
        res.sort()
        fin = res[:]
    elif l<len(res) and r==len(res):
        temp = res[l:]
        temp.sort()
        fin +=temp
            
    return fin
