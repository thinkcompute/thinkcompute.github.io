(ch-graphs)=
# Greedy algorithms

This chapter introduces the last kind of algorithms presented in this book, i.e. the *greedy algorithms*. The historic hero introduced in these notes is Evelyn Berezin, one of the most influential businesswomen of the past century who have created the first word processor.

```{note}
The slides for this chapter are <a href="14-slides-greedy.html">available</a> within the book content.
```


## Historic hero: Evelyn Berezin

[Evelyn Berezin](https://en.wikipedia.org/wiki/Evelyn_Berezin) (depicted in {numref}`berezin`) was a physicist. She began to work in a company that produced digital computers, where she started to work on particular the development of the logic designs of computers – e.g. {cite}`auerbach_electronic_1962`. After many years passed in changing jobs and several contributions related to the development of large computer systems such as the computerised reservation system for United Airlines, in 1969, she founded her own company: Redactron Corporation.

In this new company, she started to work on computer systems to simplify the work of secretaries. The company’s main product was *Secretary*: the first [word processor](https://en.wikipedia.org/wiki/Word_processor) in history. It was a stand-alone device developed to address specific tasks and replace the more common typewriter. Data Secretary was the precursor of all the word processors designed since that date. While they were stand-alone devices initially, word processors soon became independent software applications. We remember [Electric Pencil (1976)](https://en.wikipedia.org/wiki/Electric_Pencil), [WordStar (1978)](https://en.wikipedia.org/wiki/WordStar), [Microsoft Word (1983)](https://en.wikipedia.org/wiki/Microsoft_Word) and [OpenOffice Writer (1999)](https://en.wikipedia.org/wiki/OpenOffice.org).


```{figure} images/14-berezin.png
---
name: berezin
---
A picture of Evelyn Berezin taken in 2015. Source: [Computer History Museum](https://images.computerhistory.org/blog-media/2015-fellow-awards-evelyn-berezin.jpg). 
```


## The greedy approach

A *[greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)* is a particular algorithmic approach. At every execution stage, it always makes the optimal choice (i.e. the best one) in that specific moment. For certain kinds of problems, this behaviour allows us to reach the best possible solution to the computational problem into consideration. For instance, if you have to determine the minimum number of euro coins needed for making a change, then a greedy algorithm will return an optimal solution overall:

1. consider the coins to choose for the change as ordered in a decrescent way, from the highest value (i.e. 2 euros) to the lowest one (i.e. 1 cent);
2. for each kind of value, add in the candidate set of the solution as many coins of that value as possible until their sum is lesser than the remaining of the change to give;
3. If we reach the change value, return it.

However, sometimes it is possible that the solution found is just a suboptimal solution while it provides a correct answer to the problem. For instance, driving from Florence to Bologna, we can encounter a crossroad with two signs indicating two different routes to get to Bologna. The left road allows us to get to Bologna by travelling for 42 kilometres. On the other hand, the right way enables us to get to Bologna by going 56 kilometres. A simple greedy approach would select the left route: at the moment, it seems the most convenient scenario. However, the plan does not predict possible traffic on the left road. Consequently, it would be possible to arrive in Bologna even after a car takes the correct route.

There are two main characteristics that a computational problem should show to ensure that the application of a greedy approach will bring an optimal solution to the problem. The first one is that the *greedy choice property* should be guaranteed. This property means that, at a particular step, we can choose the best candidate for improving the set of candidates bringing to a solution.

The other characteristic is that the problem has an *[optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure)*. In particular, we must build the optimal solution to a computational problem by considering the optimal solutions to its subproblems. For instance, the previous example of the travel from Florence to Bologna does not have an optimal substructure. As a result, we can encounter accidents on a road we chose in a previously-chosen optimal strategy (i.e. the shortest path).


## Line wrap

[Wrapping a line](https://en.wikipedia.org/wiki/Line_wrap_and_word_wrap), i.e. understanding where to break a line in a page, is one of the problems one must tackle when dealing with documents, either in print or digital forms. For instance, when a person is using a typewriter for writing a document, at a certain point, after she has written many characters, there is a mandatory action to perform, which is the carriage and return operation, performed mechanically on the typewriter itself. When the writer notices that the line has no more space for imprinting a new word, she initialises the typewriter to start from the very beginning of the left border but in the following line.


```{figure} images/14-wordprocessor.png
---
name: wordprocessor
---
A screenshot that depicts how[ OpenOffice Writer](https://www.openoffice.org/) deals with line wrap.
```


```{code-block} python
---
name: py-linewrap
linenos: True
caption: |
    The implementation of the algorithm for calculating the line-wrap problem in Python. The source code of this listing is available {Download}`as part of the material of the course<./python/line_wrap.py>`.
---
# Test case for the function
def test_line_wrap(text, line_width, expected):
	result = line_wrap(text, line_width)
	if expected == result:
    		return True
	else:
    	return False

# Code of the function
def line_wrap(text, line_width):
	result = list() # the list of all the lines of a document

	# the maximum available space per a specific line
	space_left = line_width
	# the current line that is built
	line = list()

	for word in text.split(" "):
    		word_len = len(word)
        	# the length of the word plus one space character
        	if word_len + 1 > space_left:
            	result.append(" ".join(line))
            	line = list()
               line.append(word)
            	space_left = line_width - word_len
        	else:
            	line.append(word)
            	space_left = space_left - (word_len + 1)

	# we add the remaining line to the document
	result.append(" ".join(line))
	return "\n".join(result)

# Tests
print(test_line_wrap("Just a word.", 15, "Just a word."))
print(test_line_wrap("Just a word.", 1, "\nJust\na\nword."))
print(test_line_wrap("Just a few words.", 9, "Just a\nfew\nwords."))
print(test_line_wrap("This is a simple example.", 10,
                 	"This is a\nsimple\nexample."))
```


In modern tools, such as word processors (shown in {numref}`wordprocessor`), an algorithm handles the line wrap. Such an algorithm takes care of choosing when there is enough space to put that word in the current line. Generally speaking, we can describe the problem in the following manner:

```{admonition} Computational problem
Break a text into lines to fit in the available width of a page.
```

A greedy approach is very efficient and effective for addressing the aforementioned computational problem. It will proceed as follows:

1. For each word in the input text, see if there is enough space in the line for adding that word;
2. If there is space, add the word to the line; otherwise,
3. Declare finished the current line, and add the word as the first token of the following line.

To implement this algorithm, we need two methods for tokenising and recomposing strings. The first of these methods is ​`<string>.split(<string_separator>`). This method allows us to separate the string according to a specific set of characters the string may contain, specified by the parameter ​`<string_separator>`. For instance, if we have the variable `my_string` assigned to `"a b c"`, the execution of the method mentioned above, i.e. `my_string.split(" ")`, returns the following list: `["a", "b", "c"]`.

The other method we need, i.e. ​`<string_separator>.join(<list_of_strings>)`, implements the opposite operation, i.e. it is able to concatenate the strings in a list again, according to a particular sequence of characters. For instance, if we have the list `my_list = ["a", "b", "c"]`, the execution of the aforementioned method, i.e. ​`" ".join(my_list)`, returns the following string: `"a b c"`.

We now have all the ingredients for implementing our algorithm for the line-wrap in Python, as shown in {numref}`py-linewrap`.



## References

```{bibliography}
:filter: docname in docnames
```