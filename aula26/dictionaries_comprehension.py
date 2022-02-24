###    new_dict = {new_key:new_value for item in list}    ####
###    new_dict = {new_key:new_value for (key, value) in dict.items()}   ####
###    new_dict = {new_key:new_value for (key, value) in dict.items() if test }   ####
###    new_dict = {new_key:new_value for (index, rows) in df.iterrows()}     #####
import random

students = ['Alex', 'Calorine', 'Romeu', 'Luana', 'Jose']

score_students = {student:random.randint(1, 100) for student in students}
print(score_students)

passed_students = {key:value for (key, value)
                   in score_students.items() if value >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
print(sentence_list)
result = {word: len(word) for word in sentence_list}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {key:value * 9/ 5 + 32 for (key, value) in weather_c.items()}


print(weather_f)
