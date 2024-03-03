# ПМС
# CF CC D1
# 1100 1111 1100 1100 1101 0001

from util.util import *
from codes.manchester2 import *
from codes.nrz import *
from codes.ami import *
from util.transform_4bto5b import *
from util.scramble import *

bitrate = 100000000
data = [1, 1, 0, 0,   1, 1, 1, 1,   1, 1, 0, 0,   1, 1, 0, 0,   1, 1, 0, 1,   0, 0, 0, 1]

print(f"bitrate: {bitrate}")
print("data: ПМС")
print(f"data length: {len(data)}")
print(f"bin data: {to_str_bin(data)}")
print(f"hex data: {to_str_hex(data)}")
print()

nrz(data, bitrate)
ami(data, bitrate)
manchester2(data, bitrate)


data_4bto5b = transform_4bto5b(data)
print(f"data 4bto5b length: {len(data_4bto5b)}")
print(f"bin data 4bto5b: {to_str_bin(data_4bto5b)}")
print(f"hex data 4bto5b: {to_str_hex(data_4bto5b)}")
print()

nrz(data_4bto5b, bitrate)


data_scrambled = scramble(data)
print(f"data scrambled length: {len(data_scrambled)}")
print(f"bin data scrambled: {to_str_bin(data_scrambled)}")
print(f"hex data scrambled: {to_str_hex(data_scrambled)}")
print()

nrz(data_scrambled, bitrate)