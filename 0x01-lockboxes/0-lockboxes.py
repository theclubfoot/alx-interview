def canUnlockAll(boxes):
    # Set to keep track of visited boxes
    visited = set()
    # Recursive function to open the boxes
    def open_boxes(boxes, i):
        # Base case: if the box is already visited, return
        if i in visited:
            return
        # Add the box to the visited set
        visited.add(i)
        # Open all the boxes that can be opened with the keys in the current box
        for key in boxes[i]:
            open_boxes(boxes, key)
    # Start by opening the first box
    open_boxes(boxes, 0)
    # Return True if all boxes can be opened, else return False
    return len(visited) == len(boxes)

