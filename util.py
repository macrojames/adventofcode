import os
from queue import PriorityQueue
import sys


def open_input(day, sample_mode):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ext = '.sample' if sample_mode else '.input'
    return open(os.path.join(dir_path, 'inputs', f"{day}{ext}"))


def read_input_lines(day, sample_mode):
    return [_.strip() for _ in open_input(day, sample_mode).readlines()]


def read_input_raw(day, sample_mode):
    return open_input(day, sample_mode).read()


def arr2d_get_near_idx(arr2d: list[list], y: int, x: int) -> list[tuple]:
    # Return neighbor indexes
    nt = []
    if x >= 1:
        nt.append((y, x-1))
    if x + 1 < len(arr2d[y]):
        nt.append((y, x+1))
    if y >= 1:
        nt.append((y-1, x))
    if y + 1 < len(arr2d):
        nt.append((y+1, x))
    return nt


def arr2d_get_neighbors(arr2d: list[list], y: int, x: int):
    # Return neighbor values
    return [arr2d[y][x] for y, x in arr2d_get_near_idx(arr2d, x, y)]


def arr2d_get_idx(arr2d: list[list], value: any) -> tuple:
    """ Returns first occurence coordinates of value in arr2d
        Raises ValueError if no match is found
    """
    for y, row in enumerate(arr2d):
        if value in row:
            return y, row.index(value)
    raise ValueError


def arr2d_get_all_idx(arr2d: list[list], value: any) -> list[tuple]:
    """ Returns all occurence coordinates of value in arr2d
        Raises ValueError if no match is found
    """
    ret = []
    for y, row in enumerate(arr2d):
        if value in row:
            ret.append((y, row.index(value)))
    if not ret:
        raise ValueError
    return ret


def dijkstra(grid, start, end, get_cost):
    nodes_open = PriorityQueue()
    nodes_open.put((0, start))
    dist = {start: 0}
    previous = {}
    visited = set()

    while nodes_open:
        while not nodes_open.empty():
            _, node = nodes_open.get()
            if node not in visited:
                break
        else:
            break
        visited.add(node)
        if node == end:
            break
        check_neighbors = [_ for _ in arr2d_get_near_idx(grid, *node) if _ not in visited]
        for neighbor in check_neighbors:
            new_dist = dist.get(node) + get_cost(grid[node[0]][node[1]], grid[neighbor[0]][neighbor[1]])
            if new_dist == float('inf'):    # Abbruchmöglichkeit durch cost implementierung
                next
            if new_dist < dist.get(neighbor, float('inf')):
                nodes_open.put((new_dist, neighbor))
                dist[neighbor] = new_dist
                previous[neighbor] = node
                
    return dist, previous
