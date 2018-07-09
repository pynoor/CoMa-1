
class EulereanGraph:
        
    @staticmethod
  
    def eulertour(A):
    
        for adj_vertex_list in A:
            if len(adj_vertex_list)%2 != 0:
                return False
            else:
                continue
    
    
     #checking whether all lists in A are empty
     
        b = False
        for list_in_A in A:
            if list_in_A != []:
                b = True
            else:
                continue
        if b == False:
            return []
        
        # creating a List containing all edges in th graph described by A
        Edges_in_A = []
        for adj_vertex_list in A:
            for adj_vertex in adj_vertex_list:
                Edges_in_A.append((A.index(adj_vertex_list),adj_vertex))
                
    # note : this list contains tubles of pairs because the graph is undirected, i.e, disregarding isolated points.
    # creating a function to check whether or not graph described by A is connected using        
        def is_connected(A, Edges_in_A):
            #creating a list of all vertices in A that are incident to an edge
            Vertices = [] 
            
            for vertex in range(len(A)):
                if A[vertex] != []:
                    Vertices.append(vertex)
                else:
                    continue
    #        print(Vertices)
            r = Vertices[0]
            R = [r]
            F = []
            Queue = [r]
    #        print(Queue)
            while Queue != []:  
                v = Queue.pop()
                for x in Edges_in_A:
                    if x[0] == v and (x[1] not in R): 
                        R.append(x[1])
                        Queue.append(x[1])
                        F.append(x)
                    else:
                        continue 
            
    #        print("This is R")
    #        print(R)
    #        print("This is Vertices")
    #        print(Vertices)
            if set(R) == set(Vertices):
                return True
            else:
                return False   
            
        if is_connected(A, Edges_in_A) == False:
            return False
        
            
        for edge in Edges_in_A:
            if (edge[1],edge[0]) in Edges_in_A:
                Edges_in_A.remove((edge[1],edge[0]))
                
        def find_tour(A, starting_vertex):

            temp_stack = [starting_vertex]
            
            while A[starting_vertex] != []: 
                i = starting_vertex
                starting_vertex = A[starting_vertex][-1]
                temp_stack.append(starting_vertex)
                A[i].remove(starting_vertex)
                A[starting_vertex].remove(i)
    #            print("this is A[i] now")
    #            print (A[i])
    #            print("this is A[starting_vertex now")
    #            print (A[starting_vertex])
                if (i, starting_vertex) in Edges_in_A:
                    Edges_in_A.remove((i, starting_vertex))
                elif (starting_vertex, i) in Edges_in_A:
                    Edges_in_A.remove((starting_vertex, i))
            return temp_stack
        
        final_tour = []
        starting_vertex = Edges_in_A[0][0]
        final_tour += find_tour(A, starting_vertex)
        
        for vertex in final_tour:
            if len(A[vertex])>0:
                new_tour = find_tour(A,vertex) 
                x = final_tour.index(new_tour[0])
                del final_tour[x]
                final_tour[x:x] = new_tour
        for list in A:
            if len(list)>0:
                return False
        return final_tour 