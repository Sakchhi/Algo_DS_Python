# Array Structure
- Multiple sequential elements
- Stored in contiguous bytes of memory
- Allows random access to individual elements by subscript
- Arrays vs List
    - Array has limited operations like creation, reading, writing; List has large number of operations
    - Array remains fixed in size, List size can change as elements are added and deleted
    
### Python list vs Array ADT
- Python list implements Array ADT with some changes
    - Array created with size larger than requested
    - Elements assigned in contiguous cells
- When appending elements, elements are usually appended until underlying array capacity is full
    - Post which, new Array is created, elements copied, new elements appended, old array destroyed and new array assigned as DS for list
- For insertion at given index, elements are shifted to make room for insertion; similarly for deletion
- Slicing doesn't affect original list but copies relevant references to new list

## 2-D Array