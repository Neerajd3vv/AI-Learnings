from question import question

questions_prompts = [
    "What is the capital of France?\n(a) London\n(b) Berlin\n(c) Paris\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Saturn\n\n"
]


questions = [
    question(questions_prompts[0], "c"),
    question(questions_prompts[1], "b"),
    question(questions_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct.")        


run_test(questions)