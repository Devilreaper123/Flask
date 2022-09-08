# friends_ages = {'Rolf':24 , 'Adam':30, 'Anne':27}
# friends_ages['Bob'] = 20
# print(friends_ages)

# friends = [
#     {'Name': 'Rolf', 'Age': 30},
#     {'Name': 'Adam', 'Age': 27},
#     {'Name': 'Anne', 'Age': 24},
# ]
# print(friends[1]['Name'])

student_attendance = {'Rolf':96,'Adam':80}
if 'Rolf' in student_attendance:
    print(f'Rolf attented: {student_attendance["Rolf"]}')

for student,attendance in student_attendance.items():
    print(f'{student} : {attendance}') 

attendance_values = student_attendance.values()
print(f'The Average Attendance is {sum(attendance_values)/len(attendance_values)}')