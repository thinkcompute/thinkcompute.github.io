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
:label: part-4-ex-9

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

````{solution} part-4-ex-9
:label: part-4-ex-9-sol
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
:label: part-4-ex-10

Write an extension of the multiplication function introduced in the {numref}`ch-recursion`, i.e. `def multiplication(int_1, int_2, solution_dict)`, by using a dynamic programming approach. This new function takes in input two integers to multiply and a dictionary with solutions of multiplications between numbers. The function returns the result of the multiplication and, at the same time, modifies the solution dictionary adding additional solutions when found. 

Accompany the implementation of the function with the appropriate test cases. 

````{solution} part-4-ex-10
:label: part-4-ex-10-sol
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


## References

```{bibliography}
:filter: docname in docnames
```