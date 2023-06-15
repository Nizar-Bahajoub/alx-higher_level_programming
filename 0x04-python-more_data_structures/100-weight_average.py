#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (float(0))
    else:
        score = 0
        wgt = 0
        for i in my_list:
            score += (i[0] * i[1])
            wgt += i[1]
        return (score / wgt)
