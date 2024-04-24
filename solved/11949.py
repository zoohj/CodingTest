N, M= map(int, input().split())

num_ticket = []

for i in range(N):
    num_ticket.append(int(input()))

for i in range(1, M+1):
    for index in range(0, len(num_ticket)-1):
        if num_ticket[index] % i > num_ticket[index+1] % i:
            # 카드 교환
            X = num_ticket[index]
            num_ticket[index]=num_ticket[index+1]
            num_ticket[index+1]= X

for num in num_ticket:
    print(num)