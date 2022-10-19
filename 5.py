hat_list = [1,2,3,4,5]
wise_input = int(input("Input A Number From [1,2,3,4,5] :")) 
hat_list[len(hat_list)//2]= wise_input
print(hat_list)
hat_list.pop(-1)
print(len(hat_list))