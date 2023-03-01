import funcs
user_input = input("enter your operations: ") + " "
listed_items=funcs.split_input(user_input=user_input)
listed_items = funcs.operation_p(listed=listed_items)
while len(listed_items)>1:
    funcs.clear_func(input_list=listed_items)
    listed_items = funcs.operation(op_ready=listed_items)
#this loop makes listed_items smaller and ends whne it reches to one answer in listed_items
resualt = listed_items
print(resualt)
#print(funcs.operation(op_ready=listed_items))