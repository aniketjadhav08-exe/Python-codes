from multiprocessing import Pool

def SumOfSquares(n):
    return sum(i * i for i in range(1, n + 1))

def Main():
    List = [1000000, 2000000, 3000000, 4000000]

    with Pool(processes=4) as pool:
        Result = pool.map(SumOfSquares, List)

    print("Input list :", List)
    print("Sum of squares for each element :", Result)

if __name__ == "__main__":
    Main()
