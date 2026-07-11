from multiprocessing import Pool, current_process

def Factorial(n):
    Fact = 1
    for i in range(1, n + 1):
        Fact *= i
    return (current_process().pid, n, Fact)

def Main():
    Data = [10, 15, 20, 25]

    with Pool(processes=4) as pool:
        Result = pool.map(Factorial, Data)

    for pid, no, fact in Result:
        print("Process ID :", pid)
        print("Input Number :", no)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    Main()