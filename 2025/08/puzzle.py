import functools
import math
import operator
import time
from linecache import cache
from typing import List, Dict, Optional
from xml.etree.ElementTree import tostring

with open('input.txt') as f:
    junction_boxes: List[tuple[int,int,int]] = [tuple(int(n) for n in x.split(",")) for x in f.read().splitlines()]

# print(junction_boxes)
junction_box_to_network_lookup: Dict[tuple[int, int, int], Optional[int]] = {}
network_to_junction_box: Dict[int, set[tuple[int, int, int]]] = {}

network_counter: int = 0

# add circuits to dict
start_time = time.time()

# print(f"time to build dict {time.time() - start_time} seconds")
# print(junction_box_to_network_lookup)

@functools.cache
def find_distance (a: tuple[int,int,int], b: tuple[int,int,int]) -> int:
    return math.sqrt(math.pow(abs(a[0] - b[0]), 2) + math.pow(abs(a[1] - b[1]), 2) + math.pow(abs(a[2] - b[2]), 2))

# def is_junction_boxes_in_same_network(a: tuple[int,int,int], b: tuple[int,int,int]) -> bool:
#     if a not in junction_box_to_network_lookup or b not in junction_box_to_network_lookup:
#         return False
#
#     return junction_box_to_network_lookup[a] == junction_box_to_network_lookup[b]
#
def join_network(a,b):
    if a == b:
        return

    network_b_junction_boxes = network_to_junction_box.pop(b)

    for junction_box in network_b_junction_boxes:
        junction_box_to_network_lookup[junction_box] = a
        network_to_junction_box[a].add(junction_box)
#
#
# # print(find_distance((162,817,812),(425,690,689)))
#
# for i in range(1000):
#     shortest_path:int = math.inf
#     nodes_for_shortest_path:List[tuple[int,int,int]] = []
#
#     for index_a, junction_box_a in enumerate(junction_boxes):
#         for junction_box_b in junction_boxes[index_a + 1:]:
#             if is_junction_boxes_in_same_network(junction_box_a, junction_box_b):
#                 continue
#
#             if find_distance(junction_box_a, junction_box_b) < shortest_path:
#                 shortest_path = find_distance(junction_box_a, junction_box_b)
#                 nodes_for_shortest_path = [junction_box_a, junction_box_b]
#
#     if not nodes_for_shortest_path:
#         break
#
#     network = network_counter
#     if nodes_for_shortest_path[0] in junction_box_to_network_lookup and nodes_for_shortest_path[1] in junction_box_to_network_lookup:
#         join_network(junction_box_to_network_lookup[nodes_for_shortest_path[0]],junction_box_to_network_lookup[nodes_for_shortest_path[1]])
#         break
#
#     elif nodes_for_shortest_path[0] in junction_box_to_network_lookup:
#         network = junction_box_to_network_lookup[nodes_for_shortest_path[0]]
#         junction_box_to_network_lookup[nodes_for_shortest_path[1]] = network
#         network_to_junction_box[network].append(junction_box_to_network_lookup[nodes_for_shortest_path[0]])
#     elif nodes_for_shortest_path[1] in junction_box_to_network_lookup:
#         network = junction_box_to_network_lookup[nodes_for_shortest_path[1]]
#         junction_box_to_network_lookup[nodes_for_shortest_path[0]] = network
#         network_to_junction_box[network].append(junction_box_to_network_lookup[nodes_for_shortest_path[1]])
#     else:
#         if network in network_to_junction_box:
#             network_to_junction_box[network].append(nodes_for_shortest_path[0])
#             network_to_junction_box[network].append(nodes_for_shortest_path[1])
#         else:
#             network_to_junction_box[network] = [*nodes_for_shortest_path]
#
#         for t in nodes_for_shortest_path:
#             junction_box_to_network_lookup[t] = network
#
#     network_counter += 1
#
# print(junction_box_to_network_lookup)
# print(network_to_junction_box)
# print(sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True)[:3])
# print(functools.reduce(operator.mul, sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True)[:3]))


class Path:
    distance: object
    connected_junction_boxes: list[tuple[int, int, int]]

    def __init__(self, connected_junction_boxes: List[tuple[int,int,int]]):
        self.connected_junction_boxes = connected_junction_boxes
        self.distance = find_distance(connected_junction_boxes[0], connected_junction_boxes[1])

    def __str__(self):
        return f"{self.connected_junction_boxes[0]},{self.connected_junction_boxes[1]},{self.distance}"


all_paths_between_junction_boxes: List[Path] = []

# start_time = time.time()
for index_a, junction_box_a in enumerate(junction_boxes):
    for junction_box_b in junction_boxes[index_a+1:]:
        all_paths_between_junction_boxes.append(Path((junction_box_a, junction_box_b)))

all_paths_between_junction_boxes.sort(key= lambda x: x.distance)

network_counter = 0
connection_counter = 0
last_two_nodes = None

for connection in all_paths_between_junction_boxes:
    connection_counter += 1
    network = network_counter
    connected_junction_box_a, connected_junction_box_b = connection.connected_junction_boxes


    if connection_counter == 1000:
        # print(sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True))
        # print(sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True)[:3])
        # print(functools.reduce(operator.mul,
        #                        sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True)[
        #                            :3]))
        print(f"part 1 {functools.reduce(operator.mul,
                               sorted([len(network_to_junction_box[l]) for l in network_to_junction_box], reverse=True)[
                                   :3])} {time.time() - start_time}")

    if len(network_to_junction_box) == 1 and len(network_to_junction_box[list(network_to_junction_box.keys())[0]]) == 1000:
        print(f"part 2 {last_two_nodes.connected_junction_boxes[0][0] * last_two_nodes.connected_junction_boxes[1][0]} {time.time() - start_time}")
        break
    else:
        last_two_nodes = connection

    if connected_junction_box_a not in junction_box_to_network_lookup and connected_junction_box_b not in junction_box_to_network_lookup:
        network_counter += 1
        network_to_junction_box[network] = set()
    elif connected_junction_box_a in junction_box_to_network_lookup and connected_junction_box_b not in junction_box_to_network_lookup:
        network = junction_box_to_network_lookup[connected_junction_box_a]
    elif connected_junction_box_a not in junction_box_to_network_lookup and connected_junction_box_b in junction_box_to_network_lookup:
        network = junction_box_to_network_lookup[connected_junction_box_b]
    elif junction_box_to_network_lookup[connected_junction_box_a] == junction_box_to_network_lookup[connected_junction_box_b]:
        continue
    else:
        join_network(junction_box_to_network_lookup[connected_junction_box_a], junction_box_to_network_lookup[connected_junction_box_b])
        continue

    junction_box_to_network_lookup[connected_junction_box_b] = network
    junction_box_to_network_lookup[connected_junction_box_a] = network
    network_to_junction_box[network].add(connected_junction_box_a)
    network_to_junction_box[network].add(connected_junction_box_b)
