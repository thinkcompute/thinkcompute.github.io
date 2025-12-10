(ch-part-2-exercises)=
# Part 4: Exercises

`````{exercise}
:label: part-4-ex-1

The variable `my_list` contains a list of ten integer number from 0 to 9. Study the execution of the following function when it is called as `algorithm(my_list, 0)`:

```python
def algorithm(a_list, pos):
    if pos >= len(a_list):
        return a_list
    else:
        common_division = pos / 2
        floor_division = pos // 2
        if floor_division < common_division:
            a_list.remove(a_list[floor_division])

        return algorithm(a_list, pos + 1)
```

````{solution} part-4-ex-1
:label: part-4-ex-1-sol
:class: dropdown

The recursive function `algorithm` modifies the list in input according to the particular position in the list specified, until all the items in the list have been processed. The first call starts working on the very first item of the list, thus starting with the instructions in the `else` block - unless the initial list is empty (in this case, the empty list will be returned as such).

The instructions in the `else` check if the position (i.e. `pos`) is an odd number and, in that case, it modify the list removing the first instance of the item in position `pos // 2`. Independently from the fact that the execution remove an item or not from the input list, the last step execute a recursive step calling the function `algorithm` passing the list (modified or not) and a subsequent position (i.e. `pos + 1`) as input, and returns the value returned by the recursive execution.

For instance, the following call

```python
my_list = [0, 0, 0, 1, 0, 9, 8, 2, 0, 7]
result = algorithm(my_list, 0)
print(result)
```

prints on screen the list `[1, 0, 9, 8, 2, 0, 7]`.

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-modify_list.py>`. You can run it executing the command `python ex-und-modify_list.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-2

The variable `my_mat_string` contains a string of ten 0-9 digits (e.g. `"0000123456"`). Study the execution of the following functions when they are called as follows: `f(my_mat_string)`.

```python
def f(mat_string):
    c = 0
    lst = list()

    for chr in mat_string:
        n = int(chr)
        lst.append(n)
        if n / 2 != n // 2:
            c = c + 1

    return g(lst, c)


def g(mat_list, c):
    if c <= 0 or len(mat_list) == 0:
        return 0
    else:
        v = 0
        result = list()

        for i in mat_list:
            if v > 0:
                result.append(i)
            if i > 0 and v == 0:
                v = i

        return v + g(result, c - 1)
```
````{solution} part-4-ex-2
:label: part-4-ex-2-sol
:class: dropdown

The function `f` transform the input string in another data structure, i.e. a list of integers (created casting the digit character into the related number) and counts the number of odd numbers the list contains (using the variable `c`). The function `g`, that is called by the function `f`, is a recursive function.

The instructions that are executed by the function `g`, in case the input list is not empty and the input number is greater than 0, creates a new list. In particular, it iterates over all the numbers of the input list. At every iteration, the current number considered (i.e. `i`) is added to the new list if the variable `v`, set to 0 before starting the for each loop, is greater than 0. In addition, the variable `v` is updated with the value of the variable `i` during the first iteration in which `i` assumes a value greater than 0. Thus, the for each loop create a sublist of the original input list that includes all the elements in the input list starting from the item following the one considered when `v` is modified.

Finally, the recursive step is executed, passing the new list created and `c - 1` as input, and the result is summed to the value specified in the variable `v` and then returned.

For instance, the following call

```python
my_mat_string = "0001098207"
result = f(my_mat_string)
print(result)
```

prints on screen the number `18`.

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-number_from_matriculation.py>`. You can run it executing the command `python ex-und-number_from_matriculation.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-3

The Euclidean algorithm is a method for computing the greatest common divisor (GCD) of two integers, i.e. the largest number that divides them both without a remainder. 

The Euclidean algorithm is based on the principle that the GCD of two numbers does not change if the larger number is replaced by its difference with the smaller number. For example, 3 is the GCD of 15 and 6 (as 15 = 3 × 5 and 6 = 3 × 2), and the same number 3 is also the GCD of 6 and 15 − 6 = 9. Since this replacement reduces the larger of the two numbers, repeating this process gives smaller pairs of numbers successively until the two numbers become equal. When that occurs, that number is the GCD of the original two numbers:

1. GCD(15, 6) = GCD(15-6=9, 6)
2. GCD(9, 6) = GCD(9-6=3, 6)
3. GCD(3, 6) = GCD(3, 6-3)
4. GCD(3, 3) = 3

Write a recursive algorithm in Python – `def euclidean(r, s)` – which takes in input two integer numbers `s` and `r` greater than zero, and returns their greatest common divisor. Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-3
:label: part-4-ex-3-sol
:class: dropdown

