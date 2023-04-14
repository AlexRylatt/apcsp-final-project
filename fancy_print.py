import time
def f_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.025)
    print("")