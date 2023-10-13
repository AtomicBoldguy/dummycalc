def res_calc(one="", res=0):
    # self.label_text = customtkinter.StringVar()
    # res = 0
    print(one)
    pos = one.find("+")
    temp = one[pos + 1:]
    pos1 = temp.find("+")
    if pos != -1:
        print(one[:pos], temp, temp[:temp.find("+")])
        if pos1 != -1:
            res += int(one[:pos])
            res_calc(one=temp, res=res)
            print(res, '---')
        else:
            res += int(temp)
            print(res, '++')
            res_calc(one=temp, res=res)
    else:
        res += int(one)
        print(res, one, 'fso')
        print(res)


one = input('go -> ')
res_calc(one)
