cgpa=float(input("Enter CGPA:"))
perc=(cgpa*10-5)
if cgpa > 10:
    print("Please enter the correct cgpa:")
elif cgpa > 8.49:
    print("you scored distinction")
elif cgpa > 6.99:
        print("you scored first division")
elif cgpa > 5.99:
        print("you scored second division")
elif cgpa > 4.99:
        print("you are pass")
else:
        print("you are fail")
