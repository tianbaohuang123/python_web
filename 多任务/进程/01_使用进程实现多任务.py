import time
import multiprocessing

def sing():
    """唱歌"""
    while True:
        print("---I'm singing---")
        time.sleep(1)

def dance():
    """跳舞"""
    while True:
        print("---I'm dancing---")
        time.sleep(1)

def main():
    p_sing = multiprocessing.Process(target=sing)
    p_dance = multiprocessing.Process(target=dance)

    p_sing.start()
    p_dance.start()

if __name__ == "__main__":
    main()