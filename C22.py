from itertools import count

quiz_num=1
user_input=int(input(f"Enter Quiz {quiz_num} score  or -1 to stop: "))
quiz_score_sum=0
count=0
while user_input != -1:
    count+=1
    quiz_score_sum+=user_input
    quiz_num+=1
    user_input = int(input(f"Enter Quiz {quiz_num} score  or -1 to stop: "))
if count>0:
    print("AVG OF YOUR QUIZZES = ",quiz_score_sum/count)
else:
    print("No quizzes entered")
