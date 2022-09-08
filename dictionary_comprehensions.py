# import getpass
# users = [
#     (0,"Bob","password"),
#     (1,"Rolf","bob123"),
#     (2,"Jose","longp4assword"),
#     (3,"username","1234"),
# ]

# username_mapping = {user[1]:user for user in users}
# # print(username_mapping["Bob"])
# username_inp = input("Enter username : ")
# password_inp = getpass.getpass()

# _,username , password = username_mapping[username_inp]
# if password_inp == password : 
#     print("Details are correct")
# else : 
#     print("Incorrect pass")


student = {'name':'Jose','school':'Computing','grades':(66,77,88)}

def average_grade(data):
    grades = data['grades']
    print(sum(grades) / len(grades))
    return sum(grades) / len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0 
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])
    print(total)
    print(count)
    print(total/count)
    return total/count

average_grade(student)
average_grade_all_students(student)