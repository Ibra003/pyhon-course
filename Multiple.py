from Question import Qestion
question_prompt=[
    "what color are apples?\n(a) Red/Grenn\n(b) Purple\n(c) orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",


]

questions=[
    Qestion(question_prompt[0], "a"),
    Qestion(question_prompt[1], "c"),
    Qestion(question_prompt[2], "b"),
]

def run_test(question):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct")
run_test(questions)
