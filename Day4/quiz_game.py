#QUIZZ_GAME_PROJECT 
file_name = "high_score.txt"

score = 0
high_score = 0

#load high_score
def load_high_score():
    global high_score

    try:
        file = open(file_name,"r")
        high_score = int(file.read())
        file.close()
    except:
        high_score = 0

#SAVE HUGH SCORE
def save_high_score():
    #open the file in write mode
    file = open(file_name,"w")
    file.write(str(high_score))
    file.close()

#PLAY QUIZZ
def play_quiz():
    global score
    score = 0
    questions = [
        "What is the capital of India?",
        "Which language is used for web development?",
        "What is 5 + 3?",
        "Which keyword is used to define a function in Python?"
    ]
    #answers
    answers = [
        "delhi",
        "python",
        "8",
        "def"
    ]
    for i in range(len(questions)):
        print("\nQ.",questions[i])
        user_answer = input("your answer:").lower()
        if user_answer == answers[i]:
            score += 1
            print("Correct")
        else:
            print("wrong!!")
            print("Correct answer is:", answers[i])

#main program
def main():
    #global allows updating same high score
    global high_score
    #load previous high score
    load_high_score()
    #ask player name
    name = input("enter your name:")
    #start quiz
    play_quiz()
    #print final score
    print("\nQuiz over")
    print(name," your score is ",score)
    if score>high_score:
        high_score=score
        print("\nCongratulation you got the high score")
        save_high_score()
    else:
        print("high score is:",high_score)
main()





