'''
graph
'''
EX_GRAPH0 = {0 : set([1, 2]), 1 : set([]), 2 : set([])}
EX_GRAPH1 = {0:set([1, 4, 5]), 1:set([2, 6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0 : set([1,4,5]),1 : set([2,6]),2 : set([3,7]),3 : set([7]),4 : set([1]),5 : set([2]),6 : set([]),7 : set([3]),8 : set([1,2]),9 : set([0,3,4,5,6,7]),}

def make_complete_graph(num_nodes):

     '''
     make_complete_graph
     '''
     if(num_nodes <= 0 ):
          return dict()

     graph = dict()

     for node in range(num_nodes):
          nodes = range(num_nodes)
          nodes.remove(node)
          graph[node] = set(nodes)

     return graph


def compute_in_degrees(digraph):
     '''
     compute_in_degrees
     '''
     degree_dict = dict()

     for current_node in digraph.iterkeys():
          degree_dict[current_node] = 0

          for inner_node in digraph.iterkeys():

               if current_node == inner_node:
                    continue


               if current_node in digraph[inner_node]:
                    degree_dict[current_node] += 1   

     return degree_dict

def in_degree_distribution(digraph):
     '''
     in_degree_distribution
     '''
     degree_dict = dict()
     in_degree_dict = compute_in_degrees(digraph)

     node_count = len(in_degree_dict)

     for the_pk in range(node_count):

          count = 0

          for node in in_degree_dict.iterkeys():

               if in_degree_dict[node] == the_pk:
                    count += 1
          if count > 0:
               degree_dict[the_pk] =  count

     return degree_dict


