questions = ["Qovun nima?", "Olma mevami?", "Tarvuz poliz ekinimi?"]
options = [["sabzavot", "meva", "texnika"], ["ha", "yo'q", "u go'sht"], ["ha", "daraxtda o'sadi", "bilmadim"]]
answers = [1, 0, 1]


def greeting():
    """Salomlashish"""
    print("=" * 10, "BekKing", "=" * 10)
    print("Savol-javob o'yiniga xush kelibsiz")
    print("=" * 30)


def get_ready():
    print("O'yinni boshlashga tayyormisiz?(ha/yoq)")
    yes_or_no = input(">>>").replace(" ", "").lower()
    if yes_or_no == "ha":
        return True
    return False


def remove_question(question):
    questions.remove(question[0])
    options.remove(question[1])


def get_random_question_and_options():
    
    import random

    question = random.choice(questions)

    index_question = questions.index(question)

    question_options = options[index_question]

    answer1 = question_options[question_options.index(question_options[answers[index_question]])]

    random.shuffle(question_options)

    answer = question_options.index(answer1)

    return question, question_options, answer


def start_question():
    n = 1
    score = 0

    while len(questions) != 0:
        q = get_random_question_and_options()
        remove_question(q)

        print(f"{n}) {q[0]}")
        print("=" * 30)

        for idx, option in enumerate(q[1]):
            print(f"{idx + 1}) {option}")

        user_answer = int(
            input(f"Javobni tanlang(1-{len(q[1])})>>>")
        )

        if user_answer - 1 == q[2]:
            print("To'g'ri javob berdingiz!")
            score += 1
        else:
            print("Noto'g'ri javob berdingiz!")
            print("To'g'ri javob:", q[1][q[2]])

        print("=" * 30)
        n += 1

    print("O'yin tugadi!")
    print(f"Sizning natijangiz: {score} / {n - 1}")


def main():
    greeting()
    if get_ready():
        start_question()
    else:
        print("O'yin bekor qilindi.")


main()
