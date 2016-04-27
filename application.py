import alg_load_graph as loader
import my_graph_helper as helper
import matplotlib.pyplot as plt
import random
import time


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the 	 ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    
    




def normalize(degree_distribution):

	count = 0
	for key in degree_distribution.iterkeys():
		count += degree_distribution[key]
	
	normalized_dict = dict()

	for key in degree_distribution.iterkeys():
		normalized_dict[key] = 1.0 * degree_distribution[key] / count
			
	return normalized_dict

def q1():
	citation_graph = loader.load_graph(loader.CITATION_URL)
	#citation_graph = helper.EX_GRAPH1

	print 'start calculating degree distribution'
	degree_distribution = helper.in_degree_distribution(citation_graph)
	print 'finish calculating degree distribution'

	print 'start normalizing'
	degree_distribution = normalize(degree_distribution)
	print 'finish normalizing'

	print degree_distribution

	print 'start plotting'
	plt.yscale('log')
	plt.xscale('log')
 	plt.xlabel('degree')
 	plt.ylabel('distribution')
	plt.plot(degree_distribution.keys(), degree_distribution.values(),'ro') 
	plt.show()


def ER(num, probability):
	graph = dict()
	for node in range(num):
		in_degree_list = list()

		for innder_node in range(num):
			if node == innder_node: 
				continue
			rand = random.random()
			 
			if rand < probability:
				in_degree_list.append(innder_node)		
		graph[node] = set(in_degree_list)
	return graph

def DPA(n, m):
	graph = helper.make_complete_graph(m)

	V = set(range(m))
	trial = DPATrial(m)
	for i in range(m, n):
		
		#toindeg = sum_of_indegree(graph)
		#temp_V = set([])
		#for times in range(m):
		#	for j in V:
		#		probability = 1.0*(len(graph[j]) +1)/(toindeg + len(V))
		#		rand = random.random()
		#		if rand < probability:
		#			temp_V.add(j)

		temp_V = trial.run_trial(m)

		
		V.add(i)
		graph[i] = temp_V

	return graph


def q2():
	 
	graph = ER(1000, 0.5)
	#print graph

	degree_distribution = helper.in_degree_distribution(graph)
	degree_distribution = normalize(degree_distribution)
	#print degree_distribution
	#plt.yscale('log')
	#plt.xscale('log') 
	#print degree_distribution
	plt.plot(degree_distribution.keys(), degree_distribution.values(),'ro') 
	plt.show()

def sum_of_indegree(graph):

	count = 0

	for val in graph.values():
		count += len(val)


	return count

def average_out_degree(graph):

	sum = 0

	for val in graph.values():
		sum += len(val)

	return sum / len(graph)

def q3():
 	
	citation_graph = loader.load_graph(loader.CITATION_URL)
	n = len(citation_graph)
	m = average_out_degree(citation_graph)
	print n, m

	

	 


def q4():

	#citation_graph = loader.load_graph(loader.CITATION_URL)
	#n = len(citation_graph)
	#m = average_out_degree(citation_graph)

	n = 27700 
	m = 12

	the_time = time.time()

	print 'start dpa'
	graph = DPA(n, m)
	print 'finish dpa ', (time.time() - the_time)
	the_time = time.time()

	print 'start in degree distribution'
	degree_distribution = helper.in_degree_distribution(graph)
	print 'finish in degree distribution', (time.time() - the_time)
	the_time = time.time()

	print 'start normalize'
	degree_distribution = normalize(degree_distribution)
	print 'finish normalize', (time.time() - the_time)
	the_time = time.time()

	plt.yscale('log')
	plt.xscale('log') 
	plt.plot(degree_distribution.keys(), degree_distribution.values(),'ro') 
	plt.show()

	 
 