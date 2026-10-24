from queue import Queue
import random
import string
import time

queue = Queue()

def generate_request():
    random_request = ('номер: ' + random.choice(string.ascii_letters) + str(random.randint(1, 10000)),)
    queue.put(random_request)
    print(f"\nПроводиться додавання нової заявки, будь ласка, зачекайте...")
    fake_process_requestss(0.04)
    print(f"\nВаша заявка {random_request[0]} додана до черги")
    print("-" * len("\nПроводиться додавання нової заявки, будь ласка, зачекайте..."))

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"\nПроводиться обробка заявки {request[0]}, будь ласка, зачекайте...")
        fake_process_requestss(0.06)
        print(f"\nЗаявка {request[0]} успішно оброблена!")
        print("-" * len("\nПроводиться обробка заявки {request[0]}, будь ласка, зачекайте..."))
    else:
        print("\nЧерга пуста, немає заявок для обробки.")
        print("-" * len("\nЧерга пуста, немає заявок для обробки."))

def fake_process_requestss(delay):     
    for i in range(10, 101, 1):              
            text = ".."* (i // 10)  
            print(f"\r{i}% {text}", end="", flush=True)  
            time.sleep(delay)

# Головний цикл програми:
while True:
    user_input = input("\nДля створення нової заявки натисніть - g  \nдля обробки заявки натисніть - p \nдля виходу натисніть - q\n")
    print("-" * len("\nДля створення нової заявки натисніть - g"))
    if user_input.lower() == 'g':
        generate_request()
    elif user_input.lower() == 'p':
        process_request()
    elif user_input.lower() == 'q':
        print("Вихід з програми.")
        break
    else:
        print("Невірна команда. Спробуйте ще раз.")
    