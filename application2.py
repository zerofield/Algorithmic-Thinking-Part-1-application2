import alg_application2_provided as provided
import my_graph_helper as helper
import random
import alg_upa_trial as upa_helper
#provided.load_graph_local('computer_network.txt')


def UER(num_nodes, probability):
	if(num_nodes <= 0 ):
		return dict()
	graph = dict()

	for node in range(num_nodes):
		nodes = range(num_nodes)
		nodes.remove(node)
		graph[node] = set(nodes)

    #it's complete graph now
	
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

#test
#print UER(5, 0.5)
print UPA(10, 5)