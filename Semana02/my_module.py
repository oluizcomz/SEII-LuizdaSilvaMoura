print('import my_module..')
test = 'Test_String'
def find_index(to_search,target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1