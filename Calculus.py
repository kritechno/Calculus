msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_ =[0,1,2,3,4,5,6,7,8,9,"Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"



def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        
        return True
    else:
        return False
def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg = msg + msg_7
    if v1 == 0 or v2 == 0 and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        return

memory = 0

while True:
    print(msg_0)
    calc = input()
    calc_list = calc.split()
    calc_list2 = []
    if calc_list[0] == "M":
        calc_list[0] = float(memory)
    if calc_list[2] == "M":
        calc_list[2] = float(memory)
    try:
        calc_list2.append(float(calc_list[0]))
        calc_list2.append(float(calc_list[2]))
        a = calc_list2[0]
        b = calc_list2[1]
        opers = ["+", "-", "/", "*"]
        oper = calc_list[1]
        if calc_list[1] not in opers:
            print(msg_2)
        if oper == "/" and b == 0:
            check(a, b, oper)
            print(msg_3)
        elif calc_list[1] in opers:
            check(a, b, oper)
            if oper == '+':
                answer = float(a + b)
                print(answer)
            elif oper == '-':
                answer = float(a - b)
                print(answer)
            elif oper == '*':
                answer = float(a * b)
                print(answer)
            elif oper == "/" and b != 0:
                answer = float(a / b)
                print(answer)
            answer_mem = input(msg_4)
            if answer_mem == "y":
                if is_one_digit(answer):
                    msg_index = 10
                    while msg_index < 13:
                        answer_mem = input(msg_[msg_index])
                        if answer_mem == "y":
                            msg_index = msg_index + 1
                            continue
                        if answer_mem == "n":
                            break
                    if msg_index >= 13:
                        memory = answer
                else:
                    memory = answer
            elif answer_mem == "n":
                pass
            answer_cont = input(msg_5)
            if answer_cont == "y":
                continue
            if answer_cont == "n":
                break
    except ValueError:
        print(msg_1)