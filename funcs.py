#functions
def split_input(user_input):
    number = ""
    splited = []
    for i in user_input:
        if i in "1234567890":
            number+=i
        elif i in "+-/*":
            if number:
                splited.append(number)
            splited.append(i)
            number = ""
        elif i == "":
            pass
        elif i == "(" or i == ")":
            if number:
                splited.append(number)
            splited.append(i)
            number=""
        else:
            if number:
                splited.append(number)
            number=""
    return splited
def clear_func(input_list):
    for i in input_list:
        if i == "":
            input_list.remove(i)
        else:
            continue
def operation(op_ready):
    for i in range(0,len(op_ready)):
        if op_ready[i] == "*":
            new_vlaue = float(op_ready[i-1]) * float(op_ready[i+1])
            op_ready[i] = new_vlaue
                #testlist.remove(testlist[i])
            try:
                op_ready[i-1] = ""
                op_ready[i+1] = ""
                clear_func(op_ready)
                #break
                i=0
                break
            except:
                break
        elif op_ready[i] == "/":
            new_vlaue = float(op_ready[i-1]) / float(op_ready[i+1])
            op_ready[i] = new_vlaue
            #testlist.remove(testlist[i])
            try:
                op_ready[i-1] = ""
                op_ready[i+1] = ""
                clear_func(op_ready)
                #break
                i=0
                break
            except:
                break
        elif op_ready[i] == "+":
            if "*" not in op_ready and "/" not in op_ready:
                new_vlaue = float(op_ready[i-1]) + float(op_ready[i+1])
                op_ready[i] = new_vlaue
                #testlist.remove(testlist[i])
                try:
                    op_ready[i-1] = ""
                    op_ready[i+1] = ""
                    clear_func(op_ready)
                    #break
                    i=0
                    break
                except:
                    break
            else:
                continue
        elif op_ready[i] == "-":
            if "*" not in op_ready and "/" not in op_ready:
                new_vlaue = float(op_ready[i-1]) - float(op_ready[i+1])
                op_ready[i] = new_vlaue
                #testlist.remove(testlist[i])
                try:
                    op_ready[i-1] = ""
                    op_ready[i+1] = ""
                    clear_func(op_ready)
                    #break
                    i=0
                    break
                except:
                    break
            else:
                continue
    return op_ready
def find_p(val, index_po, index_pc):
    for po in range(len(val)):
        if val[po] == "(":
            index_po = po
    for pc in range(len(val)):
        if val[pc] == ")":
            if pc>index_po:
                index_pc = pc
                break
            else:
                continue
    if index_po<index_pc:
        return list((index_po, index_pc))
    else:
        return "input error" 
def operation_p(listed):
    while "(" in listed:
        in_parentheses = find_p(listed,index_po=0,index_pc=0)
        resualt = operation(listed[in_parentheses[0]+1: in_parentheses[1]])[0]
        listed[in_parentheses[0]] = str(resualt)
        del listed[in_parentheses[0]+1:in_parentheses[1]+1]
    return listed