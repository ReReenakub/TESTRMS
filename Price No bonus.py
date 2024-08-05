# List of numbers
numbers = [
    60 + 8100,
    60 + 60 + 8100,
    60 + 60 + 60 + 8100,
    325 + 8100,
    60 + 325 + 8100,
    60 + 60 + 325 + 8100,
    60 + 60 + 60 + 325 + 8100,
    660 + 8100,
    60 + 660 + 8100,
    60 + 60 + 660 + 8100,
    60 + 60 + 60 + 660 + 8100,
    325 + 660 + 8100,
    60 + 325 + 660 + 8100,
    60 + 60 + 325 + 660 + 8100,
    60 + 60 + 60 + 325 + 660 + 8100,
    660 + 660 + 8100,
    60 + 660 + 660 + 8100,
    1800 + 8100,
    60 + 1800 + 8100,
    60 + 60 + 1800 + 8100,
    60 + 60 + 60 + 1800 + 8100,
    325 + 1800 + 8100,
    60 + 325 + 1800 + 8100,
    60 + 60 + 325 + 1800 + 8100,
    60 + 60 + 60 + 325 + 1800 + 8100,
    660 + 1800 + 8100,
    60 + 660 + 1800 + 8100,
    60 + 60 + 660 + 1800 + 8100,
    60 + 60 + 60 + 660 + 1800 + 8100,
    325 + 660 + 1800 + 8100,
    60 + 325 + 660 + 1800 + 8100,
    60 + 60 + 325 + 660 + 1800 + 8100,
    60 + 60 + 60 + 325 + 660 + 1800 + 8100,
    660 + 660 + 1800 + 8100,
    60 + 660 + 660 + 1800 + 8100,
    3850 + 8100,
    60 + 3850 + 8100,
    60 + 60 + 3850 + 8100,
    60 + 60 + 60 + 3850 + 8100,
    325 + 3850 + 8100,
    60 + 325 + 3850 + 8100,
    660 + 3850 + 8100,
    60 + 660 + 3850 + 8100,
    60 + 60 + 660 + 3850 + 8100,
    325 + 660 + 3850 + 8100,
    60 + 325 + 660 + 3850 + 8100,
    60 + 60 + 325 + 660 + 3850 + 8100,
    60 + 60 + 60 + 325 + 660 + 3850 + 8100,
    1800 + 3850 + 8100,
    60 + 1800 + 3850 + 8100,
    60 + 60 + 1800 + 3850 + 8100,
    60 + 60 + 60 + 1800 + 3850 + 8100,
    60 + 60 + 325 + 1800 + 3850 + 8100,
    660 + 1800 + 3850 + 8100,
    60 + 660 + 1800 + 3850 + 8100,
    60 + 60 + 660 + 1800 + 3850 + 8100,
    325 + 660 + 1800 + 3850 + 8100,
    60 + 325 + 660 + 1800 + 3850 + 8100,
    16200,
    60 + 16200,
    60 + 60 + 16200,
    60 + 60 + 60 + 16200,
    325 + 16200,
    60 + 325 + 16200,
    60 + 60 + 325 + 16200,
    60 + 60 + 60 + 325 + 16200,
    325 + 325 + 16200,
    660 + 16200,
    60 + 660 + 16200,
    60 + 60 + 660 + 16200,
    60 + 60 + 60 + 660 + 16200,
    325 + 660 + 16200,
    60 + 325 + 660 + 16200,
    60 + 60 + 325 + 660 + 16200,
    660 + 660 + 16200,
    60 + 660 + 660 + 16200,
    1800 + 16200,
    60 + 1800 + 16200,
    60 + 60 + 1800 + 16200,
    60 + 60 + 60 + 1800 + 16200,
    325 + 1800 + 16200,
    60 + 325 + 1800 + 16200,
    60 + 60 + 325 + 1800 + 16200,
    660 + 1800 + 16200,
    60 + 660 + 1800 + 16200,
    60 + 60 + 660 + 1800 + 16200,
    325 + 660 + 1800 + 16200,
    60 + 325 + 660 + 1800 + 16200,
    60 + 60 + 325 + 660 + 1800 + 16200,
    60 + 60 + 60 + 325 + 660 + 1800 + 16200,
    660 + 660 + 1800 + 16200
]

subtraction_dict = {
    60: 0,
    325: 25,
    660: 60,
    1800: 300,
    3850: 850,
    8100: 2100,
    16200: 4200
}

def subtract_values(num):
    for key, value in subtraction_dict.items():
        if num == key:
            return num - value
    return num

def handle_sums(nums):
    return sum(subtract_values(num) for num in nums)

def break_down_number(num):
    components = []
    for key in sorted(subtraction_dict.keys(), reverse=True):
        while num >= key:
            components.append(key)
            num -= key
    return components

result = [handle_sums(break_down_number(num)) for num in numbers]

for value in result:
    print(value)
