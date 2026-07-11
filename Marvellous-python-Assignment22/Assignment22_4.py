from multiprocessing import Pool
import time

def SumOfFifthPowers(n):
    return sum(i ** 5 for i in range(1, n + 1))

def Main():
    List = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.time()

    with Pool(processes=4) as pool:
        Result = pool.map(SumOfFifthPowers, List)

    EndTime = time.time()

    for no, res in zip(List, Result):
        print("N =", no, " Sum of fifth powers =", res)

    print("Total execution time :", EndTime - StartTime, "seconds")

if __name__ == "__main__":
    Main()