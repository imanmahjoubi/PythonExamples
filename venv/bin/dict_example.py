#!/usr/bin/python3

# Python has another powerful data type, called the `dict(ionary)`. This is
# analogous to JavaScript's objects.

number_ = {'first_name': 'Jane', 'last_name': 'Doe', 'middle_initial': 'Q', 'address': 'Melbourne, Australia',
           'email': 'jane@gmail.com', 'phone_number': '5555555678', }
student_profile = number_

print(student_profile)

# Separator...
print('-' * 100)

# We get the value of a key just as in JavaScript--via bracket notation.
print(student_profile['first_name'])

# We can get a list of all the keys in the dict with the keys method.
print(student_profile.keys())

# Similarly, values returns the...Well, values.
print(student_profile.values())

# Separator...
print('-' * 100)

# If you want key/value pairs together, use items.
print(student_profile.items())

# Finally, iterating over dicts similar to iterating over lists, but:
#
#   1. You must iterate over dict.items(), not dict directly; and
#
#   2. we have two variables in scope--key and value.
for key, value in student_profile.items():
    print('The key {0} has value {1}.'.format(key, value))

# Separator...
print('-' * 100)

# If you iterate over the dict directly, you just get keys. If this is what
# you want, great, but remember to iterate over items() if you want the values
# as well. Keep in mind that the order in which dict entries appear is NOT
# predictable.
print('A more verbose way to get the value of a key...')
for key in student_profile:
    print('The key {0} has the value {1}.'.format(key, student_profile[key]))

# LIST
simple_array = [1, 2, 3]

# You index into arrays just like in JS...
print('The first element of simple_array is {0}.'.format(simple_array[0]))

# ...And can use negative indices, sa well.
print('The last element of simple_array is {0}.'.format(simple_array[-1]))

# You can add elements to a list with the append function...
simple_array.append(4)
print(simple_array)

# ...Or you can add the contents of other lists with the += operator.
# You can also use the extend function for this, but += is a wee bit faster.
simple_array += [5]
print(simple_array)

simple_array.extend([6, 7, 8])
print(simple_array)

# Separator...
print('-' * 18)

# To get the length of the list, use the len method.
print('The length of your simple array is {0}.'.format(len(simple_array)))

# ...And iteration is pretty simple, as well.
# Note that we didn't have to manually check loop conditions!
for x in simple_array:
    print('The current element of simple_array is {0}.'.format(x))

# Separator...
print('-' * 18)

# Finally, note that Python allows this nifty trick for variable assignments,
# known as unpacking. You can do this with an arbitrary number of variables,
# as long as the length of the array matches the number of variables assigned.
a, b = [1, 2]

print(a) # Prints 1
print(b) # Prints 2
