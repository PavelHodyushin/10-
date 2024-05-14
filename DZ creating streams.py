from time import sleep
from threading import Thread

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letter = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

def output_of_number(*args):
    for num in args:
        print(num)
        sleep(1)

def output_of_letters(*args):
    for let in args:
        print(let)
        sleep(1)


numbers1 = Thread(target=output_of_number, args=number)
letters1 = Thread(target=output_of_letters, args=letter)
numbers1.start()
letters1.start()
numbers1.join()
letters1.join()