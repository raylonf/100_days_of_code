# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['ke'])
#
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')
# except KeyError as keyerror:
#     print(f'The key error {keyerror} does not exist')
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     # file.close()
#     # print('File was closed')
#     raise TypeError('This is an error that i made up.')

height = float(input('height: '))
weight = int(input('weight: '))

bmi = (weight/height**2)

if height > 3:
    raise ValueError('Human heigt should not be over 3 meters.')

print(bmi)