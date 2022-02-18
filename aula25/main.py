# with open('aula25\weather_data.csv', 'r') as f:
#     data = f.readlines()
#
# for d in data:
#     d = d.replace(',', ' ').split()
#     day = d[0]
#     temp = d[1]
#     condi = d[2]
#     print(day +' '+  temp +' '+ condi)
#
import pandas
# import csv
#
# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temp = []
#     for d in data:
#         if d[1] != 'temp':
#             temp.append(int(d[1]))
#     print(temp)

# data = pandas.read_csv('weather_data.csv')
# print(data)
# print()
# print(data['temp'])
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# average_temp = data['temp'].mean()
# print(average_temp)
# max_temp = data['temp'].max()
# print(max_temp)
#
# #Get data im collumns
# print(data['condition'])
# print(data.condition)

#get data in row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# graus_fahr = int(monday.temp) * 1.8 + 32
# print(graus_fahr)

#created Dataframe from sratch
# data_dic = {
#     'students' : ['Amy', 'James', 'Angela'],
#     'scores':[76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dic)
# print(data)
# data.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_color = data['Primary Fur Color']
gray_count = len(data[data_color == 'Gray'])
cinnamon_count = len(data[data_color == 'Cinnamon'])
black_count = len(data[data_color == 'Black'])
print(gray_count)
print(cinnamon_count)
print(black_count)


# data_color = data['Primary Fur Color'].tolist()
# c = 0
# g = 0
# b = 0
# for d in data_color:
#     if d == 'Cinnamon':
#         c += 1
#     if d == 'Gray':
#         g += 1
#     if d == 'Black':
#         b += 1
# print(c)
# print(b)
# print(g)
#
# data_dic = {
#     'Fur Color' : ['cinnamon', 'black', 'gray'],
#     'count': [c, b, g]
# }
#
# new_data = pandas.DataFrame(data_dic)
# new_data.to_csv('Central_park_colors.csv')