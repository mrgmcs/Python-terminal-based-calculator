import funcs
user_input = input("enter your operations: ") + " "
listed_items=funcs.split_input(user_input=user_input)
while len(listed_items)>1:
    funcs.clear_func(input_list=listed_items)
    resualt = funcs.operation(op_ready=listed_items)
print(resualt)
