import alg_application2_provided as provided
import my_graph_helper as helper
import alg_upa_trial as upa_helper
import random
import math
import project2
import matplotlib.pyplot as plt

NODE_COUNT = 1239
EDGE_COUNT = 3047

def num_of_edges(graph):
	'''
	Calculate number of edges
	'''
	edge_counter = 0

	for node in graph:

		connected_nodes = graph[node]

		for connected_node in connected_nodes:

			if connected_node > node:
				edge_counter += 1


	return edge_counter

def UER(num_nodes, probability):
	if(num_nodes <= 0 ):
		return dict()
	graph = dict()

	for node in range(num_nodes):
		nodes = range(num_nodes)
		nodes.remove(node)
		graph[node] = set(nodes)

    #it's complete graph for now
	
	for node in range(num_nodes - 1):
		for inner_node in range(node + 1, num_nodes):
			rand = random.random()
			if rand > probability:
				#remove edge
				graph[node].remove(inner_node)
				graph[inner_node].remove(node)

	return graph 

def UPA(n, m):
	graph = helper.make_complete_graph(m)

	V = set(range(m))
	trial = upa_helper.UPATrial(m)
	for i in range(m, n):
		temp_V = trial.run_trial(m)
		V.add(i)
		graph[i] = temp_V
		
		for node in temp_V:
			graph[node].add(i)



	return graph

def determine_p():
	'''
	determine the probability p such that the ER graph 
	computed using this edge probability has approximately
	 the same number of edges as the computer network
	'''
	probability = 0
	amount = 0.0001
	target_edges = EDGE_COUNT

	closest = (0, 0)

	while True:

		graph = UER(NODE_COUNT, probability)
		edge_count = num_of_edges(graph)

		if edge_count < target_edges:
			closest = (probability, edge_count)
		else:
			break

		probability += amount

	print 'probability', probability

def determine_m():
	'''
	determine the number of edges in the UPA graph is
	close to the number of edges in the computer network
	'''

	m = 0
	amount = 0.0001
	target_edges = EDGE_COUNT
	closest = (0, 0)

	while True:

		graph = UPA(NODE_COUNT, m)
		edge_count = num_of_edges(graph)

		if edge_count < target_edges:
			closest = (m, edge_count)
		else:
			break

		m += 1

	print 'm', m

def random_order(graph):
	result_list = list(graph.keys())
	random.shuffle(result_list)
	return result_list



def q1():
	#network graph
	nework_graph = provided.load_graph_local('computer_network.txt')
	order_list1 = random_order(nework_graph)
	resilience1 = project2.compute_resilience(nework_graph, order_list1)
	print 'finish graph1'
	#uer graph
	uer_graph = UER(NODE_COUNT, 0.003999)
	order_list2 = random_order(uer_graph)
	resilience2 = project2.compute_resilience(uer_graph, order_list2)
	print 'finish graph2'
	#upa graph
	upa_graph = UPA(NODE_COUNT, 3)
	order_list3 = random_order(upa_graph)
	resilience3 = project2.compute_resilience(upa_graph, order_list3)
	print 'finish graph3'
	
	#plt.xlabel('degree')
 	#plt.ylabel('distribution')
	plt.plot(resilience1,'b') 
	plt.plot(resilience2,'g') 
	plt.plot(resilience3,'r') 
	plt.show()

def fast_targeted_order(ugraph):
	pass

	
#test cases
#print UER(5, 0.5)
#print UPA(10, 5)
#determine_p() p = 0.003999
#determine_m() m = 3
#q1()