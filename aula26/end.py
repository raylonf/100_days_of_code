import pandas

student_dic = {
    'students': ['Angela', 'James', 'Lily'],
    'scores': [56, 76, 98]
}

# for (key, value) in student_dic.items():
#     print(value)

students_data_frame = pandas.DataFrame(student_dic)
# print(students_data_frame)

#Loop through rows of a data frame
for (index, rows) in students_data_frame.iterrows():
    # print(rows)
    if rows.students == 'Angela':
        print(rows.scores)