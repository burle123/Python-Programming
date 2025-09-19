import multiprocessing

def worker_function(name):
    print(f"Worker {name} is running.")

def square(x):
    return x * x

if __name__ == "__main__":
    # Example 1: Using Process
    process = multiprocessing.Process(target=worker_function, args=("1",))
    process.start()
    process.join()  # Wait for the process to complete

    # Example 2: Using Pool
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)  # Output: [1, 4, 9, 16, 25]
