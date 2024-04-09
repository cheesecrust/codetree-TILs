n = int(input())

customers = list(map(int, input().split()))

master, member = map(int, input().split())

answer = 0
for customer in customers:
    
    answer += 1
    if(customer <= master):
        continue
    
    customer -= master

    if(customer % member == 0):
        answer += (customer // member)
    else:
        answer += (customer // member + 1)

print(answer)