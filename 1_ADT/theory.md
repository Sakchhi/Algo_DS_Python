# Abstract Data Types

## Terms
- Algorithm
- **Data type** -- given type along with a collection of operations for manipulating values of the given type
    - Simple data types
    - Complex data types - Multiple components consisting of simple types or other complex types, *eg strings, lists, objects, dictionaries, etc*
    - User-defined types
- **Abstraction** -- Mechanism for separating the properties of an object and restricting the focus to those relevant in the current context
    - **Procedural Abstraction** -- Use of a function or method knowing what it does but ignoring how it's accompalished
    - **Data abstraction** -- Separation of the properties of a data type (its values and operations) from the implementation of that data type
- **Abstract Data Type** -- Programmer-defined data type that specifies a set of data values and a collection of well-defined operations that can be performed on those values.
    - Independent of their implementation
    - Achieved by enforcing interaction through an *interface*
    - Four types of operations:
        - Constructors
        - Accessors
        - Mutators
        - Iterators
    - **Simple ADT** -- Composed of a single or several individually named data fields such as those used to represent a date or a rational number
    - **Complex ADTs** -- Composed of a collection of data values such as Python list or dictionary. Implemented using a particular *data structure*
- **Collection** -- Group of values with no implied organization or relationship between the individual values
- **Container** -- Any data structure or abstract data type that stores and organizes a collection -- *elements, empty*
- **Sequence** -- Container in which elements are arranged in linear order from front to back