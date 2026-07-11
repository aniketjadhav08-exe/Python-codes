from multiprocessing import Pool, current_process

def Factorial(n):
    Fact = 1
    for i in range(1, n + 1):
        Fact *= i
    return (current_process().pid, n, Fact)

def Main():
    List = [10, 15, 20, 25]

    with Pool(processes=4) as pool:
        Result = pool.map(Factorial, List)

    for pid, no, fact in Result:
        print("Process ID :", pid, " Input Number :", no, " Factorial :", fact)

if __name__ == "__main__":
    Main()