import calendar
# like_sports = False
# if like_sports == True:
#     print("good")
# else:
#     print(" very bad")
height=2
weight=80
bmi=weight/(height**2)
if bmi<=18.4:
    print ("you are underweight")
elif bmi <=24.8:
    print("you are healthy")
elif bmi <=29.9:
    print("you are overweight")
elif bmi <=34.9:
    print("you are severely overweight")
elif bmi <=39.9:
    print("you are obese")
else:
    print("you are severly obese")
print(calendar.calendar(3000))