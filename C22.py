quiz_num=1
user_input=input(f"Enter Quiz {quiz_num} score  or S to stop: ")

quiz_score_sum=0
count=0
while user_input != "S":
    user_input2 = int(user_input)
    count+=1
    quiz_score_sum+=user_input2
    quiz_num+=1
    user_input = input(f"Enter Quiz {quiz_num} score  or S to stop: ")
if count>0:
    print("AVG OF YOUR QUIZZES = ",quiz_score_sum/count)
else:
    print("No quizzes entered")
