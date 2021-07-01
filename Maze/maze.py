class square():                                                #1

#"""closed_list should be a set, not a list to check if a Node has already been visited"""


    def __init__(self, father=None, position=None):
        self.father = father
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position  #called_here_outsideofclass
   # print("self.g")


def algo(maze, start, end):                  # """Returns a list of tuples as a path from the given start to th maze"""


    # Create start and end node
    start_node = square(None, start)
    start_node.g = start_node.h = start_node.f = 0 #inialized
    end_node = square(None, end)
    end_node.g = end_node.h = end_node.f = 0
    #print("start_node")

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list): #[(0, 'pi'), (1, 'pa'), (2, 'sa'), (3, 'na')]
            if item.f < current_node.f:
                current_node = item
                current_index = index
               # print("current_node");
        #print("open_list");
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.father
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1),
                             (0, 1),
                             (-1, 0),
                             (1, 0),
                             (-1, -1),
                             (-1, 1),
                             (1, -1),
                             (1, 1)]: # Adjacent squares
       # print("new_position");

            # Get node position
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or\
                    node_position[0] < 0 or \
                    node_position[1] > (len(maze[len(maze)-1]) -1) or\
                    node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = square(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values orun sunny
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
           # print(child.f)
            #print("(" + str(child.position[0]) + "),(" + str(child.position[1]) + ") = f " + str(child.f))
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            #print ("child.g")
            #print("(" + str(child.position[0]) + "),(" + str(child.position[1]) + ") = f " + str(child.f))


def main():

    game = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

    start = (1, 1)
    end = (5, 6)

    path = algo(game, start, end)
    print(path)
   # print("(" + str(child.position[0]) + "),(" + str(child.position[1]) + ") = f " + str(child.f))


if __name__ == '__main__':
    main()