# name = "Bob"
# age = 25
# string = "My name is %s and I'm %i years old" % (name, age)
# print(string)

# name = "Bob"
# string1 = f"Hello, {name}"
# print(string1)
# string2 = f"1+1 is {1+1}"
# print(string2)

# stack = []
# stack.append(1)
# stack.append(2)
# pop_elem = stack.pop()
# print(stack, pop_elem)
#
# queue = []
# queue.append(1)
# queue.append(2)
#
# pop_elem = queue.pop(0)
# print(queue, pop_elem)

ages = dict()
ages['bob'] = 22
ages['emily'] =20
for key, value in ages.items():
    print(key, value)
