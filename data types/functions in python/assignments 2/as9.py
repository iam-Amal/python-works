#.Define a function that accepts roll number and returns whether the student is present or absent.

def student(rollno):
    no = [1,2,3,4,5,6,7,8,9,10]
    if rollno in no:
        print('present')
    else:
        print('absent')


rollno =int(input('enter the rollnum ;'))
student(rollno)
