def twoSum(li,sum):
    sumli=[];
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i]+li[j]==sum):
                return [i,j]
def main():
    li=[3,2,4];
    sum=6;
    print(twoSum(li,sum));
    return;
main();