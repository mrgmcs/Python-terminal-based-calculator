import funcs
#listed = ["12", "/", "(","10" , "*","12",")","/", "(", "3", "*", "2",")" , "/", "2" , "+", "0.2", "+","(","10","-","3",")"]
user_input = input("enter your operations: ") + " "
listed_items=funcs.split_input(user_input=user_input)
listed_items = funcs.operation_p(listed=listed_items)
while len(listed_items)>1:
    funcs.clear_func(input_list=listed_items)
    resualt = funcs.operation(op_ready=listed_items)
print(resualt)