n = int(input())

customers = list(map(int, input().split()))

master, member = map(int, input().split())

answer = 0
for customer in customers:

    if(customer < master):
        answer += 1
    else:
        customer -= master
        answer += (1 + customer // member + (customer % member)) 

print(answer)