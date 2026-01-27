# Elvis Zheng
# M02CaseStudy-AwardChecker.py
# This program will accept inputs of student names and gpa, then process them to determine eligibility for the Dean's list or Honor Roll.

while(True):

    #Recieving inputs into variables
    lastName = input("Please enter your last name: ")
    if(lastName == "ZZZ"):
        break #Breaks out of the loop which ends the program
    firstName = input("Please enter your first name: ")
    gpa = float(input("Please enter your GPA: "))

    #Testing if student meets any award criteria
    if(gpa >= 3.5):
        print(firstName + " " + lastName + " is qualified for the Dean's List!")
    elif(gpa >= 3.25):
        print(firstName + " " + lastName + " is qualified for the Honor Roll!")
    else:
        print(firstName + " " + lastName + " is not qualified for any honors.")

