import sys
import time

def info(name, number):
    print("[Y]: Hi?")
    time.sleep(1)
    print("[!]: Who are you?")
    time.sleep(1)
    print("[Y]: My name is ", name)
    time.sleep(1)
    print("[Y]: I got a new phone number, it's ", number)
    time.sleep(1)
    print("[!]: I think you dialled the wrong number...")
    print("[Y]: Is this not Jason?")
    time.sleep(1)
    print("[!]: No, my name is Brian")
    time.sleep(1)
    print("[Y]: I'm sorry, have a nice day!")
    time.sleep(1)
    print("[!!!]: beep beep beep beep")

info(sys.argv[1], sys.argv[2])