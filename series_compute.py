"""
Betty Phipps
Date: 2025-09-24
Assignment: Parallel Series Computation with Ray
Due Date: 2025-09-28

About this project:
This program computes the partial sum of the alternating harmonic series:
    ∑ (-1)^(n+1) / n^2   , for n = 1 to 1000

Assumptions:
Series is known as the alternating series of reciprocal squares.
- This series was NOT used in lecture examples.
All work below was performed by Betty Phipps.
"""

import ray

ray.init(ignore_reinit_error=True) # Initialize Ray; this starts a local cluster for parallel computation

@ray.remote
def compute_chunk(start, end):
    """Compute sum of alternating harmonic series for the given range."""
    local_sum = 0.0
    for n in range(start, end + 1):
        # Alternating harmonic series formula: (-1)^(n+1) / n^2
        local_sum += ((-1) ** (n + 1)) / (n ** 2)
    return local_sum

def main():
    """
    Main function that divides the series computation into parallel chunks,
    collects partial sums from all chunks, and prints the total sum.
    """
    N = 1000
    num_chunks = 4
    chunk_size = N // num_chunks

    # List to hold future objects returned by Ray remote function calls
    futures = []

    for i in range(num_chunks):
        start = i * chunk_size + 1
        # Last chunk takes any remaining terms if N is not perfectly divisible
        end = (i + 1) * chunk_size if i < num_chunks - 1 else N
        futures.append(compute_chunk.remote(start, end))

    # Retrieve results from all parallel computations
    results = ray.get(futures)

    # Compute total sum by summing all partial sums
    total_sum = sum(results)

    print("\nAlternating Harmonic Series of Reciprocal Squares")
    print("Formula: ∑ (-1)^(n+1) / n^2 , n=1..1000")
    print(f"Total sum: {total_sum:.12f}")
    print("Partial sums from each chunk:")
    for i, r in enumerate(results, start=1):
        print(f"  Chunk {i}: {r:.12f} ({r:.3e})")  # Decimal and scientific notation


if __name__ == "__main__":
    main()
    ray.shutdown()
