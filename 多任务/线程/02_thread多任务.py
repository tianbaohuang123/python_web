import time
import threading

def sing():
    """唱歌 5s"""
    for i in range(5):
        print("---%d I'm singing---" % (i + 1))
        time.sleep(1)

def dance():
    """跳舞 5s"""
    for i in range(5):
        print("---%d I'm dancing---" % (i + 1))
        time.sleep(1)

def main():
    t_sing = threading.Thread(target=sing)
    t_dance = threading.Thread(target=dance)
    t_sing.start()
    t_dance.start()

if __name__ == "__main__":
    main()
