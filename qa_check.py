from qa_data import questions

#is_game_on = True

for q in questions:
    converted_answer = False
    user_answer = input(f"{q.get('question')} (True/False): ").lower()
    if user_answer == "true":
        converted_answer = True
    else:
        converted_answer = False
    if converted_answer == q.get('answer'):
        print(f"{user_answer.capitalize()}, you are right.")
    else:
        print(f"Wrong answer. You said that this statement is {user_answer.capitalize()}.")