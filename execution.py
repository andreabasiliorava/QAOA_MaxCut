# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:09:06 2021

@author: AndreaB.Rava
"""

import configparser
import sys
from pathlib import Path
import qutip as qu
import qaoa
import qucompsys as qucs
import numpy as np
import networkx as nx

#main part of the code

#STEP 1: take information of the graph

#take information from a file
Path("prob_dist").mkdir(parents=True, exist_ok=True)
config = configparser.ConfigParser()
config.read(sys.argv[1])
str_graph = sys.argv[2]
str_N_NODES = config.get(str_graph, 'n_nodes')
str_edges = config.get(str_graph, 'edges')
N_NODES = int(str_N_NODES)
N_QUBITS = N_NODES
nodes = np.arange(0, N_NODES, 1)
edges = []
for edge in str_edges.split(';'):
    edges.append((int(edge[1]),int(edge[3])))
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

destination1 = config.get('paths',f"my_prob_dist_{str_graph}")


#STEP 2: find optimal parameters

# Grid search for the maximizing variables
optimal_gamma, optimal_beta = qaoa.grid_search(qaoa.analitical_f_1, (graph, edges))


#STEP 3: obtain final state with solutions

# initial state (as density matrix):
init_state = qaoa.initial_state(N_QUBITS)
dm_init_state = qu.ket2dm(init_state)

# obtain final state (as density matrix)
fin_state = qaoa.evolution_operator(N_QUBITS, edges, [optimal_gamma], [optimal_beta])*init_state
dm_fin_state = qu.ket2dm(fin_state)

#probability distributions of configurations in final state
prob_dist_fin_state = qucs.comp_basis_prob_dist(fin_state)

np.save(destination1, prob_dist_fin_state)
