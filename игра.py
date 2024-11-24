import random
import time
from playsound import playsound

# сначала выводятся правила игры
print("Правила игры следующие: \n"
      + "1. Булыжник бьёт нож. \n"
      + "2. Нож разрезает пергамент. \n"
      + "3. Пергамент обёртывает булыжник.")

# варианты, которые игрок может выбрать
variants = ["булыжник", "нож", "пергамент"]
loseVariant = {"булыжник": "нож", 
            "пергамент": "булыжник", 
            "нож": "пергамент" }

def get_user_choice():
    user_input = input("Выберите: \n" + "булыжник \n" + "нож \n" + "пергамент \n").lower()
    while user_input not in variants:
        user_input = input("Неправильный выбор. Пожалуйста, выберите булыжник, нож или пергамент: ").lower()
    return user_input

def get_computer_choice():
    print("Теперь выбирает компьютер....")
    time.sleep(1)
    comp_choice = random.choice(variants)
    print("Компьютер выбрал ", comp_choice)
    return comp_choice

def main(rounds):  
    user_score = 0
    comp_score = 0
    for _ in range(rounds):
        user_input = get_user_choice()
        comp_choice = get_computer_choice()

        if user_input == loseVariant[comp_choice]:
            comp_score += 1
            print(f"К сожалению, вы проиграли. Повезёт в другой раз!")
        if comp_choice == loseVariant[user_input]:
            user_score += 1
            print(f"Поздравляю!!!! Вы выиграли!")
        if user_input == comp_choice: 
            print("Результат раунда: ничья")
        print(f"Счет раунда: Вы {user_score} - {comp_score} Компьютер")
    if user_score > comp_score:
        # воспроизводится звук
        playsound("win.mp3")
        print("Вы выиграли игру!")
    elif user_score < comp_score:
        playsound("lose.mp3")
        print("Компьютер выиграл игру!")
    else:
        print("Игра закончилась ничьей!")
       
if __name__ == "__main__":
    rounds = input("Введите количество раундов (по умолчанию 3): ")
    if not rounds.isdigit():
        rounds = 3
    else:
        rounds = int(rounds)
    main(rounds)
