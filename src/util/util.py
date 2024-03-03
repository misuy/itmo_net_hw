def count_subseq(data: list):
    subseq = [0 for i in range(0, len(data), 1)]

    streak = 1
    for i in range(1, len(data), 1):
        if (data[i-1] == data[i]):
            streak += 1
        else:
            subseq[streak-1] += 1
            streak = 1
    subseq[streak-1] += 1

    return subseq

def to_decimal(data: list):
    ret = 0
    for i in range(0, len(data), 1):
        ret += data[len(data) - i - 1] * (2 ** i)
    return ret

def to_str_bin(data: list):
    return bin(to_decimal(data))

def to_str_hex(data: list):
    return hex(to_decimal(data))