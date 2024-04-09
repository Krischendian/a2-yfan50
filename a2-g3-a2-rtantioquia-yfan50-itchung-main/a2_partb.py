# Main Author: Raphael Antioquia, In Tae Chung
# Main Reviewer: In Tae Chung

from a1_partd import overflow
from a1_partc import Queue

"""
copy_board(board)

argument: 
board - 2D list of integers representing the game board.

functionality:
Creates and returns a deep copy of the given game board. Each cell in the original board
is copied to the new board, ensuring that changes to the new board won't affect the original.

return: 
A new 2D list that is a deep copy of the original board.
"""
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


"""
evaluate_board(board, player)

arguments:
board - 2D list of integers representing the game board.
player - Integer identifying the player (1 or -1).

functionality:
Evaluates the given board from the perspective of the specified player.
The function calculates the score for each player based on the board state,
assigning higher scores to winning conditions and lower scores to losing conditions.
The scoring mechanism is determined by the number of pieces each player has on the board,
with adjustments made for winning or losing conditions.

return:
Integer representing the score of the board from the specified player's perspective.
"""
def evaluate_board(board, player):
    player_score = 0
    opponent_score = 0

    # Looping through each cell in the game board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Get the value of the current cell
            cell_value = board[i][j]  
            
            # If the cell's value is positive, it represents player 1's pieces
            if cell_value > 0:
                if player == 1:
                    # If evaluating for player 1, add to player's score
                    player_score += cell_value  
                else:
                    # If evaluating for player 2, add to opponent's score (player 1's pieces)
                    opponent_score += cell_value  
            
            # If the cell's value is negative, it represents player 2's pieces
            elif cell_value < 0:
                if player == -1:
                    # If evaluating for player 2, add positive value to player's score
                    player_score += abs(cell_value)  
                else:
                    # If evaluating for player 1, add positive value to opponent's score (player 2's pieces)
                    opponent_score += abs(cell_value)  


    # Determine the winning condition and assign a fixed score for it
    if player_score > opponent_score and opponent_score == 0:
        # Fixed score for a clear winning condition
        return 100 
    elif player_score == 0 and opponent_score > 0:
        # Fixed score for a clear losing condition
        return -100  
    else:
        # Calculate a nuanced score based on the net advantage for other conditions
        net_score = player_score - opponent_score
        # Ensures a non-negative score that reflects the player's advantage
        return max(0, net_score)  



