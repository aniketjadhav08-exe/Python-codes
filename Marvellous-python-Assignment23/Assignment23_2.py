from multiprocessing import Pool, current_process

def SumOfOdd(n):
    Total = sum(i for i in range(1, n + 1, 2))
    return (current_process().pid, n, Total)

def Main():
    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool(processes=4) as pool:
        Result = pool.map(SumOfOdd, Data)

    for pid, no, total in Result:
        print("Process ID :", pid)
        print("Input Number :", no)
        print("Sum of Odd Numbers :", total)
        print()

if __name__ == "__main__":
    Main()