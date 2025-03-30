from greedy_alg import greedy_within_cycle, greedy_between_cycles
from random_walk_alg import random_walk
from steepest_alg import steepest_within_cycle_and_edges, steepest_between_cycles
from utils import load_from_tsp

if __name__ == "__main__":
    kroa200_matrix, kroa200_coords = load_from_tsp('datasets/kroA200.tsp')
    krob200_matrix, krob200_coords = load_from_tsp('datasets/kroB200.tsp')

    solution_intra, length_intra, time_intra = greedy_within_cycle(kroa200_matrix, randomize=True)
    print("\nGreedy search (node and edge swaps):")
    print(f"Best solution length: {length_intra}")
    print(f"Execution time: {time_intra:.4f} seconds")

    solution_inter, length_inter, time_inter = greedy_between_cycles(kroa200_matrix, randomize=True)
    print("\nGreedy search (node swap between cycles):")
    print(f"Best solution length: {length_inter}")
    print(f"Execution time: {time_inter:.4f} seconds")

    solution_steepest_within, length_steepest_within, time_steepest_within = steepest_within_cycle_and_edges(kroa200_matrix)
    print("\nSteepest local search (node and edge swaps within cycle):")
    print(f"Best solution length: {length_steepest_within}")
    print(f"Execution time: {time_steepest_within:.4f} seconds")

    solution_steepest_between, length_steepest_between, time_steepest_between = steepest_between_cycles(kroa200_matrix)
    print("\nSteepest local search (node swaps between cycles):")
    print(f"Best solution length: {length_steepest_between}")
    print(f"Execution time: {time_steepest_between:.4f} seconds")

    solution_random, length_random = random_walk(kroa200_matrix, 40)
    print("\nRandom walk search:")
    print(f"Best solution length: {length_random}")
    print(f"Execution time: 40 seconds")

    # Run algorithms on kroB200 dataset
    solution_intra_b, length_intra_b, time_intra_b = greedy_within_cycle(krob200_matrix, randomize=True)
    print("\nGreedy search (node and edge swaps) on kroB200:")
    print(f"Best solution length: {length_intra_b}")
    print(f"Execution time: {time_intra_b:.4f} seconds")

    solution_inter_b, length_inter_b, time_inter_b = greedy_between_cycles(krob200_matrix, randomize=True)
    print("\nGreedy search (node swap between cycles) on kroB200:")
    print(f"Best solution length: {length_inter_b}")
    print(f"Execution time: {time_inter_b:.4f} seconds")

    solution_steepest_within_b, length_steepest_within_b, time_steepest_within_b = steepest_within_cycle_and_edges(krob200_matrix)
    print("\nSteepest local search (node and edge swaps within cycle) on kroB200:")
    print(f"Best solution length: {length_steepest_within_b}")
    print(f"Execution time: {time_steepest_within_b:.4f} seconds")

    solution_steepest_between_b, length_steepest_between_b, time_steepest_between_b = steepest_between_cycles(krob200_matrix)
    print("\nSteepest local search (node swaps between cycles) on kroB200:")
    print(f"Best solution length: {length_steepest_between_b}")
    print(f"Execution time: {time_steepest_between_b:.4f} seconds")

    solution_random, length_random = random_walk(krob200_matrix, 40)
    print("\nRandom walk search on kroB200:")
    print(f"Best solution length: {length_random}")
    print(f"Execution time: 40 seconds")