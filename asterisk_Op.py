result = 12 * 43 # multpilication
result1 = 2 ** 4 # exponents

zeros = [0, 2] * 10 # repeat items
strings_repeat = "ABC" * 10 # repeat strings

def thing(a, b, c):
    
    print(a, b, c)
my_list = [1,2,3]

thing(*my_list)

numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
print(last)