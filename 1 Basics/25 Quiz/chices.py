from Question_Class import Question

Question_prompts = ["what is 2+2= ? \n(a)1\n(b)2\n(c)3\n(d)4\n",
                    "what is 1+1= ? \n(a)1\n(b)2\n(c)3\n(d)4\n",
                    "what is 1+2= ? \n(a)1\n(b)2\n(c)3\n(d)4\n"
                    ]

question_answer = [
    Question(Question_prompts[0], "d"),
    Question(Question_prompts[1], "b"),
    Question(Question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answers:
            score += 1

    print("you got " + str(score) + "/" + str(len(Question_prompts)))


run_test(question_answer)
