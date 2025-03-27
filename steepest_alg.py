from swaps import swap_nodes_within_cycle, swap_edges_within_cycle, swap_nodes_between_cycles
from utils import load_from_tsp, initialize_random_cycles, cycle_length
import time

def steepest_within_cycle_and_edges(distance_matrix):
    start_time = time.time()
    first_cycle, second_cycle, nodes = initialize_random_cycles(distance_matrix)
    best_length = cycle_length(first_cycle, distance_matrix) + cycle_length(second_cycle, distance_matrix)

    improved = True
    while improved:
        improved = False
        best_delta = 0
        best_move = None

        # Przeglądanie ruchów w obrębie pierwszego cyklu (wymiana wierzchołków)
        for new_cycle, delta in swap_nodes_within_cycle(first_cycle, distance_matrix):
            if delta < best_delta:
                best_delta = delta
                best_move = ('first', new_cycle)

        # Przeglądanie ruchów w obrębie drugiego cyklu (wymiana wierzchołków)
        for new_cycle, delta in swap_nodes_within_cycle(second_cycle, distance_matrix):
            if delta < best_delta:
                best_delta = delta
                best_move = ('second', new_cycle)

        # Przeglądanie zamiany krawędzi w obrębie pierwszego cyklu (2-opt move)
        for new_cycle, delta in swap_edges_within_cycle(first_cycle, distance_matrix):
            if delta < best_delta:
                best_delta = delta
                best_move = ('first', new_cycle)

        # Przeglądanie zamiany krawędzi w obrębie drugiego cyklu (2-opt move)
        for new_cycle, delta in swap_edges_within_cycle(second_cycle, distance_matrix):
            if delta < best_delta:
                best_delta = delta
                best_move = ('second', new_cycle)

        if best_move is not None:
            if best_move[0] == 'first':
                first_cycle = best_move[1]
            elif best_move[0] == 'second':
                second_cycle = best_move[1]

            best_length += best_delta
            improved = True

    execution_time = time.time() - start_time
    return (first_cycle, second_cycle), best_length, execution_time


def steepest_between_cycles(distance_matrix):
    start_time = time.time()
    first_cycle, second_cycle, nodes = initialize_random_cycles(distance_matrix)
    best_length = cycle_length(first_cycle, distance_matrix) + cycle_length(second_cycle, distance_matrix)

    improved = True
    while improved:
        improved = False
        best_delta = 0
        best_move = None

        for new_first, new_second, delta in swap_nodes_between_cycles(first_cycle, second_cycle, distance_matrix):
            if delta < best_delta:
                best_delta = delta
                best_move = ('both', new_first, new_second)

        if best_move is not None:
            first_cycle, second_cycle = best_move[1], best_move[2]
            best_length += best_delta
            improved = True

    execution_time = time.time() - start_time
    return (first_cycle, second_cycle), best_length, execution_time