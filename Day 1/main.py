import numpy as np

def read_code(file_path='Day 1/code.txt'):
    with open(file_path, 'r') as file:
        return file.read().splitlines()
    
def puzzle_one():
    code = read_code()

    dial = [50]
    sign_ref = {'R': 1, 'L': -1}

    for i in range(len(code)):
        dial.append(dial[i]+int(code[i][1:])*sign_ref[code[i][0]])

    ans = np.mod(dial,100)
    return sum(ans==0)

def puzzle_two():
    code = read_code()

    dial = [50]
    sign_ref = {'R': 1, 'L': -1}

    for i in range(len(code)):
        rotations = np.array(range(1,1+int(code[i][1:])))*sign_ref[code[i][0]]
        dial = np.concatenate((dial, dial[-1] + rotations))

    ans = np.mod(abs(dial),100)
    return sum(ans==0)

if __name__ == '__main__':
    print(f"Solution 1: {puzzle_one()}")
    print(f"Solution 2: {puzzle_two()}")