```python
# Test case for the function
def test_euclidean(r, s, expected):
    result = euclidean(r, s)
    
    if result == expected:
        return True
    else:
        return False


# Code of the function
def euclidean(r, s):
    if r == s:
        return r
    elif r < s:
        return euclidean(r, s - r)
    else:
        return euclidean(r - s, s)

        
# Tests
print(test_euclidean(1, 1, 1))
print(test_euclidean(1, 2, 1))
print(test_euclidean(1, 3, 1))
print(test_euclidean(3, 2, 1))
print(test_euclidean(3, 3, 3))
print(test_euclidean(3, 9, 3))
print(test_euclidean(15, 6, 3))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-euclidean.py>`. You can run it executing the command `python ex-dev-euclidean.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-4

Write down, using a **divide and conquer approach**, the body of the following Python function:

```
def sum(number_list) 
```

The function takes a list of numbers as input and returns their sum. The use of any form of iteration (e.g. for each and while loops) is prohibited. Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-4
:label: part-4-ex-4-sol
:class: dropdown

```python
# Test case for the function
def test_sum(number_list, expected):
    result = sum(number_list)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def sum(number_list):
    list_len = len(number_list)
    
    if list_len == 0:
        return 0
    elif list_len == 1:
        return number_list[0]
    else:
        mid = list_len // 2
        return sum(number_list[0:mid]) + sum(number_list[mid:list_len])


# Tests
print(test_sum([9, 9, 9], 27))
print(test_sum([8, 5, 9, 8, 3, 6], 39))
print(test_sum([], 0))
print(test_sum([42], 42))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-sum.py>`. You can run it executing the command `python ex-dev-sum.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-5

Implement in Python the *binary search algorithm* – i.e. the recursive function `def binary_search(item, ordered_list, start, end)`. 

It takes an item to search (i.e. `item`), an ordered list and starting and ending positions in the list as input. It returns the position of `item` in the list, if it is in the list, and `None` otherwise. The binary search first checks whether the middle item of the list between `start` and `end` (inclusive) is equal to `item`, and returns its position if so. Otherwise, if the middle item is less than `item`, the algorithm continues the search in the part of the list that follows the middle item. Instead, in case the middle item is greater than `item`, the algorithm continues the search in the part of the list that precedes the middle item. Accompany the implementation of the function with the appropriate test cases. 

As supporting material, Fekete and blinry released a nonverbal definition of the algorithm {cite}`fekete_binary_2018`, which is useful to understand the rationale of the binary search steps.

````{solution} part-4-ex-5
:label: part-4-ex-5-sol
:class: dropdown

```python
# Test case for the function
def test_binary_search(item, ordered_list, start, end, expected):
    result = binary_search(item, ordered_list, start, end)
    if expected == result:
        return True
    else:
        return False


def binary_search(item, ordered_list, start, end):
    if len(ordered_list) > 0 and start <= end:
        mid = (start + end) // 2
        mid_item = ordered_list[mid]
        if item == mid_item:
            return mid
        elif mid_item < item:
            return binary_search(item, ordered_list, mid + 1, end)
        else:
            return binary_search(item, ordered_list, start, mid - 1)


# Tests
print(test_binary_search(3, [1, 2, 3, 4, 5], 0, 4, 2))
print(test_binary_search("Denver", ["Alice", "Bob", "Catherine", "Charles"], 0, 3, None))
print(test_binary_search("Harry", ["Harry", "Hermione", "Ron"], 0, 2, 0))
print(test_binary_search("Harry", [], 0, 0, None))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-binary_search.py>`. You can run it executing the command `python ex-binary_search.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-6

Implement in Python the *partition* algorithm – i.e. the non-recursive function `def partition(input_list, start, end, pivot_position)`. 

It takes a list and the positions of the first and last elements in the list to consider as inputs. It redistributes all the elements of a list having position included between `​start` and `​end` on the right of the pivot value `input_list[pivot_position]` if they are greater than it, and on its left otherwise. Also, the algorithm returns the new position where the pivot value is now stored. For instance, considering ​​`my_list = list(["The Graveyard Book", "Coraline", "Neverwhere", "Good Omens", "American Gods"])`, the execution of `partition(my_list, 1, 4, 1)` changes ​my_list as follows: ​`list(["The Graveyard Book", "American Gods", "Coraline", "Neverwhere", "Good Omens"])` and `2` will be returned (i.e. the new position of `"Coraline"`). Note that `"The Graveyard Book"` has not changed its position in the previous execution since it was not included between the specified start and end positions (i.e. `1` and `4` respectively). Accompany the implementation of the function with the appropriate test cases. 

As supporting material, Ang [recorded a video](https://www.youtube.com/watch?v=MZaf_9IZCrc) which is useful to understand the rationale of the partition steps.

````{solution} part-4-ex-6
:label: part-4-ex-6-sol
:class: dropdown

```python
# Test case for the function
def test_partition(input_list, start, end, pivot_position, expected):
    p_value = input_list[pivot_position]
    result = partition(input_list, start, end, pivot_position)
    output = expected == result and p_value == input_list[result]

    for item in input_list[0:result]:
        output = output and item <= p_value
    for item in input_list[result + 1:len(input_list)]:
        output = output and item >= p_value

    return output


# Code of the function
def partition(input_list, start, end, pivot_position):
    pivot_value = input_list[pivot_position]

    swap_index = start - 1
    for index in range(start, end + 1):
        if input_list[index] < pivot_value:
            swap_index += 1
            if swap_index == pivot_position:
                pivot_position = index
            swap(input_list, swap_index, index)

    new_pivot_position = swap_index + 1
    swap(input_list, pivot_position, new_pivot_position)

    return new_pivot_position


def swap(input_list, old_index, new_index):
    cur_value = input_list[old_index]
    input_list[old_index] = input_list[new_index]
    input_list[new_index] = cur_value


