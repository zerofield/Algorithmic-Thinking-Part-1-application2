'''
Project 2
'''
from collections import deque

def bfs_visited(ugraph, start_node):
    '''
    bfs_visited
    '''
    visited = set([])
    visited.add(start_node)
    
    node_queue = deque()
    node_queue.append(start_node)
    
    while len(node_queue) > 0:
    	node = node_queue.popleft()

        if ugraph[node] == None: 
            continue

    	for neighbor in ugraph[node]:
    		if neighbor not in visited:
    			visited.add(neighbor)
    			node_queue.append(neighbor)
    
    return visited

def cc_visited(ugraph):
    '''
    cc_visited
    '''
    connected_components = list()
    remaining_nodes = list(ugraph.keys())

    while len(remaining_nodes) > 0:

        node = remaining_nodes[0]
        component = bfs_visited(ugraph, node)
        connected_components.append(component)

        for dummy_node in component:
            remaining_nodes.remove(dummy_node)


    return connected_components

def largest_cc_size(ugraph):
    '''
    largest_cc_size
    '''
    max_size = 0

    components = cc_visited(ugraph)

    for component in components:

        if len(component) > max_size:
            max_size = len(component)
            #print component

    return max_size

def compute_resilience(ugraph, attack_order):
    '''
    compute_resilience
    '''
    size = largest_cc_size(ugraph)

    size_list = [size]

    for node in attack_order:

        del ugraph[node]

        for node_in_graph in ugraph.keys():
            connected_list =ugraph[node_in_graph]
            if connected_list != None and node in connected_list:
                connected_list.remove(node)
        
        size = largest_cc_size(ugraph)
        size_list.append(size)

    return size_list
