import multiprocessing

def compute():
    print("Running in a separate process")

if __name__ == '__main__':
    p = multiprocessing.Process(target=compute)
    p.start()
    p.join()
