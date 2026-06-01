# game.py (версия Маши)
import random

print("🎮 Добро пожаловать в игру 'Угадай число'!")

# МАША ДОБАВИЛА ВЫБОР СЛОЖНОСТИ:
print("Выбери сложность:")
print("1 - Легко (1-10)")
print("2 - Средне (1-50)")
print("3 - Сложно (1-100)")

choice = input("Твой выбор (1-3): ")
if choice == "1":
    max_num = 10
elif choice == "2":
    max_num = 50
else:
    max_num = 100

print(f"Я загадал число от 1 до {max_num}")

secret = random.randint(1, max_num)

while True:
    guess = int(input("Твоё предположение: "))
    
    if guess < secret:
        print("❌ Мало!")
    elif guess > secret:
        print("❌ Много!")
    else:
        print(f"✅ Угадал! Это было число {secret}")
        break