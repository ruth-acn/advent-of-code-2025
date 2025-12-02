def read_ids(file_path='Day 2/ids.txt'):
    with open(file_path, 'r') as file:
        return file.read().split(",")

def puzzle_one():
    ids = read_ids()
    ids = [i.split("-") for i in ids]

    invalid_count = 0
    
    for i in ids:

        # Round uneven digit numbers for the bottom range up
        id_low = i[0]
        if len(id_low) % 2 > 0:
            id_low = '1' + '0' * len(id_low)

        # Round uneven digit numbers for the top range up
        id_high = i[1]
        if len(id_high) % 2 > 0:
            id_high = '9' * (len(id_high) - 1)

        # first half of numbers in the range
        start_low = id_low[0:len(id_low)//2]
        start_high = id_high[0:len(id_high)//2]

        for j in range(int(start_low),int(start_high)+1):
            num = int(str(j) * (2))
            if (num <= int(id_high)) & (num >= int(id_low)):
                invalid_count += num 
    
    return invalid_count


if __name__ == '__main__':
    print(f"Solution 1: {puzzle_one()}")