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

def puzzle_two():
    ids = read_ids()
    ids = [i.split("-") for i in ids]

    invalid_count = 0
    
    for i in ids:

        id_low = i[0]
        id_high = i[1]

        num_digits = {}

        invalid_ids = []

        if len(id_low) != len(id_high):
            num_digits[len(id_low)] = {'max':'9' * len(id_low), 'min': id_low}
            num_digits[len(id_high)] = {'max': id_high, 'min': '1' + '0' * (len(id_high)-1)}

        else:
            num_digits[len(id_low)] = {'max': id_high, 'min': id_low}

        for n in num_digits:
            id_max = num_digits[n]['max']
            id_min = num_digits[n]['min']
            
            factors = []
            for i in range(1, n):
                if n % i == 0:
                    factors.append(i)

            for f in factors:
                start_high = id_max[0:f]
                start_low = id_min[0:f]

                r = n // f

                for j in range(int(start_low),int(start_high)+1):
                    num = int(str(j) * r)
                    if (num <= int(id_max)) & (num >= int(id_min)):
                        invalid_ids.append(num)

        invalid_ids = list(set(invalid_ids))
        invalid_count += sum(invalid_ids)


    return invalid_count

if __name__ == '__main__':
    print(f"Solution 1: {puzzle_one()}")
    print(f"Solution 2: {puzzle_two()}")