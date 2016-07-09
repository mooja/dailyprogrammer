#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#              Challenge 37 Easy - Dijkstra's Algorithm               #
#######################################################################

class Node(object):
    def __init__(self, name, links=[]):
        self.name = name
        self.links = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Graph(object):
    def __init__(self, name, nodes, links):
        self.name = name
        self.nodes = nodes
        self.links = links

        for n1, n2, distance in links:
            n1.links.append((n2, distance))
            n2.links.append((n1, distance))


def find_shortest_path(start_node, dest_node, graph):
    current_node = start_node
    unvisited_nodes = graph.nodes
    for n in unvisited_nodes:
        n.tentative_distance = -1
    current_node.tentative_distance = 0


