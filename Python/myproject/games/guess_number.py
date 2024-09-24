import random

number = random.randint(1, 100)  # 1から100までのランダムな数字を選ぶ
attempts = 0

print("1から100までの数字を当ててください！")

while True:
    guess = int(input("あなたの予想: "))
    attempts += 1
    
    if guess < number:
        print("もっと大きい数字です。")
    elif guess > number:
        print("もっと小さい数字です。")
    else:
        print(f"おめでとうございます！ {attempts} 回目で正解しました！")
        break
