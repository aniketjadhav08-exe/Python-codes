from multiprocessing import Pool, current_process

def EvenCount(n):
    Count = len(range(2, n + 1, 2))
    return (current_process().pid, n, Count)

def Main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool(processes=4) as pool:
        Result = pool.map(EvenCount, Data)

    for pid, no, count in Result:
        print("Process ID :", pid)
        print("Input Number :", no)
        print("Even Number Count :", count)
        print()

if __name__ == "__main__":
    Main()