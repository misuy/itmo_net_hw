from util.util import *
from util.plot import *

def manchester2(data: list, bitrate: int):
    
    off = 0
    x_list = []
    y_list = []

    not_equal = 0
    equal = 0
    for i in range(0, len(data), 1):
        x_list.append(off)
        x_list.append(off + 1/2)
        off += 1
        if (data[i] == 1):
            y_list.append(1)
            y_list.append(0)
        else:
            y_list.append(0)
            y_list.append(1)
        if (i > 0):
            if (data[i-1] == data[i]):
                equal += 2
            else:
                not_equal += 2
    
    if (data[-1] == data[-2]):
        equal += 1
    else:
        not_equal += 1

    f_l = 0
    f_h = 0
    if (equal == 0):
        if (not_equal == 0):
            print("err")
            return
        else:
            f_l = bitrate
            f_h = bitrate
    else:
        if (not_equal == 0):
            f_l = bitrate / 2
            f_h = bitrate / 2
        else:
            f_l = bitrate / 2
            f_h = bitrate
    
    f_m = (not_equal * bitrate + equal * bitrate / 2) / (len(data) * 2)

    print("MANCHESTER 2")
    print(f"lowest frequency f_l = {f_l}")
    print(f"highest frequency f_h = {f_h}")
    print(f"middle frequency f_m = {f_m}")
    print(f"middle of the spectrum f_1/2 = {(f_h + f_l) / 2}")
    print(f"spectrum width S = {f_h - f_l}")
    print(f"bandwidth F >= {f_h - f_l}")
    print("##########\n")
    plot_signal(x_list, y_list, "manchester2")


        

        