#    Main Author(s): Raphael Antioquia, In Tae Chung
#    Main Reviewer(s): In Tae Chung


"""
HashTable class:
implements a hash table which stores key-value pairs
"""
class HashTable:
    """
    Node(key, value, next=None)

    arguments:
    key - The key associated with the node.
    value - The value associated with the key.
    next - A pointer to the next node in the list (default is None).

    functionality:
    Creates a new node that stores a key-value pair and a reference to the next node. 
    This node is used within the hash table to handle collisions by chaining.

    return:
    An instance of the Node class, containing the key, value, 
    and a reference to the next node.
    """
    class Node:
        def __init__(self, key, value, next=None):
            # Key for the current node
            self.key = key  
            # Value associated with the key
            self.value = value  
            # Pointer to the next node
            self.next = next  
            
    
    """
    __init__(cap=32)

    arguments:
    cap - The initial capacity of the hash table (default: 32).

    functionality:
    Initializes a new instance of a hash table with the specified capacity. 
    It creates an internal array (table) to store the key-value pairs, 
    with each entry initially set to None.

    return:
    None. An instance of the HashTable class is created.
    """
    def __init__(self, cap=32):        
         # Initialize the capacity (default: 32)
        self.cap = cap 
        # Initialize the size
        self.size = 0  
        # Initialize the table with None
        self.table = [None] * cap  

    
    """
    hash(key)

    arguments:
    key - The key to hash.

    functionality:
    Applies a hash function to the given key to determine its index 
    in the internal table array.
    This method ensures the index falls within the bounds of the current table capacity.

    return:
    Integer index where the key-value pair associated with the key should be stored.
    """
    def hash(self, key):      
        # Using python hash function, returns the index
        # modulus ensures returned value falls within bounds of current capacity
        return hash(key) % self.cap  

    
    """
    load_factor()

    arguments:
    None.

    functionality:
    Calculates the current load factor of the hash table, 
    defined as the number of stored key-value pairs divided
    by the table's capacity. The load factor is a measure of how full the hash table is.

    return:
    Float representing the current load factor of the hash table.
    """
    def load_factor(self):       
        # Calculate load factor
        return self.size / self.cap

    
    """
    resize()

    arguments:
    None.

    functionality:
    Doubles the capacity of the hash table and rehashes all 
    existing key-value pairs into a new, larger table.
    This method is called automatically when the load factor exceeds 
    a certain threshold (e.g., 0.7) to maintain efficient operations.

    return:
    None. The internal table's capacity is increased, and existing items are rehashed.
    """
    def resize(self):
        
        # Double the capacity
        new_cap = self.cap * 2  
        # New, larger table
        new_table = [None] * new_cap  
        # Temporary store for the old table
        old_table = self.table  
        # Update the capacity
        self.cap = new_cap  
        # Reset size before re-inserting items
        self.size = 0  
        # Set the table to the new, larger table
        self.table = new_table  

        # Rehash all items in the old table and insert them into the new table
        for head in old_table:
            while head:
                self.insert(head.key, head.value)
                head = head.next

    
    """
    insert(key, value)

    arguments:
    key - The key to insert.
    value - The value associated with the key.

    functionality:
    Inserts a new key-value pair into the hash table. 
    If the key already exists, the insertion fails. 
    Otherwise, the pair is added, and the table is resized 
    if necessary based on the load factor.

    return:
    True if the insertion was successful, False if the key already exists.
    """
    def insert(self, key, value):
        
        # Get the hash index
        index = self.hash(key)  
        # Get the head node at this index
        current = self.table[index] 

        # Check for existing key
        while current:
            if current.key == key:
                # Key already exists, insertion fails
                return False  
            current = current.next

        # Insert new node at the beginning of the linked list
        self.table[index] = self.Node(key, value, self.table[index])
        # Increment size
        self.size += 1  

        # Check if resizing is needed
        if self.load_factor() > 0.7:
            self.resize()

        # Insertion successful
        return True  

    
    """
    modify(key, value)

    arguments:
    key - The key whose value should be modified.
    value - The new value to associate with the key.

    functionality:
    Searches for the key in the hash table and updates its value if found.

    return:
    True if the key was found and its value updated, False if the key does not exist.
    """
    def modify(self, key, value):
        
        # Get the hash index
        index = self.hash(key) 
        # Get the head node at this index
        current = self.table[index]  

        # Traverse the list to find the node and modify its value
        while current:
            if current.key == key:
                current.value = value
                return True
            current = current.next

        # Key not found
        return False  

    
    """
    remove(key)

    arguments:
    key - The key to remove from the hash table.

    functionality:
    Searches for and removes the key-value pair associated with the given key from the hash table.

    return:
    True if the key was found and removed, False if the key does not exist.
    """
    def remove(self, key):
        
        # Get the hash index
        index = self.hash(key)  
        # Get the head node at this index
        current = self.table[index]  
        # Previous node, needed for removal
        prev = None  

        # Traverse the list to find the node to remove
        while current:
            if current.key == key:
                if prev:
                    # Bypass the node to be removed
                    prev.next = current.next  
                else:
                    # Update head of the list
                    self.table[index] = current.next  

                # Decrement size
                self.size -= 1  
                return True
            
            prev = current
            current = current.next

        # Key not found
        return False  

    
    """
    search(key)

    arguments:
    key - The key to search for.

    functionality:
    Searches for the key in the hash table and returns its associated value if found.

    return:
    The value associated with the key if found, None otherwise.
    """
    def search(self, key):
        
        # Get the hash index
        index = self.hash(key)  
        # Get the head node at this index
        current = self.table[index]  

        # Traverse the list to find the node
        while current:
            if current.key == key:
                return current.value
            current = current.next

        # Key not found
        return None  

    
    """
    capacity()

    arguments:
    None.

    functionality:
    Returns the current capacity of the hash table.

    return:
    Integer representing the current capacity of the hash table.
    """
    def capacity(self):
        
        return self.cap

    
    """
    __len__()

    arguments:
    None.

    functionality:
    Returns the current size of the hash table, i.e., the number of key-value pairs stored.

    return:
    Integer representing the number of key-value pairs in the hash table.
    """
    def __len__(self):       
        return self.size
