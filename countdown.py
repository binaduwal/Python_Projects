import time

def countdown(second):
    while(second):
        min,sec=divmod(second,60)
        time_format="{:2d}:{:2d}".format(min,sec)
        print(time_format)
        time.sleep(1)
        second=second-1
    print("Time's up.")

value=int(input("Enter number in second:"))
countdown(value)
