# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."

    graf=WeightedDigraph()
    f=open(mapFilename,'r')
    for line in f:
        strs=line.split()
        nn=[None,None]
        for i in range(2):

            if graf.hasNode2(strs[i]):
                nn[i]=graf.retNode(strs[i])
            else:
                nn[i]=Node(strs[i])
                graf.addNode(nn[i])



        edge=WeightedEdge(nn[0],nn[1],float(strs[2]),float(strs[3]))


        graf.addEdge(edge)
    return graf




#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

# Paste your code for both WeightedEdge and WeightedDigraph in this box.
# You may assume the grader has provided implementations for Node, Edge, and Digraph.
class WeightedEdge(Edge):
    def __init__(self,src,dest,tDist,oDist):
        Edge.__init__(self,src,dest)
        self.tDist=tDist
        self.oDist=oDist

    def getTotalDistance(self):
        return self.tDist

    def getOutdoorDistance(self):
        return self.oDist
    def __str__(self):
        return '{0}->{1}  ({2}, {3})'.format(self.src, self.dest,self.tDist,self.oDist)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]
class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest,(edge.getTotalDistance(),edge.getOutdoorDistance())])

    def childrenOf(self, node):
        return [nn[0] for nn in self.edges[node]]
    def hasNode(self, node):

        return node in self.nodes

    def hasNode2(self, snode):
        ans=False
        for n in self.nodes:
            ans=ans or (n.name==snode)
        return ans
    def retNode(self, snode):
        for n in self.nodes:
            if n.name==snode: return(n)

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0],float(d[1][0])
                ,float(d[1][1]))
        return res[:-1]
# Additionally paste your code for bruteForceSearch, and any helper functions, in this box.

def DFS2(graph, start, end, q = []):
    ans=[]
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[-1]
##        print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end:
            ans.append(tmpPath)
            continue
        qt=[]
        for linkNode in graph.childrenOf(lastNode):
            if linkNode not in tmpPath:
                newPath = tmpPath + [linkNode]
                qt.append(newPath)
##        q[:0]=qt
        q.extend(qt)

    return ans



##def testSP(st,end):
##    mitMap = load_map("mit_map.txt")
##
##    ssp = DFS2(mitMap, mitMap.retNode(str(st)), mitMap.retNode(str(end)))
##    for ind,sp in enumerate(ssp):
##        print '#{} path found by DFS:'.format(ind), printPath(sp)

def getdis(digraph, path):
    edges=digraph.edges
    ts=[0,0]
    for start,end in zip(path[0:-1],path[1:]):
##        print start,end,
        for edge in edges[start]:
            if edge[0]==end:
                ts[0]=ts[0]+float(edge[1][0])
                ts[1]+=float(edge[1][1])
##    print ts
    return ts

def memoize(f):
    def memf(*x):
        y=(tuple(i) for i in x)

        if y not in memf.cache:
            memf.cache[y]=f(*x)
        return memf.cache[y]
    memf.cache = {}
    return memf



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """

    #TODO
    ssp = DFS2(digraph, digraph.retNode(str(start)), digraph.retNode(str(end)))
    pl=[]
    for sp in ssp:

        tdist=getdis(digraph, sp)
        if (tdist[0]<maxTotalDist and tdist[1]<maxDistOutdoors):
            pl.append([sp,tdist[0]])
    if pl==[]:
        raise ValueError
    minl=pl[0]
    for ll in pl:
        if ll[1]<minl[1]: minl=ll
    ans2=[str(ii) for ii in minl[0]]
    return ans2

def DFS3(graph, start, end,maxtot,maxout):
    ans=None
    shortest=maxtot+1
    initPath = [start]
    q=[]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[-1]
##        print 'Current dequeued path:', (tmpPath[-1]),len(q)
        dist=getdis(graph,tmpPath)
        if (lastNode == end) :
##            print dist, shortest
            if  (dist[0]<shortest):
                ans=tmpPath
                shortest=dist[0]
            continue
        qt=[]
        for linkNode in graph.childrenOf(lastNode):
            dist=getdis(graph,(tmpPath + [linkNode]))
            if (linkNode not in tmpPath) and (dist[0]<=maxtot) and (dist[1]<=maxout):
                newPath = tmpPath + [linkNode]
                qt.append(newPath)
        q[:0]=qt

    return ans

def BFS3(graph, start, end,maxtot,maxout):
    ans=None
    shortest=maxtot+1
    initPath = [start]
    q=[]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[-1]
##        print 'Current dequeued path:', (tmpPath[-1]),len(q)
        dist=getdis(graph,tmpPath)
        if (lastNode == end) :
##            print dist, shortest
            if  (dist[0]<shortest):
                ans=tmpPath
                shortest=dist[0]
            continue
        qt=[]
        for linkNode in graph.childrenOf(lastNode):
            dist=getdis(graph,(tmpPath + [linkNode]))
            if (linkNode not in tmpPath) and (dist[0]<=maxtot) and (dist[1]<=maxout):
                newPath = tmpPath + [linkNode]
                qt.append(newPath)
        q.extend(qt)

    return ans
def DFS4(graph, start, end,maxtot,maxout):
    q=[]
    ans=[]
    initPath = [start]
    q.append(initPath)
    shortest=maxtot
    index=0
    while len(q) != 0:
        index+=1
        tmpPath = q.pop(0)
        lastNode = tmpPath[-1]
##        print 'Current dequeued path:', (tmpPath[-1]),index
        dist=getdis(graph,tmpPath)
        if (lastNode == end) :
##            print dist, shortest
            if  (dist[0]<shortest):
                ans.append(tmpPath)
                shortest=dist[0]
            continue
        qt=[]
        for linkNode in graph.childrenOf(lastNode):
            dist=getdis(graph,(tmpPath + [linkNode]))
            if (linkNode not in tmpPath) and (dist[0]<=maxtot) and (dist[1]<=maxout):
                newPath = tmpPath + [linkNode]
                qt.append(newPath)
        q[:0]=qt

    return ans

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
##    ssp = DFS4(digraph, digraph.retNode(str(start)), digraph.retNode(str(end)),
##      maxTotalDist, maxDistOutdoors)
##    pl=[]
##    for sp in ssp:
##
##        tdist=getdis(digraph, sp)
##        if (tdist[0]<maxTotalDist and tdist[1]<maxDistOutdoors):
##            pl.append([sp,tdist[0]])
##    if pl==[]:
##        raise ValueError
##    minl=pl[0]
##    for ll in pl:
##        if ll[1]<minl[1]: minl=ll
##    ans2=[str(ii) for ii in minl[0]]
##    return ans2
    sp = BFS3(digraph, digraph.retNode(str(start)), digraph.retNode(str(end))
    ,maxTotalDist,maxDistOutdoors)


    if sp==None:
        raise ValueError


    ans2=[str(ii) for ii in sp]
    return ans2
    pass
# Uncomment below when ready to test
## NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
##     Test cases
     getdis=memoize(getdis)
     mitMap = load_map("mit_map.txt")
     print isinstance(mitMap, Digraph)
     print isinstance(mitMap, WeightedDigraph)
     print 'nodes', mitMap.nodes
     print 'edges', mitMap.edges


     LARGE_DIST = 1000000

#     Test case 1
     print "---------------"
     print "Test case 1:"
     print "Find the shortest-path from Building 32 to 56"
     expectedPath1 = ['32', '56']
     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     print 'yahooo!!!!!'
     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath1
     print "Brute-force: ", brutePath1
     print "DFS: ", dfsPath1
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'

#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'

#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'

#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'

#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
