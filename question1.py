number_list = [int(item) for item in input("enter the list of number").split()]
# sol.1
sum_list=0
for i in number_list:
    sum_list= sum_list + i

print("sum of list", sum_list)

#sol.2

print("list sum",sum(number_list))

