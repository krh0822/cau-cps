import random

total_students=30
total_teams=6

students=range(total_students) #0~29

list_students=list(students) 

random.shuffle(list_students) #팀 구성원들 섞어주기

project_team=[]
for i in range(total_teams): #0~5
   
    num_of_numbers=int(total_students/total_teams)
    index=i*num_of_numbers #i= 0,1,2,3,4,5 -> 0,5,10,15,20,25 멤버수만큼 건너뛰면서 원소를 뽑기 때문
    project_team.append(list_students[index:index+num_of_numbers]) #index부터 index+num_of_numbers-1만큼 따로 출력하겠다
                       
for i in project_team:
    print (i)