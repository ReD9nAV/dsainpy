def dup(x):
    return (len(set(x))!=len(x));

def main():
    li=[1,1,2,3]
    print(dup(li));
    return ;

main();