# Run tests
print(test_partition([1, 2, 3, 4, 5], 0, 4, 0, 0))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 0, 2))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 2, 1))
print(test_partition([7, 5, 3, 1, 4], 0, 4, 4, 2))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 1, 8))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 0, 0))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 3, 6))
print(test_partition([1, 2, 2, 3, 9, 8, 4], 1, 2, 1, 1))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-partition.py>`. You can run it executing the command `python ex-partition.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-7

Implement in Python the divide and conquer *quicksort* algorithm – i.e. the recursive `def quicksort(input_list, start, end)`​. 

It takes a list and the positions of its first and last elements as inputs. Then, it calls `partition(input_list, start, end, start)` (defined in the previous exercise) to partition the input list into two slices. Finally, it executes itself recursively on the two partitions (neither of which includes the pivot value since it has already been correctly positioned through the execution of partition). In addition, define the base case of the algorithm appropriately to stop if needed before running the partition algorithm. Accompany the implementation of the function with the appropriate test cases. 

As supporting material, Fekete and blinry released a nonverbal definition of the algorithm {cite}`fekete_kvick_2018`, which is useful to understand the rationale of the quicksort.

````{solution} part-4-ex-7
:label: part-4-ex-7-sol
:class: dropdown

```python
# Test case for the function
def test_quicksort(input_list, start, end, expected):
    result = quicksort(input_list, start, end)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def quicksort(input_list, start, end):
    if start < end:
        pivot_position = partition(input_list, start, end, start)
        quicksort(input_list, start, pivot_position - 1)
        quicksort(input_list, pivot_position + 1, end)
    return input_list

def partition(input_list, start, end, pivot_position):
    pivot_value = input_list[pivot_position]

    swap_index = start - 1
    for index in range(start, end + 1):
        if input_list[index] < pivot_value:
            swap_index += 1
            if swap_index == pivot_position:
                pivot_position = index
            swap(input_list, swap_index, index)

    new_pivot_position = swap_index + 1
    swap(input_list, pivot_position, new_pivot_position)

    return new_pivot_position

def swap(input_list, old_index, new_index):
    cur_value = input_list[old_index]
    input_list[old_index] = input_list[new_index]
    input_list[new_index] = cur_value
    

# Run tests
print(test_quicksort([1], 0, 0, [1]))
print(test_quicksort([1, 2, 3, 4, 5, 6, 7], 0, 6, [1, 2, 3, 4, 5, 6, 7]))
print(test_quicksort([3, 4, 1, 2, 9, 8, 2], 0, 6, [1, 2, 2, 3, 4, 8, 9]))
print(test_quicksort(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"], 0, 4,
                     ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-quicksort.py>`. You can run it executing the command `python ex-quicksort.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-8

Consider the following function:

```python
def rin(g_name, f_name, idx):
    result = []

    if len(g_name) > 0:
        if g_name[0] in f_name:
            result.append(idx)
        
        idx = idx + 1
        result.extend(rin(g_name[1:len(g_name)], f_name, idx))

    return result 
```

The variable `my_g_name` contains the string with your given name in lower case (e.g. `"john"`), and `my_f_name` contains the string with your family name in lower case (e.g. `"doe"`). What is the value returned by calling the function sc as shown as follows: 

```python
rin(my_g_name, my_f_name, 0)
```

````{solution} part-4-ex-8
:label: part-4-ex-8-sol
:class: dropdown

The function `rin` is an recursive recursive function that reduces the characters of the given name at each recursive call, removing the first one. In particular, in each call (in case the `g_name` input parameter is not empty) it adds the value of `idx` to the result list in case the first character of `g_name` is also included in `f_name`. The final list returned will be a list of non-negative integers.

For instance, executing the function as follows

```python
rin("john", "doe", 0)
```

returns the list `[1]`.

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-given_and_family_names.py>`. You can run it executing the command `python ex-und-given_and_family_names.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-9

Consider the following function:

```python
def rsel(full_name, mat_string):
    uniq = []
    for c in full_name:
        if c not in uniq:
            uniq.append(c)
    
    r = []
    i = len(mat_string) // 2
    if i > 0:
        n = int(mat_string[i])
        if n < len(uniq):
            r.append(uniq[n])
            new_full_name = full_name[0:n] + full_name[n+1:len(full_name)]
            new_mat_string = mat_string[0:n] + mat_string[n+1:len(mat_string)]
            r.extend(rsel(new_full_name, new_mat_string))
    
    return r
```

The variable `my_mat_string` contains the string of all ten numbers of a matriculation number (e.g. `"0235145398"`), and `my_full_name` is a string of a full name, all in lowercase with no spaces (e.g. `"johndoe"`). Write down the value returned by calling the function `rsel` as shown as follows: 

```python
rsel(my_full_name, my_mat_string)
```

````{solution} part-4-ex-9
:label: part-4-ex-9-sol
:class: dropdown

The function `rsel` is a recursive function that, at every call, reduce both the input parameters of one character. In particular, it identifies all the unique letters in the given input string `full_name`, it sees if the `mat_string` contains at least two characters, and then it appends, to the list to be returned as result, the character in the list of unique letters that is specified in the position specified by the first digit number after the first half of the matricutation string if such position is indeed present in the list of unique letters.

For instance, executing the function as follows

```python
rsel("johndoe", "0235145398")
```

returns the list `["d", "e"]`.

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-name_and_matriculation.py>`. You can run it executing the command `python ex-und-name_and_matriculation.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-10

Consider the following function:

```python
def cnt(mat_string):
    result = 0

    if len(mat_string) > 0:
        n = int(mat_string[0])

        if n % 2 == 0:
            return 1 + cnt(mat_string[1:len(mat_string)])
        else:
            return -1 + cnt(mat_string[1:len(mat_string)])
    
    return result
