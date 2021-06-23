from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.distanceDict = {}

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.distanceDict[v] = -1

    # Print every distance from the head vertex
    def printDistances(self):
        print(self.distanceDict)

    # Retrun specific distance between v from the head
    def getDistFromTheHead(self, index):
        return self.distanceDict[index]

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        self.distanceDict[s] = 0

        # print(self.distanceDict)

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            # print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    self.distanceDict[i] = self.distanceDict[s] + 1
                    queue.append(i)
                    visited[i] = True


# This func convert given matrix to direct graph
def bulidGraph(Matrix):
    g = Graph()
    rowSize = len(Matrix)

    for row in range(rowSize):
        colSize = len(Matrix[row])

        for column in range(colSize):

            # change from [i][j] to number of index in the given matrix
            s = (row * colSize) + column
            # print("matrix[",row,"][",column,"]  s=", s)

            # Right
            if (column < colSize - 1 and Matrix[row][column + 1] != 'W'):
                u = s + 1
                g.addEdge(s, u)
            # Down
            if (row < rowSize - 1 and Matrix[row + 1][column] != 'W'):
                u = s + colSize
                g.addEdge(s, u)
            # left
            if (0 < column and Matrix[row][column - 1] != 'W'):
                u = s - 1
                g.addEdge(s, u)
            # Up
            if (0 < row and Matrix[row - 1][column] != 'W'):
                u = s - colSize
                g.addEdge(s, u)

    return g


# This func return the sum of all shortest path off all the employees from specific index
def SumAllShortdistancesOFfEmployeesFromIndex(index, matrix, g):
    g.BFS(index)
    sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (matrix[row][column] == 'E'):
                employeeindex = (row * len(matrix[row])) + column
                sum += g.getDistFromTheHead(employeeindex)
    return sum

#This func find the best empty space to put a kitchen in.
#The kitchen needs to be located in the empty space for which the sum of distances
#to all employees is minimal.
#The distance from an empty space to an employee is the shortest path from the employee
def findTheBestPlaceForTheKitchen(g,matrix):
  flag=0
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if (matrix[row][column] == ' '):
        EmptyIndex = (row * len(matrix[row])) + column
        sum=SumAllShortdistancesOFfEmployeesFromIndex(EmptyIndex, matrix, g)
        if(flag==0):
          minSum=sum
          saveIndex=row,column
          flag+=1
        if(minSum>=sum):
          minSum=sum
          saveIndex=row,column
        #print(EmptyIndex,sum,minSum)
  print("The best place is :",saveIndex)


# make matrix map from file
def make_map(file):
    map= []
    with open(file, 'r') as my_file:
        lines = my_file.readlines()
        for line in lines:
            if line[-1] == '\n':
                map.append(list(line)[:-1])
            else:
                map.append(list(line))
    return map


if __name__ == '__main__':

    matrix=make_map("mapText2.txt")
    g = bulidGraph(matrix)
    findTheBestPlaceForTheKitchen(g,matrix)



