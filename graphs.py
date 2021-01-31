# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:03:35 2021

@author: AndreaB.Rava
"""
import networkx as nx
from   networkx.generators.random_graphs import erdos_renyi_graph


def rand_graph (n_nodes, prob=0.5):
    """
    This method generate a random graph, with n_nodes and at least one edge

    Parameters
    ----------
    n_nodes : int
        number of nodes of the graph.
    prob : float, optional
        probability, that two edges are linked during the creation, must be in [0, 1].
        The default is 0.5.

    Returns
    -------
    graph : Returns a $G_{n,p}$ random graph, also known as an Erdős-Rényi graph or a binomial graph
        The $G_{n,p}$ model chooses each of the possible edges with probability $p$..

    """
    graph = erdos_renyi_graph(n_nodes, prob)
    while len(list(graph.edges)) < 1:
        graph = erdos_renyi_graph(n_nodes, prob)
    return graph