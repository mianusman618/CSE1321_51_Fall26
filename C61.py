quiz_scores=[]
for i in range(5):
    user_input=int(input(f"Enter Score for Student {i+1} : "))
    quiz_scores.append(user_input)
print("QUIZ SCORES = ",quiz_scores)
sum=0
for score in quiz_scores:
    sum+=score
print("AVG SCORE = ",sum/len(quiz_scores))