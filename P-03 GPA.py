# Write a Python program to convert GPAs to letter grades according to the following rules:
# GPAs : Grades ⇒ 4.0 : A+, 3.7 : A, 3.4 : A-, 3.0 : B+, 2.7 : B, 2.4 : B-, 2.0 : C+, 1.7 : C, 1.4 : C-, below : F

gpa = float ( input ( " Enter your GPA = " ) )

if gpa >= 4.0 :
    grade = " A+ "

elif gpa >= 3.7 :
    grade = " A "  

elif gpa >= 3.4 :
    grade = " A- "

elif gpa >= 3 :
    grade = " B+ "

elif gpa >= 2.7 :
    grade = " B "

elif gpa >= 2.4 :
    grade = " B- "

elif gpa >= 2 :
    grade = " C+ "

elif gpa >= 1.7 :
    grade = " C "

elif gpa >= 1.4 :
    grade = " C- "
    
else :
    grade = " F "

print ( " Your grade is = " , grade)