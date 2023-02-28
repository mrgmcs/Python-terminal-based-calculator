#testlist = ["12", "/", "10" , "*","12", "/", "3", "*", "2" , "/", "2" , "+", "0.2", "-" , "3"]

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
