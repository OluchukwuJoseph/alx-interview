# The list of boxes, each box contains keys to other boxes. The goal is to determine
# if we can unlock all boxes starting from the first box (index 0).
boxes = [[1], [2], [3], [4], []]

# Function to determine if all boxes can be unlocked
def canUnlockAll():
    # Calculate the length of the "graph" starting from the first box and add 1 to include it
    length = lenghtOfGraph(boxes[0]) + 1
    print(length)  # Output the result, expecting the total number of boxes (5 in this case)

# Recursive function to calculate the "length" or reachability from a given box
def lenghtOfGraph(box):
    # Base case: if the current box has no keys (empty list), return 0
    if len(box) == 0:
        return 0
    # Recursive case: add 1 (for the current box) and call the function for the next box using the first key
    return 1 + lenghtOfGraph(boxes[box[0]])

# Loop-based method for depth-first search (DFS) to visit all reachable boxes
def LoopeddepthFirst():
    # Initialize a stack with the first box (starting point)
    stack = [boxes[0]]

    # Continue until the stack is empty (all reachable boxes are processed)
    while len(stack) > 0:
        # Remove the last item from the stack (current box being processed)
        current = stack.pop()
        print(current)  # Output the current box

        # Add all keys from the current box to the stack (i.e., explore the boxes it can unlock)
        for item in current:
            stack.append(boxes[item])

# Recursive method for depth-first search (DFS) to visit all reachable boxes
def RecursivedepthFirst(stack):
    # Base case: if the stack is empty, stop recursion
    if len(stack) == 0:
        return

    # Remove the last item from the stack (current box being processed)
    current = stack.pop()
    print(current)  # Output the current box

    # Add all keys from the current box to the stack (i.e., explore the boxes it can unlock)
    for item in current:
        stack.append(boxes[item])

    # Recursive call to process the next box
    RecursivedepthFirst(stack)

# Test the loop-based DFS function
LoopeddepthFirst()  # Expected output: [1] [2] [3] [4] []

# Test the recursive DFS function with a stack initialized with the first box
RecursivedepthFirst([[1]])  # Expected output: [1] [2] [3] [4] []

# Test the function to check if all boxes can be unlocked
canUnlockAll()  # Expected output: 5