```

In the function above, the operation `%` returns the remainder of the division between two numbers. 

The variable `my_mat_string` contains the string of a 10-digit matriculation number (e.g. `"0000123456"`). Write down the value returned by calling the function `cnt` as shown as follows: 

```python
cnt(my_mat_string)
```

````{solution} part-4-ex-10
:label: part-4-ex-10-sol
:class: dropdown

The function `cnt` is an recursive function that, at every call, reduces the input of one character. In particular, it adds one to the final result returned if the number is even, while it subtracts one unit otherwise, before calling the recursive step.

For instance, executing the function as follows

```python
cnt("0000123456")
```

returns the number `4`.

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-und-binary_sum_matriculation.py>`. You can run it executing the command `python ex-und-binary_sum_matriculation.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-11

Write an extension of the multiplication function introduced in [Chapter "Recursion"](./08-recursion.md#py-recursive-multiplication), i.e. `def multiplication(int_1, int_2, solution_dict)`, by using a dynamic programming approach. This new function takes as input two integers to multiply and a dictionary with solutions of multiplications between numbers. The function returns the result of the multiplication and, at the same time, modifies the solution dictionary, adding additional solutions when found.  

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-11
:label: part-4-ex-11-sol
:class: dropdown

```python
# Test case for the function
def test_multiplication(int_1, int_2, solution_dict, expected):
    result = multiplication(int_1, int_2, solution_dict)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def multiplication(int_1, int_2, solution_dict):
    if int_1 < int_2:
        mult_pair = (int_1, int_2)
    else:
        mult_pair = (int_2, int_1)

    if mult_pair not in solution_dict:
        if int_2 == 0:
            solution_dict[mult_pair] = 0
        else:
            solution_dict[mult_pair] = int_1 + multiplication(int_1, int_2 - 1, solution_dict)

    return solution_dict[mult_pair]


# Tests
my_dict = {}
print(test_multiplication(0, 0, my_dict, 0))
print(test_multiplication(1, 0, my_dict, 0))
print(test_multiplication(5, 7, my_dict, 35))
print(test_multiplication(7, 7, my_dict, 49))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dp_multiplication.py>`. You can run it executing the command `python ex-dp_multiplication.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-12

Write the body of the Python function `def depth_first_visit(node)` that takes the root node of a tree as input and returns the list of all its nodes ordered according to a depth-first visit. The depth-first visit proceeds as indicated in {numref}`depth-first-visit`, where the numbers indicate the order in which the nodes should be visited.

```{figure} images/ex-depth-first-visit.png
---
name: depth-first-visit
---
Depth-first visit. Photo by Alexander Drichel, source: [Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search#/media/File:Depth-first-tree.svg).
```

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-12
:label: part-4-ex-12-sol
:class: dropdown

```python
from anytree import Node


# Test case for the function
def test_depth_first_visit(node, expected):
    result = depth_first_visit(node)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def depth_first_visit(node):
    result = list()
    depth_first_visit_recursive(node, result)
    return result


def depth_first_visit_recursive(node, list):
    list.append(node)
    for child in node.children:
        depth_first_visit_recursive(child, list)


# Tests
n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n5 = Node(5, n3)
n6 = Node(6, n2)
n7 = Node(7, n1)
n8 = Node(8, n1)
n9 = Node(9, n8)
n10 = Node(10, n9)
n11 = Node(11, n9)
n12 = Node(12, n8)
print(test_depth_first_visit(n1, [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-depth_first_visit.py>`. You can run it executing the command `python ex-dev-depth_first_visit.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-13

Write in Python a function `def breadth_first_visit(root_node)` that does not use any recursion. This function takes a tree's root node and returns a list of all nodes in breadth-first order. The breadth-first order considers all the nodes of the first level, then those ones of the second level, and so forth. For instance, considering the nodes created in the [listing](./11-trees.md#py-tree) in [Chapter "Organising information: trees"](./11-trees.md), the function called on the node book should return the following list: 

```python
[book, chapter_1, chapter_2, text_8, paragraph_1, paragraph_2, paragraph_3, text_7, text_1, quotation_1, text_3, quotation_2, text_5, text_6, text_2, text_4]
```

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-13
:label: part-4-ex-13-sol
:class: dropdown

```python
from anytree import Node
from collections import deque


# Test case for the function
def test_breadth_first_visit(root_node, expected):
    result = breadth_first_visit(root_node)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def breadth_first_visit(root_node):
    result = list()
    to_visit = deque()
    to_visit.append(root_node)

    while to_visit:
        node_to_visit = to_visit.popleft()
        result.append(node_to_visit)
        to_visit.extend(node_to_visit.children)

    return result