class GameTree:
    """
    GameTree.Node.__init__(board, depth, player, tree_height, score, move)

    arguments:
    board - 2D list representing the state of the game board.
    depth - Current depth in the game tree.
    player - Current player (1 or -1).
    tree_height - Maximum height of the game tree.
    score - Evaluation score of the node (None if not evaluated).
    move - The move that led to this board state (None if root).

    functionality:
    Initializes a Node in the GameTree. Sets up the game board associated with this node,
    the depth in the tree, the player's turn, and optionally the score and move that led to this state.
    The node initializes an empty list for children nodes to be added during tree expansion.

    return:
    None.
    """
    class Node:
        def __init__(self, board, depth, player, tree_height = 4, score = None, move = None):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.height = tree_height
            # Array that holds child nodes
            self.children = [] 
            self.score = score
            self.move = move


    """
    GameTree.__init__(board, player, tree_height)

    arguments:
    board - 2D list representing the state of the game board at the root of the game tree.
    player - The player (1 or -1) the tree is being created for.
    tree_height - Maximum height of the game tree.

    functionality:
    Initializes the GameTree object with the root node set to the given board state.
    Calls create_tree to recursively build the game tree to the specified height
    and applies the minimax algorithm to evaluate and score the nodes.

    return:
    None.
    """
    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        # Define the root
        self.root = self.Node(self.board, 0, player, tree_height) 
        # Create tree with self.root as starting point
        self.create_tree(self.root) 
        # Minimax algorithm to determine score of nodes
        self.minimax(self.root, player) 
    
    """
    create_tree(subtree)

    argument: 
    subtree - A Node object representing the current node in the game tree from which the tree will expand.

    functionality:
    Recursively expands the game tree from the given subtree by iterating over possible moves from the current board state.
    For each valid move, a new child Node is created with the resulting board state, and create_tree is called recursively
    until the maximum depth (tree_height) is reached or no more valid moves are available. This process builds out
    the complete game tree from the perspective of the initial player.

    return: 
    None. The game tree is built in-place by modifying the children of the Nodes.
    """
    def create_tree(self, subtree):
        # Base case: If depth hits the limit of tree_height, end function
        if subtree.depth == subtree.height - 1: 
            return

        # Iterate through board to determine valid moves
        for i in range(len(subtree.board)):
            for j in range(len(subtree.board[0])):
                cell_value = subtree.board[i][j]
                valid_move = False
                
                # Check if a move is valid for the current player
                if cell_value == 0:
                    valid_move = True
                elif cell_value > 0 and subtree.player == 1:
                    valid_move = True
                elif cell_value < 0 and subtree.player == -1:
                    valid_move = True
                
                # Common logic for handling a valid move
                if valid_move:
                    new_board = copy_board(subtree.board) # Create new board, so you don't affect the root board
                    new_board[i][j] += subtree.player # Add player gem to valid location
                    overflow(new_board, Queue()) # Overflow the new_board
                    new_child = self.Node(new_board, subtree.depth + 1, -subtree.player, subtree.height, move=(i, j)) # Create child node based on new board, increased depth, swapped player, height, and move used
                    subtree.children.append(new_child) # Push the child node to the current subtree's children array
        
        # After all possible children have been added to children array, iterating through each child recursively creating the subtree
        for child in subtree.children:
            self.create_tree(child) # Recursively continue creating children until base case is reached
    
    
    """
    minimax(node, maximizing_player)

    arguments:
    node - A Node object representing the current position in the game tree.
    maximizing_player - Boolean indicating if the current node is evaluated from the perspective of the maximizing player.

    functionality:
    Applies the minimax algorithm to evaluate the game tree rooted at the given node. For each node, it recursively
    calculates the optimal score by exploring all possible moves and their outcomes. The function chooses the move
    that maximizes the player's score if it's the player's turn, and minimizes the score if it's the opponent's turn.
    The scores are propagated up the tree, allowing the algorithm to determine the best possible move at the root.

    return:
    Integer representing the score of the node. For leaf nodes, the score is directly calculated from the board state.
    For internal nodes, the score is derived from the minimax evaluation of its children.
    """                
    def minimax(self, node, maximizing_player):
        # Check if the current node is a leaf node, either because it's reached the
        # maximum depth or represents a terminal game state (win or lose).
        if node.depth == node.height - 1 or node.score in [100, -100]:
            node.score = evaluate_board(node.board, maximizing_player)
            return node.score
        
        # If the current node represents the maximizing player's turn.
        if node.player == maximizing_player:
            # Initialize the best score for the maximizing player to negative infinity,
            # ensuring any score will be higher, thus making it possible to find the maximum score.
            max_eval = -float('inf')
            for child in node.children:
                # Recursively call minimax on the child nodes, keeping the perspective of
                # the maximizing player.
                eval = self.minimax(child, maximizing_player)
                # Update max_eval if the current child's evaluation is greater,
                # effectively choosing the best (maximum) score.
                max_eval = max(max_eval, eval)
            # Assign the best score found among children to the current node.
            node.score = max_eval
            return node.score
        else:
            # If it's the minimizing player's turn, initialize the best score
            # to positive infinity to find the minimum score among children.
            min_eval = float('inf')
            for child in node.children:
                # Recursively call minimax on the child nodes, switching the perspective
                # to that of the minimizing player (opponent).
                eval = self.minimax(child, -maximizing_player)
                # Update min_eval if the current child's evaluation is lower,
                # effectively choosing the worst (minimum) score from the perspective
                # of the maximizing player.
                min_eval = min(min_eval, eval)
            # Assign the worst score found among children to the current node.
            node.score = min_eval
            return node.score


    """
    get_move()

    arguments:
    None. Operates on the GameTree object it is called upon.

    functionality:
    Determines the best move to make from the current board state. It iterates over all direct children of the root node,
    evaluating their scores to choose the move that leads to the best outcome based on the minimax algorithm.
    This method assumes that the game tree has already been built and evaluated.

    return:
    Tuple (row, col) indicating the best move's coordinates on the board. If no move can improve the position, or in case of error,
    the return value may be None.
    """
    def get_move(self):
        # Empty variable to store best array
        best_move = None 

        # Initializing to -inf, so best_score will always update on first comparison
        best_score = -float('inf')  

        # Iterate through the self.root children to find best score
        for child in self.root.children: 
            if child.score > best_score:
                best_score = child.score
                best_move = child.move  
                
        return best_move


    """
    clear_tree()

    arguments:
    None. Operates on the GameTree object it is called upon.

    functionality:
    Recursively traverses the game tree, starting from the root, and clears all references to child nodes.
    This method helps in freeing up memory by ensuring that the garbage collector can reclaim the memory
    used by the nodes of the game tree. It's particularly useful to call this method before discarding
    a GameTree object or before starting a new game.

    return:
    None. The game tree is cleared in-place.
    """
    def clear_tree(self):
        # Recursive helper function
        def recursive_clear(node):
            # If the node is not None
            if node:  
                for child in node.children:
                    # Recursively clear each child
                    recursive_clear(child)  
                # Remove all children from the current node
                node.children = []  

        # Start the clearing process from the root
        recursive_clear(self.root)  
        # Remove the reference to the root node as well
        self.root = None  
