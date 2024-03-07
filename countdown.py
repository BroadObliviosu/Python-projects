import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"time remaining: {seconds} seconds")
        time.sleep(1) #delays each number for 1 second
        seconds -=1
    print("times up!")

def main():
    try:
        seconds = int(input("enter the countdown time in seconds --> "))
        countdown_timer(seconds)
    except ValueError:
        print("pleaase enter a valid number of seconds")
    

if __name__=="__main__":
        main()