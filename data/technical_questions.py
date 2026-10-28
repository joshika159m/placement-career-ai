"""
Technical Assessment Question Bank
Contains verified multiple-choice questions across:
- IT Domain (63 questions across 7 topics, 9 questions each)
- Core/ECE Domain (64 questions across 8 topics, 8 questions each)
Total: 127 questions (IDs 101 to 227)
"""

TECHNICAL_QUESTIONS = [
    # =========================================================================
    # IT DOMAIN - TOPIC 1: Programming (IDs 101 - 109)
    # =========================================================================
    {
        "id": 101,
        "domain": "IT",
        "topic": "Programming",
        "question": "What is the time complexity of searching for an element in a balanced Binary Search Tree (BST)?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(log n)",
        "explanation": "In a balanced BST, each comparison halves the search space, giving an O(log n) time complexity."
    },
    {
        "id": 102,
        "domain": "IT",
        "topic": "Programming",
        "question": "In Python, which of the following data types is immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple",
        "explanation": "Tuples are immutable in Python, meaning their elements cannot be changed or reassigned after creation."
    },
    {
        "id": 103,
        "domain": "IT",
        "topic": "Programming",
        "question": "What does a pointer in C store?",
        "options": ["Value of a variable", "Memory address of a variable", "Data type of a variable", "Size of a variable"],
        "answer": "Memory address of a variable",
        "explanation": "A pointer is a variable that stores the memory address of another variable."
    },
    {
        "id": 104,
        "domain": "IT",
        "topic": "Programming",
        "question": "What will happen if recursion does not have a valid base condition?",
        "options": ["Infinite loop without crash", "Stack Overflow error", "Syntax Error", "Segmentation fault immediately"],
        "answer": "Stack Overflow error",
        "explanation": "Without a base condition, the recursive function calls keep adding frames to the call stack until memory is exhausted, causing a stack overflow."
    },
    {
        "id": 105,
        "domain": "IT",
        "topic": "Programming",
        "question": "Which operator cannot be overloaded in C++?",
        "options": ["+", "==", "::", "[]"],
        "answer": "::",
        "explanation": "The scope resolution operator (::), member access (.), pointer-to-member (.*), and ternary operator (?:) cannot be overloaded in C++."
    },
    {
        "id": 106,
        "domain": "IT",
        "topic": "Programming",
        "question": "In Java, what is the default value of an uninitialized boolean instance variable?",
        "options": ["true", "false", "null", "0"],
        "answer": "false",
        "explanation": "In Java, primitive boolean instance variables default to false when initialized."
    },
    {
        "id": 107,
        "domain": "IT",
        "topic": "Programming",
        "question": "What is the purpose of the 'finally' block in Java / Python exception handling?",
        "options": [
            "Executes only if an exception is caught",
            "Executes only if no exception occurs",
            "Always executes regardless of whether an exception occurs",
            "Prevents exceptions from occurring"
        ],
        "answer": "Always executes regardless of whether an exception occurs",
        "explanation": "The finally block contains cleanup code that executes whether an exception was raised, caught, or not."
    },
    {
        "id": 108,
        "domain": "IT",
        "topic": "Programming",
        "question": "What is the result of 5 ^ 3 in bitwise XOR operation?",
        "options": ["6", "8", "2", "15"],
        "answer": "6",
        "explanation": "5 in binary is 101, 3 is 011. XOR operation: 101 ^ 011 = 110 in binary, which is 6 in decimal."
    },
    {
        "id": 109,
        "domain": "IT",
        "topic": "Programming",
        "question": "Which keyword is used in C to prevent a variable from being modified after initialization?",
        "options": ["static", "volatile", "const", "register"],
        "answer": "const",
        "explanation": "The 'const' qualifier tells the compiler that the variable's value cannot be altered after initialization."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 2: Data Structures & Algorithms (IDs 110 - 118)
    # =========================================================================
    {
        "id": 110,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "options": ["Queue", "Stack", "Linked List", "Tree"],
        "answer": "Stack",
        "explanation": "A Stack operates on the LIFO principle where elements added last are removed first."
    },
    {
        "id": 111,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "What is the worst-case time complexity of QuickSort?",
        "options": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"],
        "answer": "O(n^2)",
        "explanation": "QuickSort degrades to O(n^2) in the worst case when the chosen pivot is repeatedly the smallest or largest element."
    },
    {
        "id": 112,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "Which algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights?",
        "options": ["Kruskal's Algorithm", "Dijkstra's Algorithm", "Prim's Algorithm", "Floyd-Warshall Algorithm"],
        "answer": "Dijkstra's Algorithm",
        "explanation": "Dijkstra's algorithm finds single-source shortest paths in graphs with non-negative edge weights."
    },
    {
        "id": 113,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "What is the minimum number of queues needed to implement a stack?",
        "options": ["1", "2", "3", "4"],
        "answer": "2",
        "explanation": "Two queues are typically required to implement a LIFO stack behavior by transferring elements between them."
    },
    {
        "id": 114,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "In a max-heap, where is the maximum element always located?",
        "options": ["At the deepest leaf", "At the root node", "At the leftmost node", "At any internal node"],
        "answer": "At the root node",
        "explanation": "In a max-heap, the key at the root is greater than or equal to the keys of its children, placing the maximum element at the root."
    },
    {
        "id": 115,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "What is the space complexity of Breadth-First Search (BFS) on a tree with branching factor b and depth d?",
        "options": ["O(d)", "O(b^d)", "O(b * d)", "O(1)"],
        "answer": "O(b^d)",
        "explanation": "BFS stores all nodes at the current level in the queue, requiring O(b^d) space at maximum depth."
    },
    {
        "id": 116,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "Which data structure is most efficient for checking whether a string has balanced parentheses?",
        "options": ["Queue", "Stack", "Array", "Binary Search Tree"],
        "answer": "Stack",
        "explanation": "A stack allows matching the most recently opened bracket with the currently encountered closing bracket."
    },
    {
        "id": 117,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "What is the average time complexity of insertion in a Hash Table?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(1)",
        "explanation": "A hash table provides constant time O(1) on average for search, insert, and delete operations."
    },
    {
        "id": 118,
        "domain": "IT",
        "topic": "Data Structures & Algorithms",
        "question": "Which of the following sorting algorithms is stable by default?",
        "options": ["HeapSort", "MergeSort", "QuickSort", "SelectionSort"],
        "answer": "MergeSort",
        "explanation": "MergeSort preserves the relative order of duplicate elements, making it a stable sort."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 3: OOP (IDs 119 - 127)
    # =========================================================================
    {
        "id": 119,
        "domain": "IT",
        "topic": "OOP",
        "question": "Which OOP concept allows a child class to provide a specific implementation of a method already defined in its parent class?",
        "options": ["Method Overloading", "Method Overriding", "Encapsulation", "Abstraction"],
        "answer": "Method Overriding",
        "explanation": "Method overriding allows a subclass to provide a specific implementation of a method defined in its superclass."
    },
    {
        "id": 120,
        "domain": "IT",
        "topic": "OOP",
        "question": "Wrapping data and methods into a single unit and restricting direct access to internal state is called:",
        "options": ["Inheritance", "Polymorphism", "Encapsulation", "Coupling"],
        "answer": "Encapsulation",
        "explanation": "Encapsulation binds data and functions together and hides internal component representations."
    },
    {
        "id": 121,
        "domain": "IT",
        "topic": "OOP",
        "question": "Can an abstract class in Java have a constructor?",
        "options": [
            "Yes, and it is called when a subclass is instantiated",
            "No, abstract classes cannot have constructors",
            "Only if all methods are abstract",
            "Only if it contains static methods"
        ],
        "answer": "Yes, and it is called when a subclass is instantiated",
        "explanation": "Abstract classes can have constructors in Java, which are invoked during subclass object creation via super()."
    },
    {
        "id": 122,
        "domain": "IT",
        "topic": "OOP",
        "question": "Which type of polymorphism is resolved at compile time?",
        "options": ["Method Overriding", "Method Overloading", "Virtual functions", "Dynamic Dispatch"],
        "answer": "Method Overloading",
        "explanation": "Method overloading (same method name, different signatures) is resolved at compile time (static polymorphism)."
    },
    {
        "id": 123,
        "domain": "IT",
        "topic": "OOP",
        "question": "What is the diamond problem in Object-Oriented Programming?",
        "options": [
            "Ambiguity arising from multiple inheritance when a class inherits from two classes having a common base",
            "A memory leak caused by circular object references",
            "A deadlock during multi-threaded method invocation",
            "Failure to destroy an object in destructor"
        ],
        "answer": "Ambiguity arising from multiple inheritance when a class inherits from two classes having a common base",
        "explanation": "The diamond problem arises when class D inherits from B and C, both of which inherit from A, causing ambiguity over which superclass method to execute."
    },
    {
        "id": 124,
        "domain": "IT",
        "topic": "OOP",
        "question": "In Java, which keyword is used to prevent a class from being inherited?",
        "options": ["static", "final", "abstract", "const"],
        "answer": "final",
        "explanation": "Declaring a class as 'final' prevents any other class from extending or subclassing it."
    },
    {
        "id": 125,
        "domain": "IT",
        "topic": "OOP",
        "question": "What is the relationship between an Engine and a Car called, where the Engine cannot exist independently of the Car?",
        "options": ["Aggregation", "Composition", "Generalization", "Association"],
        "answer": "Composition",
        "explanation": "Composition represents a strong 'has-a' relationship where the contained object cannot exist independently of the whole."
    },
    {
        "id": 126,
        "domain": "IT",
        "topic": "OOP",
        "question": "Which access modifier allows members to be accessed only within the same class?",
        "options": ["public", "protected", "private", "default"],
        "answer": "private",
        "explanation": "'private' members are accessible only within the body of the class in which they are declared."
    },
    {
        "id": 127,
        "domain": "IT",
        "topic": "OOP",
        "question": "What is dynamic binding (late binding) in OOP?",
        "options": [
            "Connecting a method call to method body at compile time",
            "Connecting a method call to method body at runtime",
            "Binding variables to memory during compilation",
            "Linking libraries before execution"
        ],
        "answer": "Connecting a method call to method body at runtime",
        "explanation": "Late binding resolves the method call at runtime based on the actual object instance type."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 4: DBMS (IDs 128 - 136)
    # =========================================================================
    {
        "id": 128,
        "domain": "IT",
        "topic": "DBMS",
        "question": "What does the 'A' in ACID properties of database transactions stand for?",
        "options": ["Availability", "Atomicity", "Accuracy", "Authentication"],
        "answer": "Atomicity",
        "explanation": "Atomicity ensures that all transaction operations either complete entirely or none take effect ('all-or-nothing')."
    },
    {
        "id": 129,
        "domain": "IT",
        "topic": "DBMS",
        "question": "A relation is in 2NF (Second Normal Form) if it is in 1NF and:",
        "options": [
            "Has no transitive dependencies",
            "Has no partial functional dependencies on candidate keys",
            "Has no multi-valued dependencies",
            "All attributes are prime attributes"
        ],
        "answer": "Has no partial functional dependencies on candidate keys",
        "explanation": "2NF requires eliminating partial dependencies; non-prime attributes must depend on the full candidate key."
    },
    {
        "id": 130,
        "domain": "IT",
        "topic": "DBMS",
        "question": "What is a Foreign Key in a relational database?",
        "options": [
            "A key used for encrypting external database files",
            "A primary key of another table used to establish a relationship",
            "A key that uniquely identifies a record in the same table",
            "A candidate key that was not chosen as the primary key"
        ],
        "answer": "A primary key of another table used to establish a relationship",
        "explanation": "A foreign key matches the primary key of a referenced table to enforce referential integrity."
    },
    {
        "id": 131,
        "domain": "IT",
        "topic": "DBMS",
        "question": "Which of the following concurrency anomalies occurs when a transaction reads data that has been modified by another transaction that has not yet committed?",
        "options": ["Dirty Read", "Non-repeatable Read", "Phantom Read", "Lost Update"],
        "answer": "Dirty Read",
        "explanation": "A dirty read occurs when a transaction reads uncommitted changes from another concurrent transaction."
    },
    {
        "id": 132,
        "domain": "IT",
        "topic": "DBMS",
        "question": "What is the primary purpose of indexing in database management systems?",
        "options": [
            "To encrypt table records",
            "To speed up data retrieval operations",
            "To enforce normal forms automatically",
            "To reduce disk storage requirements"
        ],
        "answer": "To speed up data retrieval operations",
        "explanation": "Indexes create lookup structures (like B-trees) that drastically reduce disk I/O during queries."
    },
    {
        "id": 133,
        "domain": "IT",
        "topic": "DBMS",
        "question": "Which schedule type guarantees no cascading aborts during transaction execution?",
        "options": ["Serial schedule", "Recoverable schedule", "Cascadeless schedule", "Strict schedule only"],
        "answer": "Cascadeless schedule",
        "explanation": "In a cascadeless schedule, transactions only read committed data from other transactions, preventing cascading aborts."
    },
    {
        "id": 134,
        "domain": "IT",
        "topic": "DBMS",
        "question": "What type of lock allows concurrent read operations on a data item but prevents any write operations?",
        "options": ["Exclusive lock (X-lock)", "Shared lock (S-lock)", "Intent lock", "Deadlock"],
        "answer": "Shared lock (S-lock)",
        "explanation": "A shared lock (S-lock) allows multiple transactions to read a record simultaneously while blocking write access."
    },
    {
        "id": 135,
        "domain": "IT",
        "topic": "DBMS",
        "question": "What is 3NF (Third Normal Form) primarily designed to eliminate?",
        "options": ["Atomic repeating groups", "Partial functional dependencies", "Transitive functional dependencies", "Join dependencies"],
        "answer": "Transitive functional dependencies",
        "explanation": "3NF requires a relation to be in 2NF and have no transitive functional dependencies between non-prime attributes."
    },
    {
        "id": 136,
        "domain": "IT",
        "topic": "DBMS",
        "question": "In the relational model, what is the cardinality of a relation?",
        "options": ["Number of columns", "Number of tuples (rows)", "Number of tables", "Number of foreign keys"],
        "answer": "Number of tuples (rows)",
        "explanation": "Cardinality is the total number of rows (tuples) in a relation, whereas degree is the number of attributes (columns)."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 5: SQL (IDs 137 - 145)
    # =========================================================================
    {
        "id": 137,
        "domain": "IT",
        "topic": "SQL",
        "question": "Which SQL clause is used to filter groups returned by an aggregate function like COUNT() or AVG()?",
        "options": ["WHERE", "HAVING", "GROUP BY", "ORDER BY"],
        "answer": "HAVING",
        "explanation": "The HAVING clause filters aggregated groups, whereas the WHERE clause filters individual rows prior to aggregation."
    },
    {
        "id": 138,
        "domain": "IT",
        "topic": "SQL",
        "question": "What is the difference between DELETE and TRUNCATE in SQL?",
        "options": [
            "DELETE is a DDL command; TRUNCATE is DML",
            "DELETE can be rolled back if in transaction; TRUNCATE cannot be easily rolled back and resets identity counters",
            "TRUNCATE removes specific rows; DELETE removes all rows",
            "Both operate identically"
        ],
        "answer": "DELETE can be rolled back if in transaction; TRUNCATE cannot be easily rolled back and resets identity counters",
        "explanation": "DELETE is a DML statement that logs row deletions and respects WHERE clauses. TRUNCATE is a DDL command deallocating data pages."
    },
    {
        "id": 139,
        "domain": "IT",
        "topic": "SQL",
        "question": "Which SQL join returns all rows from the left table and matched rows from the right table, filling with NULL where no match exists?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        "answer": "LEFT JOIN",
        "explanation": "LEFT JOIN (or LEFT OUTER JOIN) returns all records from the left table and matched records from the right table."
    },
    {
        "id": 140,
        "domain": "IT",
        "topic": "SQL",
        "question": "What does the SQL command 'UNION' do compared to 'UNION ALL'?",
        "options": [
            "UNION combines and eliminates duplicates; UNION ALL keeps duplicates",
            "UNION ALL eliminates duplicates; UNION keeps duplicates",
            "UNION works only on numeric data",
            "UNION requires identical table structures; UNION ALL does not"
        ],
        "answer": "UNION combines and eliminates duplicates; UNION ALL keeps duplicates",
        "explanation": "UNION removes duplicate rows from the combined result set, whereas UNION ALL includes all duplicate records."
    },
    {
        "id": 141,
        "domain": "IT",
        "topic": "SQL",
        "question": "How do you select the top 5 highest salaries from an Employee table in standard SQL?",
        "options": [
            "SELECT salary FROM Employee ORDER BY salary DESC LIMIT 5;",
            "SELECT TOP 5 salary FROM Employee ORDER BY salary ASC;",
            "SELECT salary FROM Employee WHERE salary = MAX(5);",
            "SELECT salary FROM Employee GROUP BY salary LIMIT 5;"
        ],
        "answer": "SELECT salary FROM Employee ORDER BY salary DESC LIMIT 5;",
        "explanation": "Sorting descending by salary ('ORDER BY salary DESC') and taking 'LIMIT 5' yields the top 5 highest salaries."
    },
    {
        "id": 142,
        "domain": "IT",
        "topic": "SQL",
        "question": "Which aggregate function ignores NULL values when calculating the total count of an attribute?",
        "options": ["COUNT(*)", "COUNT(column_name)", "SUM(*)", "COUNT_ALL()"],
        "answer": "COUNT(column_name)",
        "explanation": "COUNT(column_name) counts only non-NULL occurrences in that specific column, whereas COUNT(*) counts all rows."
    },
    {
        "id": 143,
        "domain": "IT",
        "topic": "SQL",
        "question": "Which SQL constraint ensures that all values in a column are distinct?",
        "options": ["DEFAULT", "CHECK", "UNIQUE", "NOT NULL"],
        "answer": "UNIQUE",
        "explanation": "The UNIQUE constraint ensures that all values in a column are different from one another."
    },
    {
        "id": 144,
        "domain": "IT",
        "topic": "SQL",
        "question": "What is the function of the SQL keyword 'COALESCE(val1, val2, val3)'?",
        "options": [
            "Returns the average of non-null values",
            "Returns the first non-null expression in the argument list",
            "Concatenates all non-null strings",
            "Checks if all arguments are equal"
        ],
        "answer": "Returns the first non-null expression in the argument list",
        "explanation": "COALESCE evaluates arguments in order and returns the first value that is not NULL."
    },
    {
        "id": 145,
        "domain": "IT",
        "topic": "SQL",
        "question": "Which operator is used in SQL pattern matching with wildcards ('%' and '_')?",
        "options": ["IN", "EXISTS", "LIKE", "BETWEEN"],
        "answer": "LIKE",
        "explanation": "The LIKE operator searches for specified patterns using wildcards ('%' for multiple characters, '_' for single character)."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 6: Operating Systems (IDs 146 - 154)
    # =========================================================================
    {
        "id": 146,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "Which of the following is NOT a necessary condition for a deadlock to occur (Coffman conditions)?",
        "options": ["Mutual Exclusion", "Hold and Wait", "Preemption", "Circular Wait"],
        "answer": "Preemption",
        "explanation": "The four Coffman conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Preemption breaks deadlocks."
    },
    {
        "id": 147,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What is 'thrashing' in an Operating System?",
        "options": [
            "A CPU hardware overheating failure",
            "A state where the system spends more time paging than executing processes",
            "A virus corrupting the master boot record",
            "A high-frequency network collision"
        ],
        "answer": "A state where the system spends more time paging than executing processes",
        "explanation": "Thrashing occurs when main memory is overcommitted, causing continuous page faults and disk swapping."
    },
    {
        "id": 148,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "Which CPU scheduling algorithm gives minimum average waiting time for a given set of processes?",
        "options": ["First-Come-First-Served (FCFS)", "Shortest Job First (SJF)", "Round Robin (RR)", "Priority Scheduling"],
        "answer": "Shortest Job First (SJF)",
        "explanation": "SJF is provably optimal in minimizing average waiting time for a static set of processes."
    },
    {
        "id": 149,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What is the main advantage of threads over processes in multi-tasking systems?",
        "options": [
            "Threads have isolated, separate address spaces",
            "Lower overhead for creation and context switching as they share memory",
            "Threads never experience deadlocks",
            "Threads execute without CPU clock cycles"
        ],
        "answer": "Lower overhead for creation and context switching as they share memory",
        "explanation": "Threads share memory and resources within the same process, making creation and context switching faster than process switching."
    },
    {
        "id": 150,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What algorithm is commonly used for deadlock avoidance in operating systems?",
        "options": ["Dijkstra's Shortest Path", "Banker's Algorithm", "Round Robin", "LRU Algorithm"],
        "answer": "Banker's Algorithm",
        "explanation": "The Banker's Algorithm tests for safe states before allocating requested resources to avoid deadlocks."
    },
    {
        "id": 151,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What is virtual memory primarily used for?",
        "options": [
            "Increasing the CPU clock speed",
            "Allowing execution of processes larger than physical RAM",
            "Backing up data permanently to secondary storage",
            "Encrypting file system directories"
        ],
        "answer": "Allowing execution of processes larger than physical RAM",
        "explanation": "Virtual memory maps secondary storage space as physical address space, enabling execution of programs larger than RAM."
    },
    {
        "id": 152,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What is a 'race condition' in concurrent programming?",
        "options": [
            "A competition between processes to execute first without shared data",
            "When the outcome of execution depends on the uncontrollable timing/order of threads accessing shared data",
            "A network packet collision in Ethernet",
            "A fast hardware context switch"
        ],
        "answer": "When the outcome of execution depends on the uncontrollable timing/order of threads accessing shared data",
        "explanation": "A race condition occurs when concurrent threads access and modify shared resources without proper synchronization."
    },
    {
        "id": 153,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "Which page replacement algorithm suffers from Belady's Anomaly?",
        "options": ["FIFO (First In First Out)", "LRU (Least Recently Used)", "Optimal Page Replacement", "LFU (Least Frequently Used)"],
        "answer": "FIFO (First In First Out)",
        "explanation": "FIFO page replacement can exhibit Belady's Anomaly, where increasing the number of page frames results in more page faults."
    },
    {
        "id": 154,
        "domain": "IT",
        "topic": "Operating Systems",
        "question": "What is the role of the TLB (Translation Lookaside Buffer)?",
        "options": [
            "A cache used to reduce the time taken to access virtual-to-physical page mappings",
            "A buffer for network packet translation",
            "A queue for printer spooling",
            "A secondary memory disk controller"
        ],
        "answer": "A cache used to reduce the time taken to access virtual-to-physical page mappings",
        "explanation": "The TLB is a high-speed hardware memory cache that stores recent virtual-to-physical page table translations."
    },

    # =========================================================================
    # IT DOMAIN - TOPIC 7: Computer Networks (IDs 155 - 163)
    # =========================================================================
    {
        "id": 155,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "Which layer of the OSI model is responsible for end-to-end reliable delivery and flow control?",
        "options": ["Network Layer", "Transport Layer", "Data Link Layer", "Session Layer"],
        "answer": "Transport Layer",
        "explanation": "The Transport Layer (Layer 4) manages reliable end-to-end communication, segmentation, flow control, and error correction (TCP)."
    },
    {
        "id": 156,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "What is the standard port number for HTTPS (Hypertext Transfer Protocol Secure)?",
        "options": ["80", "8080", "443", "22"],
        "answer": "443",
        "explanation": "HTTPS runs over port 443 by default, whereas HTTP runs on port 80."
    },
    {
        "id": 157,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "Which protocol resolves an IP address to a physical MAC address in a local area network?",
        "options": ["DNS", "DHCP", "ARP", "RARP"],
        "answer": "ARP",
        "explanation": "ARP (Address Resolution Protocol) maps a known 32-bit IPv4 address to a 48-bit physical MAC address."
    },
    {
        "id": 158,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "What is the main difference between TCP and UDP?",
        "options": [
            "TCP is connection-oriented and reliable; UDP is connectionless and faster",
            "UDP is connection-oriented and reliable; TCP is connectionless",
            "TCP operates at the Network layer; UDP operates at the Transport layer",
            "UDP handles encryption; TCP does not"
        ],
        "answer": "TCP is connection-oriented and reliable; UDP is connectionless and faster",
        "explanation": "TCP establishes a 3-way handshake and guarantees packet arrival; UDP sends packets without connection overhead or delivery guarantees."
    },
    {
        "id": 159,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "What is the subnet mask for a default Class C IPv4 network (/24)?",
        "options": ["255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.255"],
        "answer": "255.255.255.0",
        "explanation": "A /24 subnet has 24 network bits set to 1, producing the mask 255.255.255.0."
    },
    {
        "id": 160,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "Which routing protocol uses the Bellman-Ford algorithm and hop count as its primary metric?",
        "options": ["OSPF", "BGP", "RIP", "IS-IS"],
        "answer": "RIP",
        "explanation": "RIP (Routing Information Protocol) uses hop count as metric with a maximum limit of 15 hops and implements Bellman-Ford."
    },
    {
        "id": 161,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "What is the primary function of DNS (Domain Name System)?",
        "options": [
            "Assigning IP addresses to client machines dynamically",
            "Translating human-friendly domain names to numeric IP addresses",
            "Filtering network traffic at firewall boundaries",
            "Encrypting email communications"
        ],
        "answer": "Translating human-friendly domain names to numeric IP addresses",
        "explanation": "DNS acts as the internet's directory, resolving human-readable names (e.g., google.com) to machine IP addresses."
    },
    {
        "id": 162,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "In the TCP three-way handshake, what are the sequence of packets sent between client and server?",
        "options": ["SYN -> SYN-ACK -> ACK", "ACK -> SYN -> SYN-ACK", "SYN -> ACK -> DATA", "CONNECT -> ACCEPT -> ACK"],
        "answer": "SYN -> SYN-ACK -> ACK",
        "explanation": "Connection establishment: Client sends SYN, Server replies with SYN-ACK, Client confirms with ACK."
    },
    {
        "id": 163,
        "domain": "IT",
        "topic": "Computer Networks",
        "question": "Which device operates at Layer 2 (Data Link Layer) of the OSI model to forward frames based on MAC addresses?",
        "options": ["Router", "Switch", "Hub", "Repeater"],
        "answer": "Switch",
        "explanation": "A network switch operates at Layer 2 and uses a MAC address lookup table to forward frames to specific ports."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 1: Digital Electronics (IDs 164 - 171)
    # =========================================================================
    {
        "id": 164,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "Which of the following gates is considered a 'Universal Gate'?",
        "options": ["AND gate", "OR gate", "NAND gate", "XOR gate"],
        "answer": "NAND gate",
        "explanation": "NAND and NOR gates are universal gates because any Boolean function can be implemented using only these gates."
    },
    {
        "id": 165,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "How many select lines are required for a 16-to-1 Multiplexer?",
        "options": ["2", "4", "8", "16"],
        "answer": "4",
        "explanation": "For an N-to-1 MUX, 2^m = N select lines are needed. Since 2^4 = 16, 4 select lines are required."
    },
    {
        "id": 166,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "What is the 2's complement of the binary number 101100?",
        "options": ["010011", "010100", "010010", "110100"],
        "answer": "010100",
        "explanation": "1's complement of 101100 is 010011. Adding 1: 010011 + 1 = 010100."
    },
    {
        "id": 167,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "What condition causes an indeterminate race-around state in an SR flip-flop?",
        "options": ["S = 0, R = 0", "S = 1, R = 0", "S = 0, R = 1", "S = 1, R = 1"],
        "answer": "S = 1, R = 1",
        "explanation": "When both S and R inputs are 1 simultaneously, both outputs attempt to go LOW, resulting in an invalid/forbidden state."
    },
    {
        "id": 168,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "A decade counter requires a minimum of how many flip-flops?",
        "options": ["2", "3", "4", "10"],
        "answer": "4",
        "explanation": "A decade counter counts 10 states (0 to 9). Since 2^3 = 8 < 10 and 2^4 = 16 >= 10, a minimum of 4 flip-flops is required."
    },
    {
        "id": 169,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "De Morgan's theorem states that (A + B)' is equivalent to:",
        "options": ["A' + B'", "A' . B'", "(A . B)'", "A . B"],
        "answer": "A' . B'",
        "explanation": "The complement of a logical OR operation equals the logical AND of the inverted variables: (A + B)' = A' . B'."
    },
    {
        "id": 170,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "What is the primary difference between combinational and sequential logic circuits?",
        "options": [
            "Combinational circuits have memory; sequential do not",
            "Sequential circuit output depends on present inputs and past state (memory); combinational depends only on present inputs",
            "Sequential circuits operate only with analog signals",
            "Combinational circuits require a clock signal"
        ],
        "answer": "Sequential circuit output depends on present inputs and past state (memory); combinational depends only on present inputs",
        "explanation": "Sequential circuits have feedback/memory elements whose output depends on both current inputs and previous history."
    },
    {
        "id": 171,
        "domain": "Core",
        "topic": "Digital Electronics",
        "question": "What is the resolution of an 8-bit Analog-to-Digital Converter (ADC) with a reference voltage of 5.12 V?",
        "options": ["10 mV", "20 mV", "40 mV", "50 mV"],
        "answer": "20 mV",
        "explanation": "Number of steps = 2^8 = 256. Resolution = 5.12 V / 256 = 0.02 V = 20 mV."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 2: Analog Electronics (IDs 172 - 179)
    # =========================================================================
    {
        "id": 172,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What is the ideal input impedance of an Operational Amplifier (Op-Amp)?",
        "options": ["Zero", "50 Ohms", "Infinite", "1 Megaohm"],
        "answer": "Infinite",
        "explanation": "An ideal op-amp draws no input current, which corresponds to an infinite input impedance."
    },
    {
        "id": 173,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What type of feedback is applied in an amplifier circuit to increase stability and bandwidth?",
        "options": ["Positive feedback", "Negative feedback", "Regenerative feedback", "No feedback"],
        "answer": "Negative feedback",
        "explanation": "Negative feedback reduces distortion, stabilizes gain, widens bandwidth, and controls input/output impedances."
    },
    {
        "id": 174,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "In a BJT operating in the active region, the junctions are biased as follows:",
        "options": [
            "Emitter-Base forward biased, Collector-Base reverse biased",
            "Both junctions forward biased",
            "Both junctions reverse biased",
            "Emitter-Base reverse biased, Collector-Base forward biased"
        ],
        "answer": "Emitter-Base forward biased, Collector-Base reverse biased",
        "explanation": "For normal amplification (active mode), the E-B junction must be forward biased and C-B junction reverse biased."
    },
    {
        "id": 175,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What is the voltage gain of an ideal voltage follower (buffer) op-amp circuit?",
        "options": ["0", "1", "10", "Infinite"],
        "answer": "1",
        "explanation": "A voltage follower provides unity voltage gain (A_v = 1) with high input impedance and low output impedance."
    },
    {
        "id": 176,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What is the Common Mode Rejection Ratio (CMRR) of an ideal differential amplifier?",
        "options": ["0", "1", "100 dB", "Infinite"],
        "answer": "Infinite",
        "explanation": "An ideal differential amplifier completely rejects common-mode noise signals (A_cm = 0), yielding infinite CMRR."
    },
    {
        "id": 177,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "Which diode is primarily used as a constant voltage reference in voltage regulation circuits?",
        "options": ["Varactor diode", "Schottky diode", "Zener diode", "Tunnel diode"],
        "answer": "Zener diode",
        "explanation": "Zener diodes maintain a stable breakdown voltage across their terminals when operated in reverse bias."
    },
    {
        "id": 178,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What is Barkhausen's criterion for sustained oscillations in an oscillator circuit?",
        "options": [
            "Loop gain |A * beta| >= 1 and total loop phase shift = 0 or 360 degrees",
            "Loop gain |A * beta| = 0",
            "Phase shift = 180 degrees only",
            "Loop gain must be negative"
        ],
        "answer": "Loop gain |A * beta| >= 1 and total loop phase shift = 0 or 360 degrees",
        "explanation": "Barkhausen criteria require loop gain magnitude >= 1 and zero (or 360 degree) phase shift around the feedback loop."
    },
    {
        "id": 179,
        "domain": "Core",
        "topic": "Analog Electronics",
        "question": "What is the maximum theoretical efficiency of a Class-A power amplifier with transformer coupling?",
        "options": ["25%", "50%", "78.5%", "90%"],
        "answer": "50%",
        "explanation": "Transformer-coupled Class-A amplifiers achieve a maximum theoretical efficiency of 50% (direct-coupled is 25%)."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 3: Microprocessors (IDs 180 - 187)
    # =========================================================================
    {
        "id": 180,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "How many address lines and data lines are present in the classic 8085 microprocessor?",
        "options": ["16 address lines, 8 data lines", "8 address lines, 16 data lines", "16 address lines, 16 data lines", "20 address lines, 8 data lines"],
        "answer": "16 address lines, 8 data lines",
        "explanation": "The 8085 has 16 address lines (accessing up to 64 KB memory) and an 8-bit bidirectional data bus."
    },
    {
        "id": 181,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "Which interrupt in the 8085 microprocessor is non-maskable?",
        "options": ["RST 7.5", "RST 6.5", "INTR", "TRAP"],
        "answer": "TRAP",
        "explanation": "TRAP (RST 4.5) is the highest-priority, non-maskable hardware interrupt in the 8085 microprocessor."
    },
    {
        "id": 182,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "What is the function of the Program Counter (PC) register in a microprocessor?",
        "options": [
            "Counts total instructions executed",
            "Holds the memory address of the next instruction to be fetched and executed",
            "Stores temporary calculation results",
            "Controls the system clock frequency"
        ],
        "answer": "Holds the memory address of the next instruction to be fetched and executed",
        "explanation": "The Program Counter points to the address of the next sequential instruction in memory."
    },
    {
        "id": 183,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "What is the memory addressing capacity of the 8086 microprocessor with its 20-bit address bus?",
        "options": ["64 KB", "512 KB", "1 MB", "4 MB"],
        "answer": "1 MB",
        "explanation": "With 20 address lines, 2^20 bytes = 1,048,576 bytes = 1 MB of physical memory can be addressed."
    },
    {
        "id": 184,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "In 8086 memory segmentation, how is the physical 20-bit address calculated from Segment and Offset registers?",
        "options": [
            "Physical Address = Segment + Offset",
            "Physical Address = (Segment * 16) + Offset",
            "Physical Address = (Segment * 256) + Offset",
            "Physical Address = (Offset * 16) + Segment"
        ],
        "answer": "Physical Address = (Segment * 16) + Offset",
        "explanation": "The 16-bit segment value is shifted left by 4 bits (multiplied by 16 or 10H) and added to the 16-bit offset."
    },
    {
        "id": 185,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "What does the ALE (Address Latch Enable) signal in 8085 indicate?",
        "options": [
            "A memory write operation is taking place",
            "Address bus lines AD0-AD7 contain a valid address during the first clock cycle (T1)",
            "The processor is in a HALT state",
            "An interrupt has been acknowledged"
        ],
        "answer": "Address bus lines AD0-AD7 contain a valid address during the first clock cycle (T1)",
        "explanation": "ALE pulses HIGH during T1 of a machine cycle to demultiplex the lower-order address from the data bus using an external latch."
    },
    {
        "id": 186,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "In 8085, which register pair is commonly used as a default memory pointer (M)?",
        "options": ["B-C pair", "D-E pair", "H-L pair", "Stack Pointer (SP)"],
        "answer": "H-L pair",
        "explanation": "The H-L register pair holds the 16-bit address for memory operand instructions referencing register 'M'."
    },
    {
        "id": 187,
        "domain": "Core",
        "topic": "Microprocessors",
        "question": "What is the size of the instruction prefetch queue in the 8086 microprocessor Bus Interface Unit (BIU)?",
        "options": ["4 bytes", "6 bytes", "8 bytes", "16 bytes"],
        "answer": "6 bytes",
        "explanation": "The 8086 BIU implements a 6-byte FIFO instruction queue enabling instruction pipelining."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 4: Microcontrollers (IDs 188 - 195)
    # =========================================================================
    {
        "id": 188,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "What is the primary architectural difference between Harvard and Von Neumann architectures?",
        "options": [
            "Harvard uses separate physical buses for instructions and data; Von Neumann shares a common bus",
            "Von Neumann uses RISC; Harvard uses CISC",
            "Harvard has no RAM",
            "Von Neumann supports higher clock frequencies only"
        ],
        "answer": "Harvard uses separate physical buses for instructions and data; Von Neumann shares a common bus",
        "explanation": "Harvard architecture separates instruction and data memories/buses, allowing simultaneous instruction fetch and data read."
    },
    {
        "id": 189,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "The standard 8051 microcontroller contains how many 8-bit parallel I/O ports?",
        "options": ["2 ports", "3 ports", "4 ports", "8 ports"],
        "answer": "4 ports",
        "explanation": "The classic 8051 has four 8-bit bidirectional I/O ports designated Port 0, Port 1, Port 2, and Port 3 (total 32 pins)."
    },
    {
        "id": 190,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "What is the size of internal on-chip RAM in the original standard 8051 microcontroller?",
        "options": ["128 bytes", "256 bytes", "1 KB", "4 KB"],
        "answer": "128 bytes",
        "explanation": "The standard 8051 features 128 bytes of internal data RAM (addresses 00H to 7FH) and 4 KB on-chip ROM."
    },
    {
        "id": 191,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "Which communication protocol is a synchronous, full-duplex serial protocol using Master-Slave topology with MOSI, MISO, SCK, and CS lines?",
        "options": ["I2C", "UART", "SPI", "CAN"],
        "answer": "SPI",
        "explanation": "SPI (Serial Peripheral Interface) uses 4 lines (MOSI, MISO, SCK, CS) for synchronous high-speed full-duplex communication."
    },
    {
        "id": 192,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "How many wires does the I2C communication protocol use for multi-device bus communication?",
        "options": ["1 wire", "2 wires", "4 wires", "8 wires"],
        "answer": "2 wires",
        "explanation": "I2C uses only two bidirectional open-drain lines: SDA (Serial Data) and SCL (Serial Clock) with pull-up resistors."
    },
    {
        "id": 193,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "What is the function of a Watchdog Timer (WDT) in a microcontroller system?",
        "options": [
            "Generates PWM waveforms for motors",
            "Automatically resets the microcontroller if firmware freezes or enters an infinite loop",
            "Keeps real-time calendar date and time",
            "Regulates voltage supply from battery"
        ],
        "answer": "Automatically resets the microcontroller if firmware freezes or enters an infinite loop",
        "explanation": "A watchdog timer detects system hangs and recovers the microcontroller by triggering a hardware reset if not refreshed."
    },
    {
        "id": 194,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "What is Pulse Width Modulation (PWM) primarily used for in microcontroller outputs?",
        "options": [
            "Transmitting analog signals using variable duty-cycle digital square waves",
            "Encrypting serial packets",
            "Measuring internal clock jitter",
            "Powering external crystals"
        ],
        "answer": "Transmitting analog signals using variable duty-cycle digital square waves",
        "explanation": "PWM simulates analog output voltages by varying the duty cycle of digital pulses, widely used for motor speed and LED brightness."
    },
    {
        "id": 195,
        "domain": "Core",
        "topic": "Microcontrollers",
        "question": "In the 8051 microcontroller, which timer mode provides an 8-bit auto-reload feature?",
        "options": ["Mode 0", "Mode 1", "Mode 2", "Mode 3"],
        "answer": "Mode 2",
        "explanation": "Mode 2 configures the 8051 timer as an 8-bit auto-reload counter, commonly used for baud rate generation in serial communication."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 5: Communication Systems (IDs 196 - 203)
    # =========================================================================
    {
        "id": 196,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "What is the Nyquist minimum sampling rate for a signal with maximum frequency component fm = 4 kHz?",
        "options": ["4 kHz", "8 kHz", "16 kHz", "2 kHz"],
        "answer": "8 kHz",
        "explanation": "The Nyquist sampling criterion states that fs >= 2 * fm. For fm = 4 kHz, fs >= 2 * 4 = 8 kHz."
    },
    {
        "id": 197,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "Which modulation scheme is more immune to channel amplitude noise?",
        "options": ["Amplitude Modulation (AM)", "Frequency Modulation (FM)", "Double Sideband Suppressed Carrier (DSB-SC)", "Single Sideband (SSB)"],
        "answer": "Frequency Modulation (FM)",
        "explanation": "FM carries information in frequency variations rather than amplitude, allowing limiters to eliminate amplitude noise."
    },
    {
        "id": 198,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "What is the modulation index (m) of an AM wave if the carrier amplitude is 10 V and message amplitude is 8 V?",
        "options": ["0.8", "1.25", "1.8", "0.2"],
        "answer": "0.8",
        "explanation": "Modulation index m = Am / Ac = 8 / 10 = 0.8 (or 80%)."
    },
    {
        "id": 199,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "What is the transmission bandwidth of a standard AM signal with modulating signal bandwidth B?",
        "options": ["B", "2 * B", "4 * B", "B / 2"],
        "answer": "2 * B",
        "explanation": "Standard AM contains two sidebands (USB and LSB), requiring a transmission bandwidth equal to 2 * B."
    },
    {
        "id": 200,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "According to Shannon's Channel Capacity theorem, channel capacity C is given by:",
        "options": ["C = B * log2(1 + S/N)", "C = 2 * B * log2(S/N)", "C = B * (S/N)", "C = log2(1 + S/N) / B"],
        "answer": "C = B * log2(1 + S/N)",
        "explanation": "Shannon-Hartley theorem states C = B * log2(1 + SNR), where B is bandwidth and S/N is signal-to-noise ratio."
    },
    {
        "id": 201,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "Which digital modulation scheme alters the phase of the carrier signal by 180 degrees between binary 0 and binary 1?",
        "options": ["ASK (Amplitude Shift Keying)", "FSK (Frequency Shift Keying)", "BPSK (Binary Phase Shift Keying)", "QAM (Quadrature Amplitude Modulation)"],
        "answer": "BPSK (Binary Phase Shift Keying)",
        "explanation": "BPSK shifts carrier phase between 0 and 180 degrees (pi radians) to represent binary digits."
    },
    {
        "id": 202,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "What is the purpose of a matched filter in a digital communication receiver?",
        "options": [
            "Maximizing the output signal-to-noise ratio in the presence of additive white Gaussian noise",
            "Eliminating carrier phase jitter",
            "Amplifying high-frequency harmonics",
            "Matching antenna impedance to 50 ohms"
        ],
        "answer": "Maximizing the output signal-to-noise ratio in the presence of additive white Gaussian noise",
        "explanation": "A matched filter is the optimal linear filter designed to maximize output peak SNR in AWGN channels."
    },
    {
        "id": 203,
        "domain": "Core",
        "topic": "Communication Systems",
        "question": "What phenomenon occurs when a continuous signal is sampled below the Nyquist rate?",
        "options": ["Quantization error", "Aliasing", "Intersymbol Interference (ISI)", "Thermal distortion"],
        "answer": "Aliasing",
        "explanation": "Under-sampling causes high frequency spectral components to fold back into lower frequencies, resulting in aliasing distortion."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 6: Signals & Systems (IDs 204 - 211)
    # =========================================================================
    {
        "id": 204,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "A continuous-time system is Linear and Time-Invariant (LTI). Its output y(t) to an input x(t) is determined by:",
        "options": [
            "Convolution of input x(t) with system impulse response h(t)",
            "Direct multiplication of x(t) and h(t)",
            "Integration of x(t) only",
            "Fourier inversion of x(t) alone"
        ],
        "answer": "Convolution of input x(t) with system impulse response h(t)",
        "explanation": "The output of any continuous LTI system is given by the convolution integral: y(t) = x(t) * h(t)."
    },
    {
        "id": 205,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "What is the condition for an LTI system with impulse response h(t) to be BIBO (Bounded-Input Bounded-Output) stable?",
        "options": [
            "Integral of |h(t)| from -infinity to +infinity is finite",
            "h(t) must be zero for t < 0",
            "h(t) must be purely real",
            "System transfer function must have poles on the imaginary axis"
        ],
        "answer": "Integral of |h(t)| from -infinity to +infinity is finite",
        "explanation": "BIBO stability requires the impulse response to be absolutely integrable: integral of |h(t)| dt < infinity."
    },
    {
        "id": 206,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "What is the Laplace transform of the unit step function u(t)?",
        "options": ["1", "1 / s", "s", "1 / s^2"],
        "answer": "1 / s",
        "explanation": "L{u(t)} = integral from 0 to infinity of e^(-st) dt = 1/s, for Re(s) > 0."
    },
    {
        "id": 207,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "For a causal discrete-time LTI system to be stable, where must all the poles of its transfer function H(z) lie?",
        "options": [
            "Inside the unit circle in the z-plane (|z| < 1)",
            "Outside the unit circle in the z-plane",
            "On the real axis only",
            "In the left half of the s-plane"
        ],
        "answer": "Inside the unit circle in the z-plane (|z| < 1)",
        "explanation": "A discrete causal LTI system is stable if and only if all poles of H(z) have magnitude strictly less than 1 (inside unit circle)."
    },
    {
        "id": 208,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "What is the Fourier Transform of a Dirac delta function delta(t)?",
        "options": ["0", "1", "2 * pi", "delta(omega)"],
        "answer": "1",
        "explanation": "The Fourier transform of the unit impulse function delta(t) is a constant 1 across all frequencies."
    },
    {
        "id": 209,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "Which property of a signal x(t) implies that x(-t) = -x(t)?",
        "options": ["Even signal", "Odd signal", "Periodic signal", "Causal signal"],
        "answer": "Odd signal",
        "explanation": "An odd (antisymmetric) signal satisfies the condition x(-t) = -x(t) for all t."
    },
    {
        "id": 210,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "What is the Region of Convergence (ROC) of the z-transform of a finite-duration two-sided sequence?",
        "options": ["The entire z-plane except possibly z = 0 and z = infinity", "Inside the unit circle only", "Outside a circle only", "Does not exist"],
        "answer": "The entire z-plane except possibly z = 0 and z = infinity",
        "explanation": "For any finite-duration sequence, the sum has a finite number of terms and converges everywhere except possibly z = 0 or z = infinity."
    },
    {
        "id": 211,
        "domain": "Core",
        "topic": "Signals & Systems",
        "question": "If a signal x(t) is compressed in the time domain by factor a > 1 as x(a*t), what happens in the frequency domain?",
        "options": [
            "It is expanded in frequency and scaled in amplitude by 1/|a|",
            "It is compressed in frequency",
            "Its frequency spectrum remains unchanged",
            "Its phase changes by 90 degrees"
        ],
        "answer": "It is expanded in frequency and scaled in amplitude by 1/|a|",
        "explanation": "Time-frequency scaling theorem states: F{x(at)} = (1/|a|) * X(omega / a). Time compression leads to frequency expansion."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 7: Electronic Devices (IDs 212 - 219)
    # =========================================================================
    {
        "id": 212,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What is the built-in potential barrier voltage of a standard silicon PN junction diode at room temperature?",
        "options": ["0.2 V - 0.3 V", "0.6 V - 0.7 V", "1.1 V - 1.2 V", "2.0 V - 2.5 V"],
        "answer": "0.6 V - 0.7 V",
        "explanation": "Silicon PN junctions have a barrier potential of approximately 0.7 V (Germanium is ~0.3 V)."
    },
    {
        "id": 213,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "In an N-channel MOSFET, conduction between drain and source occurs when gate-to-source voltage Vgs is:",
        "options": [
            "Greater than the threshold voltage Vth",
            "Negative",
            "Zero",
            "Equal to drain voltage Vds"
        ],
        "answer": "Greater than the threshold voltage Vth",
        "explanation": "An enhancement N-MOSFET requires Vgs > Vth to form an inversion channel of electrons between source and drain."
    },
    {
        "id": 214,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What causes the depletion region to form at a PN junction?",
        "options": [
            "Diffusion of majority charge carriers across the junction and subsequent recombination leaving uncompensated ions",
            "External battery connection",
            "Thermal expansion of silicon",
            "Magnetic field generated by electrons"
        ],
        "answer": "Diffusion of majority charge carriers across the junction and subsequent recombination leaving uncompensated ions",
        "explanation": "Electrons and holes diffuse across the junction and recombine, leaving immobile donor and acceptor ions that create an electric field."
    },
    {
        "id": 215,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What is the primary carrier transport mechanism in a BJT's base region?",
        "options": ["Drift", "Diffusion", "Tunneling", "Thermionic emission"],
        "answer": "Diffusion",
        "explanation": "In the base region, majority carriers injected from the emitter travel toward the collector primarily via diffusion across the concentration gradient."
    },
    {
        "id": 216,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "Which semiconductor device exhibits negative differential resistance in its forward characteristic curve?",
        "options": ["Tunnel diode", "Zener diode", "Schottky diode", "Photodiode"],
        "answer": "Tunnel diode",
        "explanation": "Due to quantum mechanical tunneling of electrons, a heavily doped tunnel diode exhibits negative resistance at small forward bias."
    },
    {
        "id": 217,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What is the bandgap energy (Eg) of Silicon at room temperature (300 K)?",
        "options": ["0.67 eV", "1.12 eV", "1.42 eV", "3.2 eV"],
        "answer": "1.12 eV",
        "explanation": "Silicon has an indirect bandgap of approximately 1.12 eV at 300 K (Germanium is 0.67 eV, GaAs is 1.42 eV)."
    },
    {
        "id": 218,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What is the Early effect (base-width modulation) in a BJT caused by?",
        "options": [
            "Increase in reverse bias across the Collector-Base junction narrowing the effective base width",
            "Excessive emitter doping",
            "Thermal runaway in the collector",
            "Saturation of base currents"
        ],
        "answer": "Increase in reverse bias across the Collector-Base junction narrowing the effective base width",
        "explanation": "Increasing collector-base reverse voltage widens the depletion region into the lightly doped base, narrowing effective base width."
    },
    {
        "id": 219,
        "domain": "Core",
        "topic": "Electronic Devices",
        "question": "What type of semiconductor material is formed when pure Silicon is doped with Boron (a trivalent impurity)?",
        "options": ["N-type semiconductor", "P-type semiconductor", "Intrinsic semiconductor", "Compound semiconductor"],
        "answer": "P-type semiconductor",
        "explanation": "Trivalent dopants (like Boron, Gallium) create deficiency of electrons (holes), forming a P-type semiconductor."
    },

    # =========================================================================
    # CORE / ECE DOMAIN - TOPIC 8: Embedded Systems (IDs 220 - 227)
    # =========================================================================
    {
        "id": 220,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "What is a Real-Time Operating System (RTOS) primarily optimized for?",
        "options": [
            "Maximizing graphical user interface rendering speeds",
            "Deterministic predictability and meeting strict timing deadlines",
            "High-throughput multi-user file storage",
            "Compressing audio/video streams"
        ],
        "answer": "Deterministic predictability and meeting strict timing deadlines",
        "explanation": "An RTOS guarantees deterministic task completion within defined time constraints rather than just raw throughput."
    },
    {
        "id": 221,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "What is 'priority inversion' in an embedded real-time multitasking system?",
        "options": [
            "A situation where a high-priority task is blocked by a low-priority task holding a shared resource",
            "When the CPU reverses execution order of instructions",
            "When interrupts are disabled permanently",
            "When memory allocation fails"
        ],
        "answer": "A situation where a high-priority task is blocked by a low-priority task holding a shared resource",
        "explanation": "Priority inversion happens when a low-priority task holds a lock needed by a high-priority task, and is preempted by a medium task."
    },
    {
        "id": 222,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "Which mechanism is used in an RTOS to solve the priority inversion problem?",
        "options": ["Priority Inheritance protocol", "Round Robin scheduling", "Virtual Memory paging", "Spinlocks"],
        "answer": "Priority Inheritance protocol",
        "explanation": "Priority inheritance temporarily raises the priority of the lock-holding low-priority task to that of the waiting highest-priority task."
    },
    {
        "id": 223,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "What is an Interrupt Service Routine (ISR)?",
        "options": [
            "A software routine executed in response to a hardware or software interrupt event",
            "A background thread that compiles code",
            "A battery management driver",
            "A serial terminal simulator"
        ],
        "answer": "A software routine executed in response to a hardware or software interrupt event",
        "explanation": "An ISR is a dedicated callback function invoked by the processor hardware immediately upon receiving an interrupt signal."
    },
    {
        "id": 224,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "Why should an Interrupt Service Routine (ISR) be kept as short and non-blocking as possible?",
        "options": [
            "Because other interrupts and system tasks may be delayed or missed while the ISR executes",
            "Because ISRs cannot execute arithmetic operations",
            "To prevent the crystal oscillator from stopping",
            "Because microcontrollers can only execute 10 instructions in an ISR"
        ],
        "answer": "Because other interrupts and system tasks may be delayed or missed while the ISR executes",
        "explanation": "Long ISRs delay servicing other pending interrupts, increasing interrupt latency and jitter in real-time systems."
    },
    {
        "id": 225,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "What is the purpose of Direct Memory Access (DMA) in embedded systems?",
        "options": [
            "Allows hardware peripherals to transfer data directly to/from memory without continuous CPU intervention",
            "Replaces the central processing unit entirely",
            "Encrypts memory bus transmissions",
            "Acts as a software cache for variables"
        ],
        "answer": "Allows hardware peripherals to transfer data directly to/from memory without continuous CPU intervention",
        "explanation": "DMA offloads high-speed bulk data transfers between peripherals and RAM, freeing the CPU to execute application logic."
    },
    {
        "id": 226,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "Which bus protocol is widely used in automotive embedded systems for robust fault-tolerant communication between ECUs?",
        "options": ["CAN (Controller Area Network)", "I2C", "SPI", "USB 2.0"],
        "answer": "CAN (Controller Area Network)",
        "explanation": "CAN bus provides robust, differential, message-based communication with hardware error confinement across automotive vehicles."
    },
    {
        "id": 227,
        "domain": "Core",
        "topic": "Embedded Systems",
        "question": "What is a 'critical section' in embedded multi-threaded code?",
        "options": [
            "A block of code accessing shared resources that must not be concurrently executed by multiple threads",
            "The memory segment where the bootloader is stored",
            "The physical CPU silicon core",
            "The section of code that initializes the system clock"
        ],
        "answer": "A block of code accessing shared resources that must not be concurrently executed by multiple threads",
        "explanation": "A critical section accesses shared data and requires mutual exclusion (via mutex, semaphore, or disabling interrupts) to prevent race conditions."
    }
]
