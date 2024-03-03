from util.util import *
from util.plot import *

def ami(data: list, bitrate: int):
    x_list = []
    y_list = []
    curr = 1

    subseq = [0 for i in range(0, len(data), 1)]
    streak = 1
    for i in range(0, len(data), 1):
        x_list.append(i)
        if (data[i] == 0):
            y_list.append(0)
        else:
            y_list.append(curr)
            curr *= -1
        
        if (i > 0):
            if (data[i-1] == data[i] == 0):
                streak += 1
            else:
                subseq[streak] += 1
                streak = 0
    
    l = 0
    h = len(subseq) - 1
    while (subseq[l] == 0):
        l += 1
    while (subseq[h] == 0):
        h -= 1
    l += 1
    h += 1
    f_l = bitrate / (2 * h)
    f_h = bitrate / (2 * l)

    f_m = 0
    for i in range(0, len(subseq), 1):
        f_m += (i + 1) * subseq[i] * (bitrate / ((i + 1) * 2))
    f_m /= len(data)
    
    x_list.append(x_list[-1] + 1)
    y_list.append(y_list[-1])

    print("AMI")
    print(f"lowest frequency f_l = {f_l}")
    print(f"highest frequency f_h = {f_h}")
    print(f"middle frequency f_m = {f_m}")
    print(f"middle of the spectrum f_1/2 = {(f_h + f_l) / 2}")
    print(f"spectrum width S = {f_h - f_l}")
    print(f"bandwidth F >= {f_h - f_l}")
    print("##########\n")
    plot_signal(x_list, y_list, "ami")

# Передрий (8) Михаил (6) Сергеевич (9)
# (192 + Н + О).(Ф + Н).(И + Н).(Ф + И)
# 192 + 9 + 2 . 8 + 2 . 6 + 2 . 8 + 6
# 203.10.8.14