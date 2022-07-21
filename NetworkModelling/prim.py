# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/minimum-spanning-trees-prims-algorithm/#whatisaminimumspanningtree
class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        # Initialize the adjacency matrix with zeros 
        self.m_graph = [[0 for column in range(num_of_nodes)] #why set to 0? # to show there is no connections
                    for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight #node 1 to 2 and node 2 to 1 have the same weight
        self.m_graph[node2][node1] = weight
        print("testing")

      
    def prims_mst(self):
        # Defining a really big number, that'll always be the highest weight in comparisons
        postitive_inf = float('inf') #inf? #act as the temporary high number so the first node will find it lesser
        #positive_inf, numbers are guaranteed to be below 10-setting the temporary value at 10 would been technically as valid
        print("lorem ipsum") #testing
        
        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes = [False for node in range(self.m_num_of_nodes)] # every column in this comprehension list represents a node

        # Matrix of the resulting MST
        result = [[0 for column in range(self.m_num_of_nodes)] 
                    for row in range(self.m_num_of_nodes)]
        
        indx = 0
        for i in range(self.m_num_of_nodes):
            print(self.m_graph[i])
        
        print(selected_nodes)

        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0
            


            for i in range(self.m_num_of_nodes):
                #we moved through the adjency matrix of the initial graph, using two loops.
                #The first loop is for the X-axis(rows) and the second loop is for the Y-axis(columns)
                # If the node is part of the MST, look its relationships
                if selected_nodes[i]: # validate that the node given by the first loop is selected b4 entering the second loop
                    for j in range(self.m_num_of_nodes):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                            # If the weight path analized is less than the minimum of the MST
                            if self.m_graph[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.m_graph[i][j]
                                start, end = i, j 
                                #start is the first randomly selected node
                                #end is the last node we add to the MST
            
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True

            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
            
            if minimum == postitive_inf:
                result[start][end] = 0

# When you start building the tree, none of the nodes are initally selcted, they are all False, so the first loop 
#would end before we enter the second loop. For this reason, start and end are initially set to 0, and when we exit from loop
#the Boolean value assigned to the end position will become True. As a result, one field of the result will be filled with the
# existing minimum, and since the result is symmetrical we can use the same trick on the self.m_graph to fill in anoter field.


            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            
            result[end][start] = result[start][end]

        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))       
        # the weight in the (i, j) position of the adjency matrix must be greater than zero
        # the vertex j must not be selected (if it's already selected this can lead to a cycle)        
                

#Given these two conditions, you can compare the edge weight of a given relationship with the general minimum
# of the MST. If the weight is less than the minimum, then it will become the new minimum, and the variables start and end
# will receive the i and j values. If the weight is more than the minimum, then you keep searching through the remaining columns.


#The start and end will populate the MST matrix, creating the tree we are looking for. After that, you repeat described process
#until you select all nodes from the inital graph.


                
                
                
                # Example graph has 9 nodes
example_graph = Graph(9)
                
example_graph.add_edge(0, 1, 4)
example_graph.add_edge(0, 2, 7)
example_graph.add_edge(1, 2, 11)
example_graph.add_edge(1, 3, 9)
example_graph.add_edge(1, 5, 20)
example_graph.add_edge(2, 5, 1)
example_graph.add_edge(3, 6, 6)
example_graph.add_edge(3, 4, 2)
example_graph.add_edge(4, 6, 10)
example_graph.add_edge(4, 8, 15)
example_graph.add_edge(4, 7, 5)
example_graph.add_edge(4, 5, 1)
example_graph.add_edge(5, 7, 3)
example_graph.add_edge(6, 8, 5)
example_graph.add_edge(7, 8, 12)


example_graph.prims_mst()
