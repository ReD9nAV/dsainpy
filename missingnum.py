# #fails at [0,1];
# def missing(x):
#     x.sort();
#     y=x[0];
#     for i in range(len(x)):
#         if(y+i!=x[i]):
#             return y+i;
#     return None;

# def main():
#     li=[0,1]
#     print(missing(li));
#     return;
# main()


#better
def missing(li):
    expectedsum=sum(range(li[0],li[-1]+1))
    realsum=sum(li);
    return expectedsum-realsum;
def main():
    li=[2,4,5]
    print(missing(li));
    return;
main();