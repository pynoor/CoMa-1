from eulerean_graph import EulereanGraph

def test_first_sample_graph():
    sample_graph = [[1, 1], [0, 0]]
    expected_result = [0, 1, 0]
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result
    
def test_second_sample_graph():

    sample_graph = [[ 1 , 3 ] ,[0 ,3 ] ,[] ,[0 , 1 ]]

    expected_result = [0 , 3 , 1 , 0]
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result

def test_third_sample_graph():

    sample_graph = [[ 1 ,2 ,3 ,4 ] ,[0 ,2 ,3 ,4 ] ,[0 ,1 ,3 ,4 ] ,[0 ,1 ,2 ,4 ] ,[0 ,1 ,2 ,3 ]]

    expected_result = [0 , 4 , 3 , 2 , 4 , 1 , 3 , 0 , 2 , 1 , 0 ]
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result
    
def test_fourth_sample_graph():
    sample_graph = [[ 1 ,2 , 3 ] ,[0 ,2 , 3 ] ,[0 ,1 ,3 , 4 ] ,[0 ,1 ,2 , 4 ] ,[2 ,3 ]]
    expected_result = False
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result

def test_fifth_sample_graph():

    sample_graph = [[ 1 , 1 ] ,[0 ,0 ] ,[3 , 3 ] ,[2 ,2 ]]

    expected_result = False
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result
    
def test_sixth_sample_graph():

    sample_graph = [[1, 3], [0, 2, 4, 5] ,[1, 3, 4, 5], [0, 2], [1, 2], [1, 2]]

    expected_result = [0, 3, 2, 5, 1, 4, 2, 1, 0]
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result
    
