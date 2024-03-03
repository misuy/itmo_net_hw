def scramble(data: list):
    new_data = []
    for i in range(0, len(data), 1):
        if (i < 3):
            new_data.append(data[i])
        elif (i < 5):
            new_data.append(data[i] ^ new_data[i-3])
        else:
            new_data.append(data[i] ^ new_data[i-3] ^ new_data[i-5])
    return new_data