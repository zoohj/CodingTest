N, r, c= map(int, input().split()) #2^N배열, r행 c열을 몇번째로 방문
ans = 0

while N != 0:
    
    N -= 1

    #1사분면
    if r < 2**N and c < 2**N:
        ans += ( 2 ** N ) * ( 2 ** N ) * 0
    #2사분면
    elif r < 2**N and c >= 2**N:
        ans += ( 2 ** N ) * ( 2 ** N ) * 1
        c -= 2**N
    #3사분면
    elif r >= 2**N and c < 2**N:
        ans += ( 2 ** N ) * ( 2 ** N ) * 2
        r -= 2**N
    #4사분면
    elif r >= 2**N and c >= 2**N:
        ans += ( 2 ** N ) * ( 2 ** N ) * 3
        r -= 2**N
        c -= 2**N    

print(ans)