def test_seventh_sample_graph():

    sample_graph = [[1, 3], [0, 2, 4, 5] ,[1, 3, 4, 5], [0, 2], [1, 2], [1, 2]]

    expected_result = [0, 3, 2, 5, 1, 4, 2, 1, 0]
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result
    
    
def test_crazy_sample_graph():

    sample_graph = [[39, 47, 40, 27, 55, 22, 28, 50, 37, 34, 16, 46, 30, 16, 30, 41, 55, 18, 15, 51, 50, 9, 17, 42, 56, 10], [7, 9, 43, 23, 18, 43, 36, 45, 23, 2, 15, 44, 48, 56, 49, 22, 45, 2, 31, 20, 37, 52, 2, 29, 20, 18, 33, 35, 42, 21, 9, 25, 55, 6, 43, 23, 17, 18, 30, 14, 41, 23, 54, 49, 31, 30, 44, 33, 13, 13, 45, 35, 2, 2, 20, 29, 29, 11], [1, 55, 1, 39, 35, 39, 15, 56, 47, 1, 49, 46, 37, 30, 20, 6, 37, 1, 1, 15, 53, 38, 46, 5, 29, 27, 39, 34, 35, 26, 46, 49], [20, 19, 36, 5, 26, 17, 26, 6, 29, 49, 16, 14, 30, 21, 52, 28, 8, 40, 41, 28, 16, 35], [40, 8, 45, 8, 39, 12, 28, 50, 15, 55, 40, 40, 28, 15, 49, 16, 25, 23, 46, 31, 44, 39, 14, 9, 32, 48, 42, 44, 44, 23], [46, 51, 30, 24, 3, 36, 37, 39, 51, 45, 45, 56, 16, 35, 50, 21, 7, 40, 28, 9, 24, 2, 8, 35, 6, 28, 38, 46], [2, 17, 47, 39, 14, 13, 10, 27, 55, 30, 17, 37, 33, 22, 39, 8, 24, 24, 44, 14, 15, 55, 40, 38, 22, 23, 5, 29, 45, 12, 1, 37, 40, 34, 7, 32, 52, 17, 23, 39, 53, 40, 13, 17, 3, 9, 30, 7, 22, 39, 32, 56, 21, 14, 52, 10], [52, 51, 35, 48, 45, 56, 31, 8, 51, 36, 6, 25, 49, 6, 48, 26, 28, 14, 43, 55, 5, 45, 1, 15, 38, 42, 24, 42, 15, 55, 30, 36, 55, 23], [20, 50, 24, 24, 10, 19, 33, 42, 7, 25, 19, 23, 30, 21, 27, 56, 3, 21, 31, 45, 47, 21, 49, 49, 9, 52, 17, 11, 4, 21, 56, 21, 4, 5, 6, 21, 26, 56], [27, 1, 53, 31, 15, 37, 6, 39, 35, 39, 56, 38, 42, 15, 55, 5, 13, 11, 46, 46, 0, 27, 37, 4, 42, 35, 1, 47, 55, 30, 49, 8, 25, 17, 40, 48], [8, 17, 12, 0, 28, 32, 56, 44, 37, 20, 25, 20, 55, 48, 37, 39, 20, 37, 16, 56, 6, 6, 54, 14, 20, 37, 43, 19], [9, 38, 44, 36, 24, 41, 38, 36, 37, 39, 8, 26, 15, 23, 31, 18, 34, 32, 13, 55, 27, 26, 49, 27, 31, 1], [37, 56, 44, 51, 4, 43, 27, 26, 45, 32, 39, 54, 35, 49, 28, 47, 17, 41, 46, 10, 28, 23, 28, 54, 51, 21, 17, 34, 54, 6], [45, 40, 37, 1, 56, 6, 11, 56, 44, 15, 15, 25, 6, 25, 49, 31, 1, 19, 9, 24, 33, 34, 16, 22, 27, 54, 20, 44, 38, 40], [21, 43, 1, 7, 37, 6, 51, 40, 6, 36, 18, 45, 19, 21, 17, 3, 26, 4, 29, 10, 6, 39, 41, 56, 39, 32, 36, 56, 27, 49, 52, 51], [29, 13, 55, 1, 25, 43, 39, 2, 4, 2, 28, 0, 7, 44, 42, 53, 29, 29, 32, 28, 7, 13, 25, 32, 6, 11, 17, 50, 38, 31, 4, 9, 31, 22, 9, 38], [48, 51, 35, 45, 30, 17, 31, 0, 22, 21, 18, 54, 13, 3, 55, 5, 33, 4, 26, 3, 41, 54, 36, 36, 49, 55, 10, 34, 23, 0], [16, 55, 8, 38, 55, 1, 3, 0, 12, 51, 34, 40, 6, 14, 43, 36, 21, 6, 40, 6, 55, 44, 15, 53, 44, 6, 12, 49, 43, 9, 44, 23, 10, 25], [48, 0, 35, 1, 43, 14, 29, 24, 40, 36, 33, 31, 46, 22, 56, 46, 55, 20, 16, 30, 49, 24, 11, 52, 53, 21, 35, 45, 38, 37, 1, 29, 28, 1, 19, 25, 54, 43, 34, 36], [13, 46, 46, 18, 35, 29, 8, 49, 8, 48, 34, 43, 3, 20, 23, 10, 53, 21, 40, 26, 55, 53, 27, 55, 26, 22, 14, 30, 30, 23, 46, 23], [30, 10, 2, 8, 3, 39, 53, 18, 32, 23, 51, 44, 45, 50, 22, 37, 37, 44, 23, 46, 34, 10, 10, 43, 1, 23, 46, 42, 32, 48, 1, 46, 52, 13, 10, 38, 31, 39, 25, 1, 19, 46, 26, 51], [43, 48, 36, 26, 8, 37, 3, 55, 8, 24, 16, 8, 17, 37, 28, 56, 32, 49, 34, 36, 8, 8, 12, 27, 1, 5, 27, 54, 31, 27, 6, 31, 14, 19, 24, 49, 18, 14, 8, 56], [16, 48, 42, 42, 55, 27, 0, 32, 29, 6, 6, 46, 32, 45, 6, 56, 29, 20, 48, 43, 43, 46, 32, 1, 15, 18, 53, 52, 19, 49, 34, 55, 35, 13], [19, 17, 20, 4, 48, 1, 49, 6, 40, 34, 54, 30, 20, 28, 30, 19, 12, 40, 20, 4, 16, 54, 38, 32, 32, 1, 1, 11, 27, 19, 1, 8, 6, 54, 44, 37, 33, 7], [39, 42, 43, 18, 21, 36, 7, 37, 28, 8, 47, 45, 11, 28, 13, 46, 49, 6, 32, 46, 8, 18, 35, 5, 30, 40, 40, 38, 48, 21, 6, 5, 37, 53], [36, 18, 54, 20, 47, 9, 8, 48, 45, 34, 15, 55, 37, 15, 17, 13, 47, 7, 29, 56, 10, 45, 4, 13, 41, 1, 26, 48, 51, 48], [47, 49, 11, 41, 14, 48, 44, 29, 3, 21, 12, 2, 16, 38, 3, 38, 51, 44, 42, 19, 20, 25, 47, 33, 7, 44, 29, 35, 8, 46, 11, 55, 52, 47, 32, 19, 49, 53], [0, 23, 11, 48, 52, 36, 21, 53, 38, 2, 21, 31, 41, 19, 31, 51, 54, 40, 48, 12, 51, 8, 14, 29, 13, 48, 34, 49, 55, 44, 36, 21, 9, 51, 6, 11, 22, 9, 28, 36], [36, 10, 15, 12, 55, 15, 34, 32, 47, 7, 56, 56, 23, 4, 4, 42, 24, 47, 45, 45, 40, 5, 33, 30, 29, 0, 24, 3, 46, 12, 39, 5, 31, 18, 50, 49, 12, 51, 29, 35, 31, 3, 49, 54, 46, 27, 29, 21], [43, 18, 51, 2, 18, 26, 35, 14, 43, 28, 40, 15, 54, 53, 1, 22, 31, 6, 15, 1, 1, 15, 53, 54, 32, 38, 53, 3, 43, 44, 32, 54, 28, 54, 44, 22, 47, 47, 38, 43, 28, 25, 26, 27, 36, 19], [16, 55, 23, 6, 24, 39, 20, 51, 41, 1, 8, 52, 23, 39, 19, 6, 35, 42, 54, 52, 52, 33, 54, 33, 0, 1, 0, 18, 34, 41, 19, 9, 2, 44, 28, 40, 5, 7, 3, 52, 39, 37], [27, 50, 33, 29, 13, 38, 28, 28, 53, 53, 27, 45, 1, 21, 20, 18, 4, 32, 15, 21, 46, 44, 7, 11, 8, 52, 9, 42, 11, 37, 54, 1, 42, 15, 16, 38], [44, 22, 22, 46, 26, 28, 23, 50, 4, 24, 48, 29, 29, 46, 31, 54, 42, 11, 20, 10, 55, 43, 48, 15, 15, 14, 12, 56, 50, 20, 6, 33, 51, 21, 6, 23, 55, 22], [1, 47, 18, 35, 30, 28, 26, 8, 13, 37, 43, 1, 48, 39, 31, 34, 39, 42, 49, 34, 23, 16, 39, 53, 36, 39, 56, 6, 30, 32], [50, 18, 47, 40, 33, 48, 27, 39, 22, 44, 37, 39, 39, 11, 55, 30, 33, 2, 0, 19, 36, 20, 45, 25, 38, 50, 6, 36, 51, 35, 51, 17, 23, 35, 35, 41, 16, 13, 28, 21, 47, 12], [34, 2, 40, 28, 19, 9, 30, 41, 16, 26, 3, 41, 7, 52, 33, 5, 22, 34, 9, 34, 1, 37, 29, 18, 24, 51, 37, 53, 2, 55, 41, 5, 1, 12, 46, 50, 37, 18], [14, 29, 55, 43, 3, 11, 53, 16, 55, 52, 21, 42, 1, 34, 17, 39, 33, 24, 21, 38, 25, 16, 47, 27, 28, 18, 5, 27, 7, 7, 47, 34, 14, 11, 54, 51, 18, 27], [35, 47, 5, 33, 0, 47, 14, 47, 47, 11, 49, 24, 18, 30, 35, 43, 38, 50, 10, 6, 10, 40, 20, 34, 40, 51, 24, 23, 41, 56, 9, 10, 2, 2, 12, 45, 45, 21, 20, 13, 48, 35, 46, 10, 44, 21, 1, 31, 6, 47, 25, 9], [43, 5, 6, 24, 36, 15, 11, 17, 26, 29, 26, 31, 34, 29, 52, 2, 11, 9, 20, 27, 23, 13, 18, 52, 37, 7, 15, 45, 31, 54], [34, 11, 14, 15, 49, 49, 9, 6, 2, 0, 28, 4, 30, 50, 40, 20, 41, 4, 46, 9, 30, 2, 36, 49, 33, 24, 6, 33, 33, 34, 10, 30, 6, 20, 49, 12, 55, 6, 33, 54, 34, 2, 14, 5], [52, 37, 9, 43, 47, 44, 3, 19, 6, 54, 23, 24, 56, 45, 4, 43, 27, 14, 17, 6, 46, 47, 49, 28, 29, 52, 13, 35, 34, 30, 24, 47, 0, 37, 13, 4, 23, 39, 42, 18, 6, 4, 41, 17, 47, 5], [56, 26, 35, 34, 49, 53, 40, 11, 52, 27, 14, 51, 1, 30, 16, 0, 30, 37, 39, 12, 35, 52, 3, 35, 51, 25], [24, 36, 55, 40, 33, 55, 7, 7, 9, 48, 48, 0, 53, 20, 54, 9, 26, 30, 22, 45, 31, 53, 4, 45, 31, 1, 22, 15, 28, 8, 52, 32], [19, 7, 1, 29, 29, 33, 20, 24, 17, 1, 32, 51, 18, 22, 22, 29, 12, 29, 15, 38, 21, 40, 45, 54, 51, 40, 36, 45, 17, 1, 18, 14, 37, 10], [20, 34, 46, 26, 11, 20, 17, 1, 23, 15, 12, 4, 6, 48, 30, 26, 55, 1, 56, 4, 29, 26, 17, 13, 32, 31, 47, 37, 46, 29, 40, 27, 52, 17, 52, 10, 13, 4], [24, 25, 56, 48, 5, 43, 43, 51, 42, 1, 7, 46, 1, 16, 28, 55, 34, 50, 54, 54, 40, 28, 50, 25, 37, 5, 31, 1, 42, 47, 8, 20, 22, 13, 7, 6, 12, 38, 37, 14, 4, 18], [40, 22, 56, 12, 50, 24, 2, 9, 44, 0, 45, 26, 9, 32, 2, 5, 48, 54, 54, 28, 44, 28, 19, 4, 20, 20, 2, 19, 32, 24, 31, 18, 20, 22, 56, 37, 54, 53, 52, 5, 35, 55, 18, 20, 19, 39], [29, 0, 40, 26, 2, 56, 28, 24, 26, 37, 36, 37, 33, 28, 53, 34, 37, 37, 37, 44, 25, 45, 6, 25, 36, 29, 54, 12, 26, 52, 48, 8, 40, 48, 34, 55, 40, 9, 40, 56], [49, 52, 46, 10, 23, 27, 32, 51, 49, 25, 42, 26, 21, 22, 27, 37, 32, 33, 25, 9, 18, 42, 19, 24, 7, 55, 16, 47, 27, 47, 45, 34, 1, 7, 53, 20, 25, 22, 4, 44], [48, 27, 8, 18, 41, 39, 33, 7, 9, 1, 23, 51, 4, 39, 2, 26, 3, 28, 13, 16, 2, 1, 17, 21, 54, 28, 48, 14, 12, 39, 50, 51, 21, 11, 8, 26, 19, 39, 22, 37, 40, 24], [8, 32, 28, 35, 46, 15, 49, 45, 53, 4, 45, 34, 39, 52, 5, 32, 0, 37, 31, 20, 34, 0], [7, 17, 28, 35, 34, 55, 45, 49, 34, 30, 25, 16, 48, 36, 14, 7, 43, 14, 5, 27, 29, 26, 12, 0, 20, 27, 32, 37, 27, 12, 41, 43, 20, 5, 41, 49], [41, 44, 42, 55, 38, 6, 53, 27, 30, 55, 18, 3, 40, 8, 41, 48, 47, 30, 31, 55, 20, 35, 50, 46, 1, 56, 54, 38, 14, 40, 22, 36, 26, 30, 30, 6, 44, 7], [46, 35, 55, 29, 33, 15, 6, 52, 50, 20, 19, 48, 31, 9, 29, 42, 18, 36, 24, 17, 41, 2, 27, 42, 26, 47, 31, 19, 29, 22], [36, 52, 29, 25, 38, 47, 23, 21, 30, 46, 31, 49, 45, 28, 29, 18, 23, 12, 29, 16, 12, 30, 32, 46, 45, 23, 27, 40, 13, 1, 12, 39, 43, 42, 29, 10, 16, 46], [19, 10, 0, 36, 27, 22, 35, 26, 52, 32, 17, 18, 46, 7, 17, 39, 52, 21, 28, 44, 17, 25, 0, 32, 51, 16, 7, 9, 7, 1, 19, 9, 53, 4, 22, 30, 16, 6, 11, 42, 36, 2, 48, 6, 45, 15, 34, 42, 52, 47], [14, 32, 9, 33, 25, 1, 13, 21, 0, 10, 40, 44, 52, 47, 22, 37, 41, 6, 5, 12, 14, 8, 46, 8, 7, 2, 28, 45, 13, 47, 10, 18, 21, 28, 46, 8]]

    expected_result = something_long
    
    result = EulereanGraph.eulertour(sample_graph)
    
    assert result == expected_result


  

    