# Tests
book = Node("book")
chapter_1 = Node("chapter1", book)
chapter_2 = Node("chapter2", book)
paragraph_1 = Node("paragraph1", chapter_1)
text_1 = Node("text1", paragraph_1)
quotation_1 = Node("quotation1", paragraph_1)
text_2 = Node("text2", quotation_1)
text_3 = Node("text3", paragraph_1)
quotation_2 = Node("quotation2", paragraph_1)
text_4 = Node("text4", quotation_2)
paragraph_2 = Node("paragraph2", chapter_1)
text_5 = Node("text5", paragraph_2)
paragraph_3 = Node("paragraph3", chapter_1)
text_6 = Node("text6", paragraph_3)
text_7 = Node("text7", chapter_2)
text_8 = Node("text8", book)
bfv = [book,
       chapter_1, chapter_2, text_8,
       paragraph_1, paragraph_2, paragraph_3, text_7,
       text_1, quotation_1, text_3, quotation_2, text_5, text_6,
       text_2, text_4]
print(test_breadth_first_visit(book, bfv))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-depth_first_visit.py>`. You can run it executing the command `python ex-depth_first_visit.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-14

Write in Python a recursive version of the function defined in the {numref}´part-4-ex-13´.

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-14
:label: part-4-ex-14-sol
:class: dropdown

```python
from anytree import Node
from collections import deque


# Test case for the function
def test_breadth_first_visit(root_node, expected):
    result = breadth_first_visit(root_node)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def breadth_first_visit(root_node):
    result = list()

    if len(root_node.ancestors) == 0:  # It is the first call
        root_node.parent = Node(deque())

    queue = root_node.root.name
    result.append(root_node)
    queue.extend(root_node.children)

    if len(queue) > 0:
        result.extend(breadth_first_visit(queue.popleft()))
    else:
        root_node.root.children = ()

    return result


# Tests
book = Node("book")
chapter_1 = Node("chapter1", book)
chapter_2 = Node("chapter2", book)
paragraph_1 = Node("paragraph1", chapter_1)
text_1 = Node("text1", paragraph_1)
quotation_1 = Node("quotation1", paragraph_1)
text_2 = Node("text2", quotation_1)
text_3 = Node("text3", paragraph_1)
quotation_2 = Node("quotation2", paragraph_1)
text_4 = Node("text4", quotation_2)
paragraph_2 = Node("paragraph2", chapter_1)
text_5 = Node("text5", paragraph_2)
paragraph_3 = Node("paragraph3", chapter_1)
text_6 = Node("text6", paragraph_3)
text_7 = Node("text7", chapter_2)
text_8 = Node("text8", book)
bfv = [book,
       chapter_1, chapter_2, text_8,
       paragraph_1, paragraph_2, paragraph_3, text_7,
       text_1, quotation_1, text_3, quotation_2, text_5, text_6,
       text_2, text_4]
print(test_breadth_first_visit(book, bfv))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-depth_first_visit_recursive.py>`. You can run it executing the command `python ex-dev-depth_first_visit_recursive.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-15

A **decision tree** is a flowchart-like structure in which each internal node represents a test on an attribute (e.g. whether a coin flip comes up heads or tails), each branch represents the outcome of the test, and each leaf node represents a class label (i.e., a decision taken after computing all attributes). The paths from root to leaf represent classification rules. An example of a decision tree is shown in {numref}`decision`.

```{figure} images/ex-decision.png
---
name: decision
---
Decision tree.
```

The decision tree above allows one to check whether a given number (identified by the variable `attribute`) is equal to 0. For checking this, supposing to execute such a decision tree passing the number 3 as input, one has (a) to start from the root, (b) to execute the condition (i.e. 3 < 0), (c) to follow the related branch (i.e. *false*), and (d) to repeat again the process if we arrived in an inner node or (e) to return the result if we arrived in a leaf node.

As shown in the figure, in a decision tree, each internal node always has two children: the left one is reached when the condition the internal node specifies is *true*, while the right one is reached when the condition the internal node specifies is *false*.

Write an algorithm in Python – `def exec_dt(decision, attribute)` – which takes in input a tree `decision` (which is represented by the root node of the tree defined as an object of the class anytree.Node) describing a decision tree, in which the name of each non-leaf node in the tree is a Python function – it means that we can see the node name as a function that can be executed by passing an input, e.g. considering the node `n`, we can call the function specified as its name passing the input between parenthesis, as usual: `n.name(56)`. Each Python function, to execute using `attribute` as input, returns either `True` or `False` if the condition defined by that function is satisfied or is not satisfied, respectively. The algorithm returns the leaf node reached by executing the decision tree with the value in `attribute`.

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-15
:label: part-4-ex-15-sol
:class: dropdown

```python
from anytree import Node


# Test case for the function
def test_exec_td(decision, attribute, expected):
    result = exec_td(decision, attribute)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def exec_td(decision, attribute):
    if decision.children:
        if decision.name(attribute):
            return exec_td(decision.children[0], attribute)
        else:
            return exec_td(decision.children[1], attribute)
    else:
        return decision


# Tests
attr_equal = "attribute is equal to 0"
attr_not_equal = "attribute is not equal to 0"

root = Node(lambda x: x < 0)
root_left = Node(attr_not_equal, root)
root_right = Node(lambda x: x > 0, root)
root_right_left = Node(attr_not_equal, root_right)
root_right_right = Node(attr_equal, root_right)

print(test_exec_td(root, 0, root_right_right))
print(test_exec_td(root, 5, root_right_left))
print(test_exec_td(root, -10, root_left))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-decision_tree.py>`. You can run it executing the command `python ex-dev-decision_tree.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-16

