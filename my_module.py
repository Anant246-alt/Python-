print('Imported my_module...')

test = "Test string"

def find_index(my_list, target):
    for i, value in enumerate(my_list):
        if value == target:
            return i
        
    return 0 