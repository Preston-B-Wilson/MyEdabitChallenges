import numpy as np

def is_adjacent(matrix, node1, node2):
	iniMatrix = np.array(matrix)
	return iniMatrix[node1, node2]

