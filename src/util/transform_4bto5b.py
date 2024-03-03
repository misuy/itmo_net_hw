def transform_4bto5b(data: list):
    new_data = []
    for i in range(0, len(data), 4):
        res = []
        match data[i:i+4]:
            case [0, 0, 0, 0]:
                res = [1, 1, 1, 1, 0]
            case [0, 0, 0, 1]:
                res = [0, 1, 0, 0, 1]
            case [0, 0, 1, 0]:
                res = [1, 0, 1, 0, 0]
            case [0, 0, 1, 1]:
                res = [1, 0, 1, 0, 1]
            case [0, 1, 0, 0]:
                res = [0, 1, 0, 1, 0]
            case [0, 1, 0, 1]:
                res = [0, 1, 0, 1, 1]
            case [0, 1, 1, 0]:
                res = [0, 1, 1, 1, 0]
            case [0, 1, 1, 1]:
                res = [0, 1, 1, 1, 1]
            case [1, 0, 0, 0]:
                res = [1, 0, 0, 1, 0]
            case [1, 0, 0, 1]:
                res = [1, 0, 0, 1, 1]
            case [1, 0, 1, 0]:
                res = [1, 0, 1, 1, 0]
            case [1, 0, 1, 1]:
                res = [1, 0, 1, 1, 1]
            case [1, 1, 0, 0]:
                res = [1, 1, 0, 1, 0]
            case [1, 1, 0, 1]:
                res = [1, 1, 0, 1, 1]
            case [1, 1, 1, 0]:
                res = [1, 1, 1, 0, 0]
            case [1, 1, 1, 1]:
                res = [1, 1, 1, 0, 1]

        for el in res:
            new_data.append(el)
    return new_data