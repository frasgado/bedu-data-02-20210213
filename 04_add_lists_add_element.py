initial_list = []
# initial_list = list

element_string = 'Bedu'
element_int = 10
element_double = 3.14
element_dict = {1: 'hello', 2: 'world'}
print('before print(initial_list)')
print(initial_list)

initial_list.append(element_string)
initial_list.append(element_int)
initial_list.append(element_double)
initial_list.append(element_double)
initial_list.append(element_dict)
print('after print(initial_list)')
print(initial_list)