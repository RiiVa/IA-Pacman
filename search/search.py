# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"

    #print("DFS")
    stack = util.Stack()
    visitor = []
    
    stack.push(((problem.getStartState(),1),[],0))
    
    return auxiliar_search(stack, visitor, problem)
    #while not stack.isEmpty():
    #    v,result = stack.pop()
    #    #print("Node",v)
    #    #print("Camino",result)
    #    if not (v[0] in visitor):
    #        visitor.append(v[0])
    #        
    #        if  problem.isGoalState(v[0]):
    #            return result
    #        #print(problem.getSuccessors(v[0]))
    #        for x in problem.getSuccessors(v[0]):
    #            if not x[0] in visitor:
    #                stack.push((x,result+[x[1]]))
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    #print("BFS")

    queue = util.Queue()
    visitor = []

    queue.push(((problem.getStartState(),0),[],0))

    return auxiliar_search(queue,visitor,problem)
    #while not queue.isEmpty():
    #    v,result = queue.pop()
    #    if not (v[0] in visitor):
    #        visitor.append(v[0])
    #        
    #        if  problem.isGoalState(v[0]):
    #            print(result)
    #            return result
    #        #print(problem.getSuccessors(v[0]))
    #        print(v[0])
    #        for x in problem.getSuccessors(v[0]):
    #            #print(x)
    #            if not x[0] in visitor:
    #                queue.push((x,result+[x[1]]))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    queue = util.PriorityQueueWithFunction(lambda i : i[2])

    visitor = []

    queue.push(((problem.getStartState(),0),[],0))

    return auxiliar_search(queue, visitor, problem)




    #dist = {}
    #dist[problem.getStartState()] = 0
    #prev = {}
    #visitor = {}
    #queue = util.PriorityQueue()
    #queue.push((problem.getStartState(),0),0)
    ##for x in problem.getSuccessors(problem.getStartState()):
    ##    queue.push(x,x[2])
    ##    prev[]
#    #oo= Infinity()
#
#    ##print("entro")
#    #while not queue.isEmpty():
#    # #   print("entro???")
#    #    v = queue.pop()
#    #    if 
#    #    visitor[v] = 1
#    #    for x in problem.getSuccessors(v[0]):
#    #        #print(dist)
#
#    #        alt = dist[v[0]]+ x[2]
#    #        #print(dist.get(x[0], oo)
#    #        if alt < (dist.get(x[0], oo)) :
#    #            dist[x[0]] = alt
#    #            prev[x[0]] = (v[0],x[1])
#
#    #            if x in visitor:
#    #                queue.push(x,alt)
#    #            else:
#    #                queue.update(x,alt)
#
#    ##print("nunca salio")
#    ##print(prev)
#
#    #return backmyprev(prev)
#



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    queue = util.PriorityQueueWithFunction(lambda i : i[2] + heuristic(i[0][0],problem))

    visitor = []

    queue.push(((problem.getStartState(),0),[],0))

    return auxiliar_search(queue, visitor, problem)


def auxiliar_search(struct, visitor, problem):

    while not struct.isEmpty():
        v,result,cost = struct.pop()
        if not (v[0] in visitor):
            visitor.append(v[0])
            
            if  problem.isGoalState(v[0]):
                #print(result)
                return result
            #print(problem.getSuccessors(v[0]))
            #print(v[0])
            for x in problem.getSuccessors(v[0]):
                #print(x)
                if not x[0] in visitor:
                    struct.push((x,result+[x[1]],cost+x[2]))



class Infinity:
    """Un valor mayor que todos los valores posibles
    de int() para comparaciones en el minimax
    """

    def __init__(self, positive = True):
        self.positive = positive

    def __le__(self, other):
        return not self.positive

    def __ge__(self, other):
        return self.positive

    def __lt__(self, other):
        return not self.positive

    def __gt__(self, other):
        return self.positive

    def __eq__(self, other):
        return False

    def __neg__(self):
        return Infinity(not self.positive)

    def __nonzero__(self):
        return True
# Abbreviations

bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

#oo= Infinity()

#dfs()