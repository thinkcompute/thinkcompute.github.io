(ch-programming-languages)=
# Programming Languages

This chapter provides a general introduction to programming languages and then focuses on a particular language: Python. The historic hero introduced in these notes is Grace Hopper. She was the first programmer of the Harvard Mark I computer. She was responsible for the development of some of the first programming languages.


## Historic hero: Grace Hopper

[Grace Brewster Murray Hopper](https://en.wikipedia.org/wiki/Grace_Hopper) (depicted in {numref}`hopper` was a computer scientist. She was the first programmer of the [Harvard Mark I](https://en.wikipedia.org/wiki/Harvard_Mark_I), i.e. a general-purpose electromechanical computer. The Harvard Mark I was used during the Second World War, fully-inspired by Babbage's [Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine). She pushed for the need of having machine-independent programming languages. This idea brought her in the development of *[COBOL](https://en.wikipedia.org/wiki/COBOL)*, one of the first high-level programming languages, which is still used today for some applications.

COBOL (i.e. the *common business-oriented language*) is a programming language designed for business use. It brings a quite extensive use of English terms for describing the operations of a program. For the very first time, the idea of adopting English for commands made the programming language a bit more verbose and more readable and even self-documenting. Just for making an example, in today's languages if we want to compare if the value assigned to a variable `x` is greater than the one assigned to another variable `y` we should use `x > y`. In COBOL, the same comparison is made with the following instruction: `x IS GREATER THAN y`.


```{figure} images/04-hopper.png
---
name: hopper
---
Portrait of Grace Hopper. Picture by James S. Davis, source: [Wikipedia](https://en.wikipedia.org/wiki/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg).
```


## A brief history of programming languages

After the Second World War, people have developed several [programming languages](https://en.wikipedia.org/wiki/History_of_programming_languages) according to several design principles and intended usage in terms of the computational problems to be solved. While all of them, in principle, make it possible to develop solutions for any solvable computational problem, some of them are more suited for a specific domain than others. For instance, [COBOL](https://en.wikipedia.org/wiki/COBOL) has been developed for business applications, while [FORTRAN](https://en.wikipedia.org/wiki/Fortran) was designed to deal with scientific computing.

While an extensive analysis of all the programming languages is out of the scope of the topics of this book, it is worth mentioning, at least graphically, a timeline of their evolution, shown in {numref}`programming-languages`. As highlighted in the timeline, we will introduce and use a particular programming language in this course, i.e. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), according to its third version released in 2006.


```{figure} images/04-programming-languages.png
---
name: programming-languages
---
A graphic timeline summary of some of the main programming languages from 1954 to 2017. The different line colour is used only for readability reasons, and it does not have any particular meaning.
```


## Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a high-level programming language for general-purpose programming. It is currently one of the most used languages for programming on the Web for Data Science and Natural Language Processing tasks. The good thing about Python is that it is one of the most simple languages for starting to learn how to program and create software.

In this course, we will use Python in its latest version, i.e. Python 3. Luckily, there are a lot of resources freely available online for learning this language from scratch, such as:

* the introductory book *Dive into Python 3* {cite}`pilgrim_dive_2009`;
* the [official documentation](https://docs.python.org/3/) of the language;
* an [online platform for playing with Python 3](https://repl.it) without installing any software on your computer;
* an [interactive online course](https://www.sololearn.com/Play/Python/) for learning Python from scratch;
* a book introducing all the basic Python features, which is particularly suited for Digital Humanities {cite}`tagliaferri_how_2018`;
* another book entirely dedicated to problem solving and algorithms developed in Python {cite}`miller_problem_2011`;
* a digital book that contains an introduction to [Python for the Humanities](http://www.karsdorp.io/python-course/).

The goal of this chapter is to develop our first algorithm in Python. The algorithm we produce is the one we have introduced in Chapter {ref}`ch-algorithms`, that can be described informally by the following natural language text: 

> Consider three different strings as input, i.e. two words and a bibliographic entry of a published paper. The algorithm must return the number 2 if the bibliographic entry contains both words; the number 1 if the bibliographic entry contains only one word; the number 0 otherwise.


### First incomplete version, in Python

In Python, we can create a new algorithm by implementing a new *function*. We can introduce a function using the keyword `def` (which stands for *define*). The keyword `def` must be followed by a name (e.g. the name of the algorithm) and a comma-separated list of input parameters between round brackets. For instance, `def contains_word(first_word, second_word, bib_entry)` defines the function `contains_word`, which takes three parameters as input​.

Each function definition is followed by “`:`” and all the instructions to execute must be specified in the following lines, as an indented block (preferably using four spaces), as illustrated in {numref}`py-function`. The name of a function and its parameters cannot contain space characters and must always start with a letter – e.g. `this_is_my_parameter` is correct, while `1_parameter` is not.


```{code-block} python
---
name: py-function
linenos: True
caption: |
    The definition of an algorithm, with its input parameter, and some dots that identify where to put the instruction of such algorithm – one per line, indented of 4 space characters. 
---
​def contains_word(first_word, second_word, bib_entry):
    ...
    ...
    ...
```


In this first version of the algorithm, we would like to introduce only some basic constructs of Python. To this end, we provide only a partial solution in this subsection, which we finalise in the following subsections, following the same strategy used in Chapter {ref}`ch-algorithms`. In particular, we want to say that if the bibliographic entry contains the first input word, the number 1 is returned; otherwise, a 0 is returned. {numref}`py-function-def` shows this incomplete version of the algorithm in Python.


```{code-block} python
---
name: py-function-def
linenos: True
caption: |
    An incomplete version of the algorithm that is used to introduce some basic constructs of Python.
---
def contains_word(first_word, second_word, bib_entry):
    if first_word in bib_entry:
        return 1
    else:
        return 0
```


In this incomplete version, there are already specified some important constructs of Python. The first one is the *if-else* conditional block. This kind of block allows one to execute a particular instruction if a condition is true (the `if` statement). Otherwise, if the condition specified is false, an alternative set of instructions is executed instead (the `else` statement). We can avoid specifying the `else` clause if no alternative set of instructions is needed. The instructions to perform in one case or the other are within indented sub-blocks (again, four additional spaces). As already introduced in {numref}`py-function-def`, every time we have to add a new block of instructions, we need to use ​`:` after the statement of interest, as shown in {numref}`py-if-else`.


```{code-block} python
---
name: py-if-else
linenos: True
caption: |
    The generic structure of an *if-else* conditional block.
---
​if <condition>:
    ...
    ...
else:
    ...
    ...
```

The condition specified in the `if` statement shown in {numref}`py-function-def` allows one to check if a certain string is contained in another one using the command “in”. In particular, `<string1> in <string2>` would be true if the *<string2>* contains *<string1>*. As anticipated in the previous chapters, a *[string](https://en.wikipedia.org/wiki/String_(computer_science))* is a particular type of value composed of a sequence of characters and defined by using quotes. For instance, `"Peroni"`, `"Osborne"`, and ​`"Peroni, S., Osborne, F., Di Iorio, A., Nuzzolese, A. G., Poggi, F., Vitali, F., Motta, E. (2017). Research Articles in Simplified HTML: a Web-first format for HTML-based scholarly articles. PeerJ Computer Science 3: e132. e2513. DOI: https://doi.org/10.7717/peerj-cs.132"` are all strings. 

Note that *<string1>* and *<string2>* are just placeholders for strings: we can use either strings, e.g. `"Peroni"` in `"Peroni beer"`, or variables referring to strings, as shown in {numref}`py-function-def`. A [variable](https://en.wikipedia.org/wiki/Variable_(computer_science)) is a symbolic name that contains some information referred to as a value (e.g. first_word). For instance, any input value is, in fact, a particular kind of variable. As defined previously, all the input parameters of the algorithm are expected to refer to strings.

The last construct of the partial algorithm introduced in this subsection is the `return` statement. It is defined by specifying the token `return` followed by the value (or the variable containing a value) that must be returned. The execution of a `return` statement concludes the algorithm execution. Thus, all the instructions that follow that statement are not processed anymore. In the example in {numref}`py-function-def`, two different numbers are returned, depending on the execution of a particular branch of the *if-else* block. In particular, the algorithm returns a *1* if the condition of the `if` statement is true, while it returns a *0* otherwise. Python permits to write any number as it is – e.g. `​42` and `-42` for positive/negative integers, `1.625` and `-1.625` for positive/negative decimals. Note that strings and numbers are distinct kinds of objects – e.g. the string `"42"` and the number `42` (without the quotes) **do not** define the same value.


### Complex boolean statements

The original text of the algorithm, introduced at the beginning of Section {ref}`Python`, needs to condition to be true for returning a 2. Indeed, the bibliographic entry must contain both words. This can be defined using a hierarchy of *if-else* blocks in Python, as shown in {numref}`py-if-else-def`.


```{code-block} python
---
name: py-if-else-def
linenos: True
caption: |
    A hierarchy of *if-else* blocks for describing the three possible return values of the algorithm.
---
​if first_word in bib_entry:
    if second_word in bib_entry:
        return 2
    else:
        return 1
else:
    if second_word in bib_entry:
        if first_word in bib_entry:
            return 2
        else:
            return 1
    else:
        return 0
```


However, the readability of the previous example is rather difficult since it repeats several times the same conditions, even if they have been specified in a different order. Thus, Python makes available some operations for assessing compositions of multiple [boolean values](https://en.wikipedia.org/wiki/Boolean_data_type) and for deriving boolean values from number and string comparisons. A boolean value (or, directly, *boolean*)[^1] can be only one of two distinct and disjoint values, *True* and *False*. For instance, the condition `first_word in bib_entry` returns a particular boolean: *True* if the bibliographic entry contains the word, *False* otherwise. We use boolean values in algorithms (and in any programming language) to organise conditional block execution flow.

Sometimes it is useful to combine somehow two distinct boolean values to simplify the conditional blocks’ organisation. This can be done by using specific operators that apply to one (`<operator> <B1>`) or two boolean values (`<B1> <operator> <B2>`), and return a new boolean value. These operators are called *logical not* (`​not` in Python, which applies to one boolean value only), *logical and *(`​and`, between two boolean values), and *logical or* (`​or`, between two boolean values). They are *logical* operators since they derive from the logic Boole proposed in his works on [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra). {numref}`truth-table-bool` summarises their use and shows the *[truth table](https://en.wikipedia.org/wiki/Truth_table)* of the application of such operators. In particular, given two boolean input values, *B1* and *B2*, the table shows the result of all their possible combinations according to the specific operator. Thus, in the example in {numref}`py-if-else-def`, we could return a *2* if the bibliographic reference contains both the strings, expressing this constraint in one condition only, i.e. `first_word in bib_entry and second_word in bib_entry`.


```{list-table} The truth table of all the boolean operations.
:header-rows: 1
:name: truth-table-bool

* - B1
  - B2
  - not B1
  - B1 and B2
  - B1 or B2
* - True
  - True
  - False
  - True
  - True
* - True
  - False
  - False
  - False
  - True
* - False
  - True
  - True
  - False
  - True
* - False
  - False
  - True
  - False
  - False
```


Round brackets can be used for grouping boolean operations, e.g. `(True and False) or False` applies the `and` operation first, and the result is used as the first value of the `or` operation – given *False* as a result. If there are no brackets, the application order proceeds as follows. First, one must execute all the `not` operations. Then, one must perform all the `and` operations. Finally, one must assess the remaining `or` operations. For instance, `​True and not False or False` returns *True* since it is interpreted as `(True and (not False)) or False`.


```{list-table} The truth table of all string comparisons.
:header-rows: 1
:name: truth-table-string

* - S1
  - S2
  - S1 < S2
  - S1 <= S2
  - S1 > S2
  - S1 >= S2
  - S1 == S2
  - S1 != S2
  - S1 in S2
  - S1 not in S2
* - `"Alice"`
  - `"Bob"`
  - True
  - True
  - False
  - False
  - False
  - True
  - False
  - True
* - `"Alice"`
  - `"Alice"`
  - False
  - True
  - False
  - True
  - True
  - False
  - True
  - False
```


In addition to the aforementioned boolean operations, it is also possible to use string comparisons for obtaining boolean values. {numref}`truth-table-string` shows all the comparisons that one can apply on two strings, i.e. `<S1> <operator> <S2>`. In this case, the operators are those typically used numerical comparison, i.e.:

* ​`<`, less than;
* ​`<=`, less than or equal to;
* ​`>`, greater than;
* `​>=` greater than or equal to;
* ​`==`, equal to;
* ​`!=`, different from;
* `​​in`, included in;
* ​`not in`, not included in.

In the case of strings, a string *S1* is *less than* another string *S2* if the former precedes the latter according to a pure alphabetic order. Of course, Python uses the alphabetic order for assessing when a string is *greater than* another one.

Note that we can use similar operators (excluding `in`) for comparing numbers, as shown in {numref}`truth-table-number`. In this case, the standard mathematical numeric comparisons hold.


```{list-table} The truth table of all the arithmetic comparisons.
:header-rows: 1
:name: truth-table-number

* - N1
  - N2
  - N1 < N2
  - N1 <= N2
  - N1 > N2
  - N1 >= N2
  - N1 == N2
  - N1 != N2
* - 3
  - 4
  - True
  - True
  - False
  - False
  - False
  - True
* - 4
  - 4
  - False
  - True
  - False
  - True
  - True
  - False
```


Thus, we can reuse these boolean operations to rewrite the *if-else* blocks shown in {numref}`py-if-else-def` more understandably. Finally, {numref}`py-if-else-def-alt` shows the result.


```{code-block} python
---
name: py-if-else-def-alt
linenos: True
caption: |
    A hierarchy of *if-else* blocks shown in Listing 4 rewritten according to the boolean operations presented in this section. 
---
​if first_word in bib_entry and second_word in bib_entry:
    return 2
else:
    if first_word in bib_entry or second_word in bib_entry:
        return 1
    else:
        return 0
```


### Conditional statements with multiple branches

While in the previous subsections we have improved the readability of the *if-else* blocks, Python allows us to do even better. First of all, in the two if statements in {numref}`py-if-else-def-alt`, we ask Python to evaluate the same sub-conditions (i.e. `first_word in bib_entry and second_word in bib_entry`) twice. This can be easily avoided by defining new variables. A variable is defined by specifying its name (without spaces), followed by an `=` and the value to associate to it, i.e. `<variable_name> = <variable_value>`. The value can be specified directly (e.g. a number) or indirectly by using other variables or even complex operations.

In our example, we could create two variables, called `contains_first_word` and `contains_second_word`, assigned to the boolean returned by the string comparisons mentioned above, i.e. `first_word in bib_entry` and `second_word in bib_entry`, respectively. In that way, we can reuse such variables in the two if statements, as shown in {numref}`py-if-else-variables`.


```{code-block} python
---
name: py-if-else-variables
linenos: True
caption: |
    The *if-else* blocks introduced in {numref}`py-if-else-def-alt` where the conditions in `if` statements are specified using two variables.
---
​if contains_first_word and contains_second_word:
    return 2
else:
    if contains_first_word or contains_second_word:
        return 1
    else:
        return 0
```


We can improve further the readability of the code by collapsing occurrences of else statements when these contain an `if` statement. In this case, both the *else-if* pair can be safely replaced by an `elif` (i.e. *else if*) statement, which specifies the same condition used in the if statement. Thus, the code in {numref}`py-if-else-variables` can be rewritten, as shown in {numref}`py-if-elif`.


```{code-block} python
---
name: py-if-elif
linenos: True
caption: |
    The *if-else* blocks introduced in Listing 6 collapsed using an `elif` statement. 
---
if contains_first_word and contains_second_word:
    return 2
elif contains_first_word or contains_second_word:
    return 1
else:
    return 0
```


### Final algorithm

In this chapter, we have seen some initial constructs that Python makes available for developing an algorithm. In particular, we have introduced how to define a function with input parameters, variables, conditional statements (i.e. `if`, `elif`, and `else`), string, numeric, and boolean values, boolean operations and string and numeric comparisons. All these constructs enabled us to define our algorithm, which is finally introduced in {numref}`py-final-algorithm`.


```{code-block} python
---
name: py-final-algorithm
linenos: True
caption: |
    The final algorithm developed.
---
def contains_word(first_word, second_word, bib_entry):
    contains_first_word = first_word in bib_entry
    contains_second_word = second_word in bib_entry


    if contains_first_word and contains_second_word:
        return 2
    elif contains_first_word or contains_second_word:
        return 1
    else:
        return 0
```

It is worth mentioning that the algorithm proposed initially in Chapter {ref}`ch-algorithms` as a flowchart does not map with the one presented in {numref}`py-final-algorithm`. This misalignment has been done to explicitly show that it is entirely possible to develop two different algorithms for addressing the same computational problem.

As a final note, and in addition to using the Python interpreter installed on your machine (in any), several Web applications have been developed to test your Python code. Often, they show which kinds of objects Python creates when running. One of these tools, i.e. [Python Tutor](http://www.pythontutor.com), is very helpful for people approaching Python for the first time. Indeed, it allows one to see what happens as the (electronic) computer runs each line of code.


## Test-driven development

Different development strategies can be adopted when one wants to understand whether the piece of software he/she has developed is correct or not – i.e. if it is returning the expected result. One of the most used and practical methods used by programmers is the *[Test-Driven Development (or TDD)](https://en.wikipedia.org/wiki/Test-driven_development)* {cite}`beck_test-driven_2003`, summarised in {numref}`tdd`.

In practice, when one has a computational problem to solve, and he/she needs to develop a piece of software to address it, the first thing to develop is a test to check if the software that eventually will be developed behaves correctly (i.e. returns the correct result) or not. Usually, such a test is software that must be designed to test the correctness of another software. 

Writing a test before starting to develop software allows one to focus on the problem one has to solve and on the requirements of the software from the very beginning. This approach is also practical when one decides to extend an existing software. In this case, first, one has to develop the test for assessing the correctness of such a new extension. Second, one needs to write the extension and check if the extended software passes the new test.


```{figure} images/04-tdd.png
---
name: tdd
---
A diagram summarising the steps of the test-driven development approach. Picture by Xarawn, source: [Wikipedia](https://en.wikipedia.org/wiki/File:TDD_Global_Lifecycle.png).
```


1. Write a new test – once understood the computational problem to solve and the related requirements, a new test is written and then added to a collection of previously developed tests.
2. Run all the tests – we run all the tests available in the collection mentioned above. If the new test fails, there is no code available that addresses the particular computational problem described by the test. Thus, the test fails in the first iteration of the test-driven development since no code has been developed yet.
3. Write the new code – in this step, we develop a new code to pass the test just added to the collection.
4. Run all the tests again – in this passage, one checks if the addition of such new code developed to address the new test has not broken the other features already designed and tested by all the other tests available in the collection (in any). If any test fails, the new code must be corrected until all the tests are passed successfully.
5. Refactor the code – after several iterations of the process, the code grows naturally, and it may be necessary to refactor as to clean the code as much as possibleto guarantee its readability and maintainability in the long term. As a suggestion, every refactoring action should be checked by re-run all the tests available to be sure that a modification to the code does not break its correctness.

Following this approach to development is very useful when one has to implement a particular algorithm in Python. It enables one to check its correctness according to different kinds of input that can be used to run the algorithm itself. {numref}`tdd-define-test` shows a plausible test to verify the accuracy of the algorithm introduced in this chapter.


```{code-block} python
---
name: tdd-define-test
linenos: True
caption: |
    The test function developed for testing the `contains_word` code, introduced in {numref}`py-final-algorithm`.
---
def test_contains_word(first_word, second_word, bib_entry, expected):
    result = contains_word(first_word, second_word, bib_entry)
    if expected == result:
        return True
    else:
        return False
```


It is possible to use such a test function to test the `contains_word` code with different kinds of input values and related expected results. For instance, {numref}`tdd-define-run` shows the test code, the algorithm’s code presented in this chapter, and some checks done by running the test code (and thus the algorithm itself) with different input values. Finally, the result of the various inspections is printed on screen by using the Python function `print()`.


```{code-block} python
---
name: tdd-define-run
linenos: True
caption: |
    The test code, the algorithm implementation in Python, and three distinct runs of the test with different configurations and expected results. The source code of this listing is available {Download}`as part of the material of the course<./python/first_algorithm.py>`.
---
# Test case for the algorithm
def test_contains_word(first_word, second_word, bib_entry, expected):
    result = contains_word(first_word, second_word, bib_entry)
    if expected == result:
        return True
    else:
        return False

# Code of the algorithm
def contains_word(first_word, second_word, bib_entry):
    if first_word in bib_entry and second_word in bib_entry:
        return 2
    elif first_word in bib_entry or second_word in bib_entry:
        return 1
    else:
        return 0

# Three different test runs
print(test_contains_word("Shotton", "Open",
    "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 2))
print(test_contains_word("Citations", "Science",
    "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 1))
print(test_contains_word("References", "1983",
    "Shotton, D. (2013). Open Citations. Nature, 502: 295–297. doi:10.1038/502295a", 0))
```

{numref}`tdd-template-full-impl` shows the final Python implementation of the algorithm and the related test for the example mentioned above.


### Succeed: check if the Python code returns the correct output

Finally, we should test the Python implementation of the algorithm according to the tests developed in step “Fail”. If all the output values returned by running the Python tests comply with the expected results, we have finished. Otherwise, if some execution returned an unexpected output, we need to go back to the previous step and change something in the Python implementation of the algorithm.

All the tests introduced in {numref}`tdd-template-full-impl` are passed as expected. It is possible to use [Python Tutor](http://pythontutor.com/visualize.html#code=%23%20Test%20case%20for%20the%20algorithm%0Adef%20test_contains_word%28first_word,%20second_word,%20bib_entry,%20expected%29%3A%0A%20%20%20%20result%20%3D%20contains_word%28first_word,%20second_word,%20bib_entry%29%0A%20%20%20%20if%20expected%20%3D%3D%20result%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%0A%0A%23%20Code%20of%20the%20algorithm%0Adef%20contains_word%28first_word,%20second_word,%20bib_entry%29%3A%0A%20%20%20%20if%20first_word%20in%20bib_entry%20and%20second_word%20in%20bib_entry%3A%0A%20%20%20%20%20%20%20%20return%202%0A%20%20%20%20elif%20first_word%20in%20bib_entry%20or%20second_word%20in%20bib_entry%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%200%0A%0A%0A%23%20Three%20different%20test%20runs%0Aprint%28test_contains_word%28%22Shotton%22,%20%22Open%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Shotton,%20D.%20%282013%29.%20Open%20Citations.%20Nature,%20502%3A%20295%E2%80%93297.%20doi%3A10.1038/502295a%22,%202%29%29%0Aprint%28test_contains_word%28%22Citations%22,%20%22Science%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Shotton,%20D.%20%282013%29.%20Open%20Citations.%20Nature,%20502%3A%20295%E2%80%93297.%20doi%3A10.1038/502295a%22,%201%29%29%0Aprint%28test_contains_word%28%22References%22,%20%221983%22,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22Shotton,%20D.%20%282013%29.%20Open%20Citations.%20Nature,%20502%3A%20295%E2%80%93297.%20doi%3A10.1038/502295a%22,%200%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see a complete execution of such code.



## References

```{bibliography}
:filter: docname in docnames
```

## Notes

[^1]:
     The word *boolean* was named after [George Boole](https://en.wikipedia.org/wiki/George_Boole), who was a great logician of the 19<sup>th</sup> century.

