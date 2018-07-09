def abstand(start_coordinates, end_coordinates, dateiname="labyrinth.dat"):

    def get_lines_in_file(dateiname):
        #Return a list of strings, each a line on the labyrinth file.

        file_content = open(dateiname, "r")
        output = file_content.readlines()
        file_content.close()
        return output

    def count_lines_in_file(list_of_lines):
        #Returns amount of lines in the labyrinth file.
        return len(list_of_lines)

    def get_value_from_file(coordinates):
        #Return the value stored in given coordinates of the labyrinth in the file.
        first_coordinate = coordinates[0]
        second_coordinate = coordinates[1]
        return file_lines[first_coordinate][second_coordinate]

    def rows_and_columns():
            #Returns a tuple containing row and column count, from the labyrinth file.
            column_count = count_lines_in_file(file_lines) - 1
            row_count = len(file_lines[0]) - 2
            return (row_count, column_count)

    file_lines = get_lines_in_file(dateiname)
    row_count = rows_and_columns()[0]
    column_count = rows_and_columns()[1]
    passable_neighbours = {}


    def passable_neighbours_function(vertex):
            #Makes an entry in the passable neighbours dictionary for each vertex of neighbours with value p
            if get_value_from_file(vertex) == "U":
                return []

            neighbours_list = []
            if vertex[0] < column_count:
                neighbour_down = (vertex[0] + 1, vertex[1])
                neighbours_list.append(neighbour_down)
            if vertex[0] > 0:
                neighbour_up = (vertex[0] - 1, vertex[1])
                neighbours_list.append(neighbour_up)
            if vertex[1] > 0:
                neighbour_left = (vertex[0], vertex[1] - 1)
                neighbours_list.append(neighbour_left)
            if vertex[1] < (row_count):
                neighbour_right = (vertex[0], vertex[1] + 1)
                neighbours_list.append(neighbour_right)

            for neighbour in neighbours_list:

                if get_value_from_file(neighbour) == "P":
                    if vertex not in passable_neighbours:
                        passable_neighbours[vertex] = [neighbour]
                    else:
                        passable_neighbours[vertex].append(neighbour)

            if vertex not in passable_neighbours:
                passable_neighbours[vertex] = []

            return passable_neighbours[vertex]

    from collections import deque

    def calculate_abstand(start_coordinates, end_coordinates):
        #Returns the minimum amount of steps necessary to get from start_coordinates to end_coordinates

        if start_coordinates == end_coordinates:
            return 0

        path = set()
        queue = deque([start_coordinates])
        count = 0

        while len(queue) > 0:
            field = queue.pop()
            if field in path:
                continue
            path.add(field)
            if field == end_coordinates:
                return count
            passable_neighbours_not_in_path = [x for x in passable_neighbours_function(field) if x not in path]
            if passable_neighbours_not_in_path != []:
                count += 1
                for neighbour in passable_neighbours_not_in_path:
                    queue.appendleft(neighbour)

        return -1

    return calculate_abstand(start_coordinates, end_coordinates)