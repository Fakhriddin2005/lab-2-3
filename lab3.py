words=[]
word =input("Введите слово (для завершения введите stop)")
while word !='stop':
    words.append(word)
    word = input("Введите следующее слово")

result=" ".join(words)
print("Результат соединения слов: ")
print(result)
def check_rare_word(word):
    if 'ф' in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

word = input("Введите слово для проверки: ")
check_rare_word(word)
import random


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)


correct_answers = 0
wrong_answers = 0

while wrong_answers < 3:
    expression, correct_result = generate_expression()
    user_answer = input(f"{expression} = ")

    if user_answer.isdigit() and int(user_answer) == correct_result:
        print("Правильно.")
        correct_answers += 1
    else:
        print("Ответ неверный.")
        wrong_answers += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")

