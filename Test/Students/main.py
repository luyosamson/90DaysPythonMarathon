import bio
import subjects
import gen_grades

name = input("Enter your name\n")
age = int(input("Enter your age\n"))
bioData=bio.bio_infor(name,age)

print("Hello " +name+ "! you are " + str(age)+ " years old")
print("Here are your subjects and scores")
subj={"English":78,"Maths":50,"Kiswahili":47,"Chemistry":56,"Physics":70}
subj_score=subjects.sub(subj)
for n in subj:
    print(n+ ':'+str(subj_score[n]))

total=sum(subj_score.values())
print("Total Marks",total)

average_score=total/5

print("Average score",average_score)

my_grade=gen_grades.grades(average_score)
print("You are grade",my_grade)