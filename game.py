import random
print("🎮 Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 10")

secret = random.randint(1, 10)

while True:
    guess = int(input("Твоё предположение: "))
    #Файл для Димы!!!
    if guess < secret:
        print("❌ Мало!")
    elif guess > secret:
        print("❌ Много!")
    else:
        print(f"✅ Угадал! Это было число {secret}")
        break