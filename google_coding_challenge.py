from collections import namedtuple
from datetime import datetime
from functools import wraps
import math
from random import random

print_blocks = False

"""
Coding challenge from Google / Clement Mihailescu. Find it here: https://www.youtube.com/watch?v=rw4s4M3hFfs
"""

### Generate random list of blocks
reqs = ['church', 'cinema', 'library', 'museum', 'park', 'school', 'supermarket'] ### For example
exists_p = 0.5 ### Probability that a given place exists in a given block
blocks = [{req: (True if random() <= exists_p else False) for req in reqs} for _ in range(1_000)]

if print_blocks:
    for i, block in enumerate(blocks):
        block_text = ' | '.join([f'{k}: {str(v).ljust(5)}' for k, v in block.items()])
        print(f'{str(i).ljust(2)}: {block_text}')

Solution = namedtuple('Solution', ['best_block_index', 'min_total_dist'])

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        result = func(*args, **kwargs)
        t2 = datetime.now()
        time_taken = (t2 - t1).microseconds
        print(f'Function {func.__name__} took {time_taken} microseconds')
        return result
    return wrapper

@timer
def solution_1(reqs, blocks):
    """
    Faster for smaller numbers
    """
    req_index_dict = {}
    for i, block in enumerate(blocks):
        for req in reqs:
            if block.get(req):
                if req in req_index_dict:
                    req_index_dict[req].append(i)
                else:
                    req_index_dict[req] = [i]
    best_block_index, min_total_dist = None, None
    for i, block in enumerate(blocks):
        req_dists = {}
        for req in reqs:
            if block.get(req):
                dist = 0
            else:
                indices = req_index_dict[req]
                dist = min(abs(i - index) for index in indices)
            req_dists[req] = dist
        total_dist = sum(req_dists.values())
        if i == 0 or total_dist < min_total_dist:
            best_block_index = i
            min_total_dist = total_dist
    return Solution(best_block_index, min_total_dist)

@timer
def solution_2(reqs, blocks):
    """
    Scales better but loses its edge as the chance of a place not appearing in a block increase
    """
    i = 1
    complete_block_groups = {}
    len_blocks, len_reqs = len(blocks), len(reqs) ### Prevent recalculation
    max_i = len_blocks
    while i < max_i:
        for j in range(len_blocks - i):
            block_group = blocks[j:i + j]
            if sum(any(block[req] for block in block_group) for req in reqs) == len_reqs:
                complete_block_groups[j] = block_group
        if complete_block_groups and max_i == len_blocks:
            num_rows, num_cols = i, len_reqs
            max_min_total_dist = (num_rows - 1) * math.floor(num_cols / 2)
            max_i = max_min_total_dist + 1 ### Limit the maximum block group size to avoid needless checks after the point at which it becomes mathematically impossible for a minimum total distance to arise that is lower than the one we have found
        i += 1
    if i == 1:
        return Solution(min(complete_block_groups.keys()), 0)
    else:
        complete_block_groups = dict(sorted(complete_block_groups.items()))
        for k, (index_offset, complete_block_group) in enumerate(complete_block_groups.items()):
            best_block_index, min_total_dist = solution_1.__wrapped__(reqs, complete_block_group) ### __wrapped__ gets the undecorated function
            if k == 0 or min_total_dist < min_min_total_dist:
                best_best_block_index = best_block_index + index_offset
                min_min_total_dist = min_total_dist
        return Solution(best_best_block_index, min_min_total_dist)

### Display results
# best_block_index_1, min_total_dist_1 = solution_1(reqs, blocks)
# print(f'Solution 1: the best block is at index {best_block_index_1} and has a total distance of {min_total_dist_1} to all requirements')
# best_block_index_2, min_total_dist_2 = solution_2(reqs, blocks)
# print(f'Solution 2: the best block is at index {best_block_index_2} and has a total distance of {min_total_dist_2} to all requirements')

for func in [solution_1, solution_2]:
    best_block_index, min_total_dist = func(reqs, blocks)
    print(f'{func.__name__}: the best block is at index {best_block_index} and has a total distance of {min_total_dist} to all requirements')