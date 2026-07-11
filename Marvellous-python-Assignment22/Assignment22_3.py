from multiprocessing import Pool

def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False
    return True

def CountPrimes(n):
    Count = 0
    for i in range(1, n + 1):
        if ChkPrime(i):
            Count += 1
    return Count

def Main():
    List = [10000, 20000, 30000, 40000]

    with Pool(processes=4) as pool:
        Result = pool.map(CountPrimes, List)

    for no, count in zip(List, Result):
        print("N =", no, " Prime count =", count)

if __name__ == "__main__":
    Main()