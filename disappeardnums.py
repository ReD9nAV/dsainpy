def disappeard(li):
    s1=set(li);
    s2=set(range(1,len(li)+1));
    return sorted(list(s2-s1));

def main():
    li=[4,3,2,7,8,2,3,1];
    print(disappeard(li)); 
    return;
main();