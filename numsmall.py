# def small(array):
#     temparray=sorted(array)
#     hashmap={};
#     for i,num in enumerate(temparray):
#         if num not in hashmap:
#             hashmap[num]=i;
#     ret=[];
#     for i in array:
#         ret.append(hashmap[i]);
#     return ret;

# def main():
#     li=[8,1,2,2,3];
#     print(small(li));
#     return ;
# main();
def smol(array):
    retarr=[]
    for i in  range(len(array)):
        count=0;
        for j in range(len(array)):
            if(array[i]>array[j]):
                count+=1;
        retarr.append(count);
    return retarr

def main():
    li=[8,1,2,2,3];
    print(smol(li))
    return ;
main();