A binary search tree is a binary tree data structure where each node may have at most two children, and the value of each node is greater than (or equal to) all the values in the respective node's left subtree and less than (or equal to) the ones in its right subtree. It can be built, recursively following an approach which recalls the binary search strategy, starting from a list of ordered items (e.g. a list of integers), where each item becomes a node of a tree, as shown in {numref}`bst`.

```{figure} images/ex-bst.png
---
name: bst
---
Example of a binary search tree.
```

As a reminder, the binary search strategy first checks if the middle item of a list is equal to the item to search for and, in case this is not true, it continues to analyse the part of the list that either precedes or follows the middle item if it is greater than or less than the item to search.

Write a recursive algorithm in Python – `def create_bst(ordered_list, parent)` – which takes in input an ordered list of integers ordered_list and a parent node `parent`, and returns the root node of the binary search tree created from the input list. In the first call, the function is run passing `None` as input for the second parameter `parent`, e.g. 

```
create_bst([0, 1, 1, 2, 3, 5, 8, 13], None)
```

and returns the binary search tree (i.e. its root node) shown in the example above.

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-16
:label: part-4-ex-16-sol
:class: dropdown

```python
from anytree import Node, RenderTree

# Test case for the function
def test_create_bst(ordered_list, parent, expected):
    result = create_bst(ordered_list, parent)
    
    if str(RenderTree(result)) == str(RenderTree(expected)):
        return True
    else:
        return False


# Code of the function
def create_bst(ordered_list, parent):
    cur_len = len(ordered_list)

    if cur_len == 1:
        return Node(ordered_list[0], parent)
    elif cur_len > 1:
        mid = cur_len // 2
        
        r = Node(ordered_list[mid], parent)

        create_bst(ordered_list[:mid], r)
        create_bst(ordered_list[mid+1:], r)
        
        return r


# Tests
print(test_create_bst([9], None, Node(9)))

r1 = Node(5)
Node(1, r1)
Node(9, r1)
print(test_create_bst([1, 5, 9], None, r1))

r2 = Node(5)
r2_1 = Node(3, r2)
Node(1, r2_1)
r2_2 = Node(9, r2)
Node(7, r2_2)
print(test_create_bst([1, 3, 5, 7, 9], None, r2))

r3 = Node(3)
r3_1 = Node(1, r3)
r3_1_1 = Node(1, r3_1)
Node(0, r3_1_1)
Node(2, r3_1)
r3_2 = Node(8, r3)
Node(5, r3_2)
Node(13, r3_2)
print(test_create_bst([0, 1, 1, 2, 3, 5, 8, 13], None, r3))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-binary_search_tree.py>`. You can run it executing the command `python ex-dev-binary_search_tree.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-17

Propose some variation to the [implementation of the peg solitaire exercise](./12-backtracking.md#py-solve) in [Chapter "Backtracking algorithms"](./12-backtracking.md) to make it more efficient – in particular, avoiding unsuccessful configurations if they have already been encountered previously while looking for a solution.

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-17
:label: part-4-ex-17-sol
:class: dropdown

```python
from anytree import Node
from collections import deque


# Test case for the algorithm
def test_solve(pegs, holes, last_move, no_win_list, expected):
    result = solve(pegs, holes, last_move, no_win_list)
    if expected == result.name["in"] and len(pegs) == 1:
        return True
    else:
        return False


# Code of the algorithm
def solve(pegs, holes, last_move, no_win):
    result = None

    if pegs not in no_win:
        no_win.append(set(pegs))

        if len(pegs) == 1 and (5, 1) in pegs:  # leaf-win base case
            result = last_move
        else:
            last_move.children = valid_moves(pegs, holes)

            if len(last_move.children) == 0:  # leaf-lose base case
                undo_move(last_move, pegs, holes)  # backtracking
            else:  # recursive step
                possible_moves = deque(last_move.children)

                while result is None and len(possible_moves) > 0:
                    current_move = possible_moves.pop()
                    apply_move(current_move, pegs, holes)
                    result = solve(pegs, holes, current_move, no_win)

                if result is None:
                    undo_move(last_move, pegs, holes)  # backtracking
    else:
        undo_move(last_move, pegs, holes)  # backtracking

    return result


