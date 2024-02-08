import pandas as pd
import numpy as np
import multiprocessing

def square_worker(chunk):
    x='2'
    return chunk.apply(lambda x: x*2, axis=1)

def parallel_square(data, num_processes):
    pool = multiprocessing.Pool(processes=num_processes)
    data_chunks = np.array_split(data, num_processes)
    results = pool.map(square_worker, data_chunks)
    pool.close()
    pool.join()
    return pd.concat(results)

if  __name__ == "__main__":
    # Example CSV file
    csv_file_path = 'day.csv'

    # Read CSV into a DataFrame
    df = pd.read_csv("day.csv")

    # Number of processes to use
    num_processes = 4

    # Perform parallel computations
    result = parallel_square(df, num_processes)

    print(result)
