import pyautogui as auto
from time import sleep

print("Это начальный код от Ромы, он позволит тебе спамить в тг сообщениями. Один минус - писать сообщения нужно строго на английском, ведь иначе ничего отправляться не будет")
text = str(input("Текст который ты хочешь вводить:  "))
delay = int(input("Задержка между сообщениями (Секунды. Пример: 0.1)"))
messages = int(input("Сколько сообщений нужно отправить? (Не ограничено)"))
print ("Осталось 10 секунд до спама")
# Здесь задержка в СЕКУНДАХ
sleep(10)
print("Спам запущен")
for i in range (messages):
    auto.write(text)
    auto.press("enter")
    sleep(delay)

print ("Спам окончен")

#на случай если пригодится бесконечный поток сообщений
#while True:
#    auto.write(text)
#    auto.press("enter")
#    # Здесь задержка между отправкой
#    sleep(delay)
