"""implementation of a directed weighted graph object"""

import numpy as np

from tree.binary_tree import AVLTree
from collections import OrderedDict, deque

class AdjacencySet(AVLTree):
    def __init__(self):
        AVLTree.__init__(self)

    def inOrder(self):
        return [element.value for element in AVLTree.inOrder(self)]

    def __iter__(self):
        items = self.inOrder()
        for i,item in enumerate(items):
            yield item

class Node(object):
    def __init__(self,index,value=None):
        self.index         = index
        self.value         = value
        self.adjacency_set = AdjacencySet()

    def connect(self,newNode,weight=None):
        self.adjacency_set.insert(newNode.index,(newNode,weight))

    def weight(self,index):
        try:
            s = self.adjacency_set.search(index)
            return s.value[1]
        except KeyError:
            return None

    def __repr__(self):
        return "Graph Node {}".format(self.index)

class DirectedGraph(object):
    def __init__(self,init_size):
        self.nodes         = OrderedDict([(i,Node(i)) for i in xrange(init_size)])
        self.N             = len(self.nodes)

    def connect(self,i,j,weight=1.):
        if weight < 0.:
            raise ValueError('weights must be non-negative')
        self.nodes[i].connect(self.nodes[j],weight)

    def weight(self,i,j):
        return self.nodes[i].weight(j)

    def BFS(self,s):
        explored = set()
        queue    = deque([s])
        while queue:
            current = queue.pop()
            if current not in explored:
                explored.add(current)
                for child in current.adjacency_set:
                    queue.appendleft(child)
        return explored

    def DFS(self,s):
        explored = set()
        stack    = []
        while queue:
            current = stack.pop()
            if current not in explored:
                explored.add(current)
                for child in current.adjacency_set:
                    stack.append(child)
        return explored

    def Dijsktras(self,s):
        S           = OrderedDict([(s,(0.,None))])
        done        = False
        while not done:
            done    = True
            dist    = np.inf
            prev    = None
            closest = None
            for i, (d,_) in S.items():
                for o, w in self.nodes[i].adjacency_set:
                    if o.index in S:
                        continue
                    if d+w < dist:
                        dist    = d+w
                        prev    = i
                        closest = o.index
            if closest:
                done       = False
                S[closest] = (dist,prev)
        return S

    def relax(self,v,dist):
        m = min([float("infinity") if self.weight(v,w) is  None else dist[w] + self.weight(v,w) for w in dist])
        return min(dist[v],m)

    def Bellman_Ford(self,s,t):
        dist           = [None for i in xrange(self.N-1)]
        dist[0]        = OrderedDict([(v,float("infinity")) for v in self.nodes])
        dist[0][t]     = 0.
        for i in xrange(1,self.N-1):
            dist[i]    = OrderedDict([(v,float("infinity")) for v in self.nodes])
            dist[i][t] = 0.
            for v in self.nodes:
                dist[i][v] = self.relax(v,dist[i-1])
        return dist

if __name__=='__main__':
    G = DirectedGraph(20)
    for n in G.nodes:
        for m in G.nodes:
            if m != n:
                G.connect(n,m,np.random.rand())
    p = G.Bellman_Ford(2,6)
    print p[-1]