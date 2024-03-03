from util.util import count_subseq
from util.plot import plot_signal

def nrz(data: list, bitrate: int):
    subseq = count_subseq(data)

    l = 0
    h = len(subseq) - 1
    while (subseq[l] == 0):
        l += 1
    while (subseq[h] == 0):
        h -= 1
    l += 1
    h += 1
    f_h = bitrate / (2 * l)
    f_l = bitrate / (2 * h)

    f_m = 0
    for i in range(0, len(subseq), 1):
        f_m += (i + 1) * subseq[i] * (bitrate / ((i + 1) * 2))
    f_m /= len(data)

    x_list = []
    y_list = []

    for i in range(0, len(data), 1):
        x_list.append(i)
        y_list.append(data[i])
    x_list.append(x_list[-1] + 1)
    y_list.append(y_list[-1])
    
    print("NRZ")
    print(f"lowest frequency f_l = {f_l}")
    print(f"highest frequency f_h = {f_h}")
    print(f"middle frequency f_m = {f_m}")
    print(f"middle of the spectrum f_1/2 = {(f_h + f_l) / 2}")
    print(f"spectrum width S = {f_h - f_l}")
    print(f"bandwidth F >= {f_h - f_l}")
    print("##########\n")
    plot_signal(x_list, y_list, "nrz")

