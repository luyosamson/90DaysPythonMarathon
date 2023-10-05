def func(*args):
    for i in args:
        print(i)
func(1,2,3)
list_of_arg_values=[1,3,6,9,11]
func(*list_of_arg_values)