def create_board():
    initial_hole = (5, 1)
    holes = set()
    holes.add(initial_hole)

    pegs = set([
        (1, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (1, 2), (4, 2),
        (1, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
        (1, 5), (4, 5)
    ])

    return pegs, holes


def valid_moves(pegs, holes):
    result = list()

    for x, y in holes:
        if (x-1, y) in pegs and (x-2, y) in pegs:
            result.append(Node({"move": (x-2, y), "in": (x, y), "remove": (x-1, y)}))
        if (x+1, y) in pegs and (x+2, y) in pegs:
            result.append(Node({"move": (x+2, y), "in": (x, y), "remove": (x+1, y)}))
        if (x, y-1) in pegs and (x, y-2) in pegs:
            result.append(Node({"move": (x, y-2), "in": (x, y), "remove": (x, y-1)}))
        if (x, y+1) in pegs and (x, y+2) in pegs:
            result.append(Node({"move": (x, y+2), "in": (x, y), "remove": (x, y+1)}))

    return result


def apply_move(node, pegs, holes):
    move = node.name
    old_pos = move.get("move")
    new_pos = move.get("in")
    eat_pos = move.get("remove")

    pegs.remove(old_pos)
    holes.add(old_pos)

    pegs.add(new_pos)
    holes.remove(new_pos)

    pegs.remove(eat_pos)
    holes.add(eat_pos)


def undo_move(node, pegs, holes):
    move = node.name
    old_pos = move.get("move")
    new_pos = move.get("in")
    eat_pos = move.get("remove")

    pegs.add(old_pos)
    holes.remove(old_pos)

    pegs.remove(new_pos)
    holes.add(new_pos)

    pegs.add(eat_pos)
    holes.remove(eat_pos)


# Tests
pegs, holes = create_board()
print(test_solve(pegs, holes, Node("start"), list(), (5, 1)))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-solve_dp.py>`. You can run it executing the command `python ex-solve_dp.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-18

*AtariGo* is a simplified version of Go. Its rules are pretty simple. Two teams, Black and White, take turns placing a stone (game piece) of their own colour on a vacant point (intersection) of the grid on the board. Once placed, stones do not move. A vacant point adjacent to a stone is called a liberty for that stone. Connected stones formed a group and shared their liberties. A stone or group with no liberties is captured. Black plays first. The first team to capture anything wins.

Suppose you want to develop software that can play AtariGo on a 4x4 board, as shown in {numref}`go`, already populated with some stones.

```{figure} images/ex-go.png
---
name: go
---
An example of a small Go board.
```

Suppose we use tuples to define every position in the board, as  shown as follows:

```
(0, 0) (1, 0) (2, 0) (3, 0)
(0, 1) (1, 1) (2, 1) (3, 1)
(0, 2) (1, 2) (2, 2) (3, 2)
(0, 3) (1, 3) (2, 3) (3, 3)
```

One of the functions to implement returns the set of board positions that are not occupied by any stone and that do not result in the stone being immediately captured if placed. Supposing White has to play on the board in the figure, such a function would return the set containing the tuples `(0, 0)`, `(1, 0)` and `(0, 1)` – but not `(3, 3)` since if White places a stone there it will be immediately captured.

Write a function in Python – `def get_good_white_moves(white, black)` – that takes in input the set of tuples identifying the stones placed in the 4x4 board in the previous turns by the two players (`white` and `black`, respectively) and that returns the set of all the tuples identifying possible places where White can put its stone in the current turn, according to the rules mentioned above. As a simplification, avoid checking the liberties of groups of White stones.

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-18
:label: part-4-ex-18-sol
:class: dropdown

# Test case for the function
def test_get_good_white_moves(white, black, expected):
    result = get_good_white_moves(white, black)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def get_good_white_moves(white, black):
    result = set([
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3)
    ])
    result.difference_update(white)
    result.difference_update(black)

    for x, y in set(result):
        if not have_freedom((x - 1, y), black) and not have_freedom((x + 1, y), black) and \
                not have_freedom((x, y - 1), black) and not have_freedom((x, y + 1), black):
            result.remove((x, y))

    return result


def have_freedom(t, black):
    return 0 <= t[0] <= 3 and 0 <= t[1] <= 3 and t not in black


# Tests
print(test_get_good_white_moves(
    {(1, 1), (0, 2), (0, 3), (1, 0)},
    {(2, 0), (2, 1), (3, 1), (2, 2), (2, 3)},
    {(0, 0), (0, 1), (1, 2), (1, 3), (3, 2), (3, 3)}))

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-atari_go.py>`. You can run it executing the command `python ex-dev-atari_go.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-19

We define a labyrinth as a set of tuples representing the cells of its paths. The tuples are organised in an x/y grid, similar to the way used in [the listing](./12-backtracking.md#board-coords) in [Chapter "Backtracking algorithms"](./12-backtracking.md) for the peg solitaire, such as the one proposed as follows:

```
      (1,0)       (3,0) (4,0) (5,0)
(0,1) (1,1) (2,1) (3,1)       (5,1)
(0,2)       (2,2)       (4,2) (5,2)
(0,3)       (2,3) (3,3)       (5,3)
(0,4)                   (4,4)      
(0,5) (1,5) (2,5) (3,5) (4,5)      
```

Write the function `solve_labyrinth(paths, entrance, exit, last_move)` using a backtracking approach, which takes as input the paths of the labyrinth (such as the ones mentioned above), two tuples representing the entrance and the exit of the labyrinth, and the last move made. The function returns the last move done to reach the exit if the labyrinth has an escape; otherwise, it returns `None`.

Accompany the implementation of the function with the appropriate test cases.

````{solution} part-4-ex-19
:label: part-4-ex-19-sol
:class: dropdown

```python
from anytree import Node
from collections import deque


# Test case for the function
def test_solve_labyrinth(paths, entrance, exit, last_move, expected):
    result = solve_labyrinth(paths, entrance, exit, last_move)
    if result is not None and result.name == exit:
        return True
    else:
        return False


# Code of the function
def solve_labyrinth(paths, entrance, exit, last_move):
    result = None
    paths.remove(last_move.name)

    if entrance == exit:  # leaf-win base case
        result = last_move
    else:
        last_move.children = valid_moves(paths, entrance[0], entrance[1])

        if len(last_move.children) == 0:  # leaf-lose base case
            paths.add(last_move.name)  # backtracking
        else:  # recursive step
            possible_moves = deque(last_move.children)

            while result is None and len(possible_moves) > 0:
                current_move = possible_moves.pop()
                result = solve_labyrinth(paths, current_move.name, exit, current_move)

            if result is None:
                paths.add(last_move.name)  # backtracking

    return result


def create_labyrinth():
    return set([
        (1, 0), (3, 0), (4, 0), (5, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (5, 1),
        (0, 2), (2, 2), (4, 2), (5, 2),
        (0, 3), (2, 3), (3, 3), (5, 3),
        (0, 4), (4, 4),
        (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])


def valid_moves(available_paths, x, y):
    result = list()

    if (x - 1, y) in available_paths:
        result.append(Node((x - 1, y)))
    if (x + 1, y) in available_paths:
        result.append(Node((x + 1, y)))
    if (x, y - 1) in available_paths:
        result.append(Node((x, y - 1)))
    if (x, y + 1) in available_paths:
        result.append(Node((x, y + 1)))

    return result


# Tests
print(test_solve_labyrinth(create_labyrinth(), (1, 0), (5, 3), Node((1, 0)), (5, 3)))
print(test_solve_labyrinth(create_labyrinth(), (5, 3), (1, 0), Node((5, 3)), (1, 0)))
print(test_solve_labyrinth(create_labyrinth(), (1, 0), (1, 0), Node((1, 0)), (1, 0)))
```

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-solve_labirinth.py>`. You can run it executing the command `python ex-solve_labirinth.py` in a shell.
````
`````

`````{exercise}
:label: part-4-ex-20

A **minimax** is a recursive algorithm for choosing the next move in a two-player (A and B) game like chess, where all the possible configurations of the board are described as nodes in a tree of moves. A value is associated with each configuration (i.e. each node) and indicates how good it would be for a player (either A or B, depending on the turn) to reach that configuration. If it is A's turn to move, A gives a value to each of its legal moves, i.e. the child nodes of the one describing the current configuration. The best value for A is the **maximum** of the values of the children of the configuration in which A has to play, while the best value for B is the **minimum** of the values of the children of the configuration in which B has to play.

The minimax uses a heuristic function `get_value` **only** when a **terminal node** of the tree of moves is reached or when **nodes at the maximum search depth** are reached (the maximum depth is specified as input to the algorithm). The other non-leaf nodes inherit their value from a descendant leaf/max-depth node, i.e. either the maximum of the values of the children if A is playing or the minimum of the values of the children if B is playing. An example of minimax execution is shown in {numref}`minimax`.

```{figure} images/ex-minimax.png
---
name: minimax
---
Minimax execution.
```

Write an algorithm in Python – `def minimax(node, max_depth, player_a_moves)` – which takes in input a node of the tree of moves, the maximum depth to consider while visiting the tree of moves, and whether the player A is playing (when `player_a_moves` is True) or its opponent is (when `player_a_moves` is False), and returns the heuristic value that will be assigned to the input node. The function `def get_value(node)`, for getting the heuristic value associated with a leaf or a node at maximum depth, and another function `def get_next_valid_moves(node)`, used to get all the moves (i.e. children) of a configuration (i.e. a node), are provided (i.e. they must not be developed) and can be directly used in the implementation of the algorithm. Initially, for instance considering the image above, the algorithm will be called as follows:

```python
minimax(root, 2, True)
```

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-20
:label: part-4-ex-20-sol
:class: dropdown

```python
from anytree import Node


# Test case for the function
def test_minimax(node, max_depth, player_a_moves, expected):
    result = minimax(node, max_depth, player_a_moves)
    if expected == result:
        return True
    else:
        return False


# Code of the function
def minimax(node, max_depth, player_a_moves):
    if max_depth == 0 or len(node.children) == 0:
        return get_value(node)
    else:
        move_values = []
        for move in get_next_valid_moves(node):
            move_values.append(minimax(move, max_depth - 1, not player_a_moves))
            
        if player_a_moves:
            return max(move_values)
        else:
            return min(move_values)


# Ancillary functions for granted
def get_value(node):
    d = {
        "Move X": 2,
        "Move Y": 7,
        "Move Z": 5,
        "Move W": 10,
        "Move V": 8
    }
    return d[node.name]


def get_next_valid_moves(node):
    return node.children


# Tests
root = Node("Move Y")
node_1_1 = Node("Move X", root)
node_1_2 = Node("Move Y", root)
node_2_1 = Node("Move X", node_1_1)
node_2_2 = Node("Move Y", node_1_1)
node_2_3 = Node("Move Z", node_1_1)
node_2_4 = Node("Move W", node_1_2)
node_2_5 = Node("Move Y", node_1_2)
node_3_1 = Node("Move Y", node_2_2)
node_3_2 = Node("Move V", node_2_2)

print(test_minimax(root, 0, True, 7))
print(test_minimax(root, 2, True, 7))
print(test_minimax(root, 3, True, 7))
print(test_minimax(root, 7, True, 7))
``` 

The source Python file of the code shown above is available {Download}`as part of the material of the course<./material/ex-dev-minimax.py>`. You can run it executing the command `python ex-dev-minimax.py` in a shell.
````
`````

## References

```{bibliography}
:filter: docname in docnames
```