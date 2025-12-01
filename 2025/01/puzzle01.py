from helper_functions import get_input

def first_puzzle():
    i,p,n=get_input(),50,0
    for l in i:
        s=int(l[1:])
        p=((p+s) if l[0]=='R' else (p-s))%100
        if p==0:n+=1
    print(n)

def second_puzzle():
    input = get_input()

    pos = 50
    n = 0

    for l in input:
        steps = int(l[1:])
        for i in range(steps):
            if l[0] == 'R':
                pos+=1
                if pos > 99:
                    n+=1
                    pos=0
            else:
                pos-=1
                if pos == 0:
                    n+=1
                if pos < 0:
                    pos = 99
    print(n)

if __name__ == '__main__':
    first_puzzle()
    second_puzzle()