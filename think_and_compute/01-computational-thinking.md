(ch-computational-thinking)=
# Introduction to Computational Thinking

This chapter introduces the main concepts related to computational thinking by providing a summary of relevant topics in the areas of Linguistics and Computing in the past 200 years. The historic hero introduced in these notes is Noam Chomsky, considered one of the fathers of modern linguistics. His works have had an enormous impact on the Linguistics domain and the Theoretical Computer Science domain.


(historic-hero)=
## Historic hero: Noam Chomsky

[Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky) (shown in {numref}`chomsky`) is one of the most prominent scholars of the last one hundred years. His contributions and research works have been disruptive and have changed the way scholars have approached several domains in science and humanities. He is described as one of the fathers of modern linguistics with Ferdinand de Saussure, Lucien Tesnière, Luis Hjelmslev, Zellig Harris, Charles Fillmore. In addition, he is one of the very first contributors and founders of the cognitive science field[^1].

His approach to linguistics has been revolutionary, even if linguists have also debated it. The central aspect of his approach to human language is that mathematics can be used to represent the syntactic structure of a human language. Also, such a structure is [biologically determined in all humans](https://en.wikipedia.org/wiki/Universal_grammar). It is already within us since birth, and it is a unique characteristic of human beings only and not of other animals. His view of human language is in high contrast with previous ideas about the evolution of languages, which intended a human being with no preconfigured linguistic structure. Thus, the language should have been a matter of learning a radically new endeavour from scratch.

```{figure} images/01-chomsky.png
---
name: chomsky
---
A picture of Chomsky taken in 2011. Photo by Andrew Rusk, source: [Wikipedia](https://en.wikipedia.org/wiki/Noam_Chomsky#/media/File:Noam_Chomsky_Toronto_2011.jpg).
```

Among his extensive series of works in linguistics, the[ classification of formal grammars](https://en.wikipedia.org/wiki/Chomsky_hierarchy) into a hierarchy of increasing expressiveness is undoubtedly one of his most important contributions, especially in the field of Theoretical Computer Science and Programming Languages. [Formal grammar](https://en.wikipedia.org/wiki/Formal_grammar) is a mathematical tool for defining a language, such as English. This tool permits the creation of a finite set of production rules that enable the construction of any valid syntactic sentence.

Each formal grammar is composed of a set of production rules in the form `left-side ::= right-side` (according to the[ Backus–Naur form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form), or BNF), where each side can contain one or more symbols of one or more of the following types:

* _terminal_ (specified between quotes in BNF), which identifies all the elementary symbols of the language in consideration (such as the nouns, verbs, etc., in English);
* _non-terminal_ (specified between angular brackets in BNF) identifies all the symbols in the formal grammar that can be replaced by a combination of terminal and non-terminal symbols.

Applying a production rule means that the sequence of symbols in the `right-side` part of the rule replaces those specified in the `left-side` part. The rewrite process done by the application of such production rules starts from an initial non-terminal symbol. In particular, one applies the production rules until they get a sequence of terminal symbols only. For instance, the production rules `<sentence> ::= <pronoun> "write"`, `<pronoun> ::= "I"` and `<pronoun> ::= "you"` allows one to create all the two-word sentences having either the first or the second person singular pronoun accompanied by the verb write (e.g. “I write”). In addition, each formal grammar must specify a _start symbol_ that must be non-terminal.

The hierarchy proposed by Chomsky provides a way for formally describing the relations between different grammars in terms of the possible syntactic structures that such grammars can generate. In practice, they are characterised by symbols in the `left-side` and `right-side` parts of production rules. These grammars are listed as follows, from the less expressive to the most expressive – we use letters from the Greek alphabet for indicating any possible combination of terminal and non-terminal symbols, including the empty characters (usually represented by `ε`):

* _regular grammars_ – form of production rules: `<non-terminal> ::= "terminal"` and `<non-terminal> ::= "terminal" <non-terminal>`, as shwon in {numref}`regular`.

  ```{code-block} abnf
  ---
  name: regular
  caption: |
      A regular grammar.
  ---
  <sentence> ::= "I" <verb>
  <sentence> ::= "you" <verb>
  <verb> ::= "write"
  <verb> ::= "read"
  ```

* _context-free grammars_ – form of production rules: `<non-terminal> ::= γ`, as shwon in {numref}`context-free`.
  
  ```{code-block} abnf
  ---
  name: context-free
  caption: |
      A context-free grammar.
  ---
  <sentence> ::= <nounphrase> <verbphrase>
  <nounphrase> ::= <pronoun>
  <nounphrase> ::= <noun>
  <pronoun> ::= "I"
  <pronoun> ::= "you"
  <noun> ::= "book"
  <noun> ::= "letter"
  <verbphrase> ::= <verb>
  <verbphrase> ::= <verb> "a" <noun>
  <verb> ::= "write"
  <verb> ::= "read"
  ```

* _context-sensitive grammars_ – form of production rules: `α <non-terminal> β ::= α γ β`, as shwon in {numref}`context-sensitive`.

  ```{code-block} abnf
  ---
  name: context-sensitive
  caption: |
      A context-sensitive grammar.
  ---
  <sentence> ::= <noun> <verbphrase>
  <sentence> ::= <subject pronoun> <verbphrase>
  "I" <verb> <object pronoun> ::= "I" "love" <object pronoun>
  "I" <verb> <noun> ::= "I" "read" "a" <noun>
  <verbphrase> ::= <verb> <noun>
  <verbphrase> ::= <verb> <object pronoun>
  <subject pronoun> ::= "I"
  <subject pronoun> ::= "you"
  <object pronoun> ::= "me"
  <object pronoun> ::= "you"
  <noun> ::= "book"
  <noun> ::= "letter"
  ```

* _recursively enumerable grammars_ – form of production rules: `α ::= β` (no restriction applied), as shwon in {numref}`enumerable`.
  
  ```{code-block} abnf
  ---
  name: enumerable
  caption: |
      A recursively enumerable grammar.
  ---
  <sentence> ::= <subject pronoun> <verbphrase>
  "I" <verb> <object pronoun> ::= "I" <verb> "you"
  "I" <verb> <noun> ::= "I" "read" "a" "book"
  <verbphrase> ::= <verb> <noun>
  <verbphrase> ::= <verb> <object pronoun>
  <subject pronoun> ::= "I"
  <subject pronoun> ::= "you"
  <object pronoun> ::= "me"
  <object pronoun> ::= "you"
  <verb> ::= "love"
  <verb> ::= "hate"
  ```

## What is a computer?

The [English Oxford Living Dictionary](https://en.oxforddictionaries.com/definition/computer) defines the term _computer_ as an “electronic device which is capable of receiving information (data) in a particular form and of performing a sequence of operations [...] to produce a result”. However, the original definition of the same term, in use from the 17th century, is slightly different. It refers to someone “who computes” or a “person performing mathematical calculations” – from [Wikipedia](https://en.wikipedia.org/wiki/Human_computer). In this chapter, when we use the term “computer”, we always consider the most generic definition: any _information-processing agent_ (i.e. a machine or a person acting mechanically if appropriately instructed) {cite}`nardelli_we_2019` that can make calculations and produce some output starting from input information.

_Human_ computers, i.e. groups of people who have to undertake long calculations for specific experiments or measurements, have been used several times in the past. For instance, in Astronomy, human computers have been used for calculating astronomical coordinates of non-terrestrial things – such as the calculation of passages of [Halley's Comet](https://en.wikipedia.org/wiki/Halley%27s_Comet) by Alexis Claude Clairaut and colleagues. Napoleon Bonaparte used human computers, as well. He imposed the creation of mathematical tables to convert from the old imperial system of measurements to the new metric system {cite}`campbell-kelly_origin_2009,roegel_great_2010`.

```{figure} images/01-difference-engine.png
---
name: difference-engine
---
Babbage Difference Engine No. 2 built at the Science Museum (London) and displayed at the Computer History Museum in Mountain View (California). Picture by Allan J. Cronin, source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Difference_engine.JPG).
```

In 1822, [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage), understanding the complexity of doing all these calculations by hand without introducing any error, started the development of an incredible machine. This machine was called the [Difference Engine](https://en.wikipedia.org/wiki/Difference_engine), a mechanical calculator, shown in {numref}`difference-engine`. It aimed at addressing similar tasks that were run by human computers but in a way that was automatic, faster, and error-free. Babbage was able to build just a partial prototype of this machine, and, after the first enthusiasm, he was struggled by the limited flexibility that it offered. The Difference Engine was not a programmable machine. It was able to compute only a fixed set of operations on the inputs specified physically by changing specific configurations of the machine.

In order to address these limitations, in 1837, Babbage started to devise a new machine, the [Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine), summarised in {numref}`analytical-engine`. Unfortunately, Babbage built no prototypes of this machine. However, by using it, a user could create any possible procedural calculation, making it the very first mechanical general-purpose computer in history. Furthermore, in contrast to its predecessor, the Analytical Engine received the input instructions and data using [punched cards](https://en.wikipedia.org/wiki/Punched_card). The use of such cards prevented the users from making any physical manipulation of the machine to get it working.

```{figure} images/01-analytical-engine.png
---
name: analytical-engine
---
A sketch by Babbage that describes the architecture of the Analytical Engine. Source: [The Analytical Engine: 28 Plans and Counting](http://www.computerhistory.org/atchm/httpwww-computhe-analytical-engine-28-plans-and-counting/), Computer History Museum.
```

The ideas presented in the Analytical Engine were developed in a physical machine only one century later. Computing technology has had a drastic change as a consequence of World War II. Military research ordered the construction of several calculators. For instance, the [Bombe](https://en.wikipedia.org/wiki/Bombe) (1940), designed by [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) and based on previous works by Marian Rejewski and associates {cite}`inman_rejewski_2020`, was the main instrument used by a group of people living in the secret British military camp at [Bletchley Park](https://en.wikipedia.org/wiki/Bletchley_Park) to decipher German's communications encrypted through the [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine).

The Bombe was a handy and efficient machine. However, it was still partially based on mechanical components, and it allowed their users only a specific task. Nonetheless, it was crucial from a purely historical point of view. The first fully digital computer theoretically compliant with Babbage’s Analytical Engine was developed in the United States only a few years later, in 1946. It was the[ Electronic Numerical Integrator and Computer (ENIAC)](https://en.wikipedia.org/wiki/ENIAC), shown in {numref}`eniac`, that was programmable through patch cables and switches. This invention represents one of the most important milestones of the history of computers - the fixed point in time that generated all modern computers.

```{figure} images/01-eniac.png
---
name: eniac
---
A picture of the ENIAC in the Ballistic Research Laboratory (Maryland). Source: [Wikipedia](https://en.wikipedia.org/wiki/ENIAC#/media/File:Eniac.jpg).
```

## Natural languages vs programming languages

There is an aspect of _computers_ (either humans or machines) that has not been tackled yet: which mechanism can we use to ask them to address a particular task? This aspect relates to the specific communication channel we want to adopt. For example, considering human computers, we can use the natural language (e.g. English) to instruct them in addressing specific actions.

A [natural language](https://en.wikipedia.org/wiki/Natural_language) is just an ordinary language (e.g. English), either written or oral, that has evolved naturally in humans, usually without specific and deliberate planning. As we know them, natural languages have the advantage (and, on the other hand, disadvantage) of being so expressive that particular instructions provided by using them can sound ambiguous. Consider, for instance, [the sentence “shot an elephant in your pyjamas”](https://en.wikipedia.org/wiki/List_of_linguistic_example_sentences). Does it mean one has to shoot an elephant (with a rifle) while wearing pyjamas? Or that one should shoot an elephant (with a water gun) drawn in pyjamas? We could develop specific (e.g. social) conventions that allow us to restrict the possible meaning of a situation. In the previous example, the fact that one is in a bedroom and is not living in Gabon is enough for disambiguating the sentence. While natural languages are not formal by definition, several studies in Linguistics try to provide their formalisation using some mathematical tool, e.g. {cite}`bernardi_reasoning_2002`. Even if one can formally define a natural language, its intrinsic vagueness is still present in the language itself. For instance, one cannot use mathematics (or, better, logic) for removing (all) the ambiguities from a natural language.

[Programming languages](https://en.wikipedia.org/wiki/Programming_language), on the contrary, are formal-born languages. They oblige to specific syntactic rules. Such rules avoid possible ambiguous statements, mainly by restricting the expressiveness of the language. Therefore, all the sentences in such language are conveying just one possible meaning. Usually, they are based on context-free grammars, according to Chomsky's classification introduced in Section {ref}`historic-hero`. Also, they can have a significant degree of abstraction. In particular, we can distinguish three macro-sets of programming languages.

### Machine language

[Machine language](https://en.wikipedia.org/wiki/Machine_code) is a set of instructions that can be executed directly by the [central processing unit (CPU)](https://en.wikipedia.org/wiki/Central_processing_unit) of an electronic computer. For instance, the binary executable code (i.e. a sequence of 0 and 1) defining a function (i.e. a kind of tool that takes some inputs and produces some output) for calculating the n<sup>th</sup> [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) is shown in {numref}`machine`.


```{code-block}
---
name: machine
caption: |
    The implementation in machine language of a series of instructions for calculating the n<sup>th</sup> Fibonacci number. 
---
100010110101010000100100000010001000001111111010000000000111011100000110101110000000000000000000000000000000000011000011100000111111101000000010011101110000011010111000000000010000000000000000000000001100001101010011101110110000000100000000000000000000000010111001000000010000000000000000000000001000110100000100000110011000001111111010000000110111011000000111100010111101100110001001110000010100101011101011111100010101101111000011
```

### Low-level programming languages

[Low-level programming languages](https://en.wikipedia.org/wiki/Low-level_programming_language) are languages that provide one abstraction level on top of the machine language. Thus it allows one to write programs in a way that is more intelligible to humans. The most popular language of this type is [Assembly](https://en.wikipedia.org/wiki/Assembly_language). Even if it introduces humanly recognisable symbols, one line of assembly code typically represents one machine instruction in machine language. For instance, the same function for calculating the n<sup>th</sup> Fibonacci number is defined in Assembly in {numref}`lowlevel`.

```{code-block} ca65
---
name: lowlevel
linenos: True
caption: |
    The implementation in Assembly, a well-known and used low-level programming language, of the code introduced in {numref}`machine`. Source: [Wikipedia](https://en.wikipedia.org/wiki/Low-level_programming_language#Assembly_language).
---
fib:
    movl %edi, %eax
    testl %edi, %edi
    je .return_from_fib
    cmpl $2, %edi
    jbe .return_1_from_fib
    movl %edi, %ecx
    movl $1, %edx
    movl $1, %esi
.fib_loop:
    leal (%rsi,%rdx), %eax
    cmpl $2, %ecx
    je .return_from_fib
    movl %edx, %esi
    decl %ecx
    movl %eax, %edx
    jmp .fib_loop
.return_1_from_fib:
    movl $1, %eax
.return_from_fib:
    ret
```

### High-level programming languages

[High-level programming languages](https://en.wikipedia.org/wiki/High-level_programming_language) are characterised by a strong abstraction from the specifiability of the machine language. In particular, it may use natural language words for specific constructs to be easy to use and understand by humans. Generally speaking, the more abstraction from the low-level programming languages is provided, the more understandable the language is. For instance, in {numref}`highlevel`, we show how to use the [C](https://en.wikipedia.org/wiki/C_(programming_language)) programming language for implementing the same function as before.

```{code-block} c
---
name: highlevel
linenos: True
caption: |
    The implementation in C, a well-known and used high-level programming language, of the code introduced in {numref}`lowlevel`.
---
unsigned int fib(unsigned int n) {
    if (n <= 0)
        return 0;
    else if (n <= 2)
        return 1;
    else {
        unsigned int a,b,c;
        a = 1;
        b = 1;
        while (1) {
            c = a + b;
            if (n <= 3) return c;
            a = b;
            b = c;
            n--;
        }
    }
}
```


### Implementations in natural language

We can also apply an additional level of abstraction to the previous example. For instance, we can provide natural language instructions to enable a human-computer to execute the function mentioned above. Of course, none of the macro-sets discussed above includes the natural language. However, the natural language would allow us to see how we can use an even more abstract language for instructing someone else to execute the same operation. In particular, a possible natural language description of the Fibonacci function could be:

> The function for calculating the nth Fibonacci number takes as input an integer "n". If "n" is less than or equal to 0, then 0 is returned as a result. Otherwise, if "n" is less than or equal to 2, then 1 is returned. Otherwise, in all the other cases, associate the value "1" to two distinct variables "a" and "b". Then, repeat the following operations indefinitely until a value is returned. Set the variable "c" as the sum of "a" plus "b". If "n" is less than or equal to "3" then return "c", otherwise assign the value of "b" to "a" and the value of "c" to "b", and finally decrease the value of "n" by 1 before repeating.

While the previous natural language definition maps perfectly the function defined in the machine binary code introduced above, other possible implementations of such Fibonacci function are possible. For example, one of the most famous that uses the concept of [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)) could be:

> The function for calculating the nth Fibonacci number takes as input an integer "n". If "n" is less than or equal to 0, then 0 is returned as a result. Otherwise, if "n" is equal to 1, then 1 is returned. Otherwise, return the sum of the same function with "n-1" as input and still the same function with "n-2" as input.


## Abstraction is the key

We often say that we _program_ a computer – where the word _computer_ refers to an electronic computer. However, according to the definition we have provided in this document, computers can be both humans and machines. Thus, the verb _to program_ is not very well suited when referring to human computers – we cannot program a person, can we? In this latter case, we usually say that we _talk with_ a person to instruct her to execute specific actions through a (natural) language used as a communication channel. Thus, we think that, in this context, we should use the same verbs, i.e. _to talk_ and _to instruct_, even when we refer to an electronic computer. Writing a program is precisely that: communicating to an electronic computer in a (formal) language that such an electronic computer and the human instructor can both understand {cite}`papert_mindstorms_1980`.

First, we need to agree on the language to use to communicate between us and a computer (either human or machine). Then, we can start to think about possible instructions that, if followed systematically, can return the expected result to a particular problem. To reach this goal, we (even unconsciously) try to figure out possible solutions to such a problem by comparing it with other possible recurring situations that happened in the past. The idea is to find some patterns that depict a viable solution for a set of abstractly homogeneous cases. Once found, the solution can be reused to reach our goal if it has been successful in the past. For instance, let us consider the actions that we perform at a post office. Some steps are similar to those we perform when we wait for our turn to play with a slide in the playground – as shown in {numref}`analytical-engine`.

```{figure} images/01-queues.png
---
name: queues
---
Two pictures that depict the same situation, i.e. queuing, in two different contexts: a playground (left) and a post office (right). Left photo by Prateek Rungta, source: [Flickr](https://www.flickr.com/photos/rungta/4409560365/). Right photo by Rain Rabbit, source: [Flickr](https://www.flickr.com/photos/37996583811@N01/6158491035/).
```

Considering the situations and contexts mentioned above, we call _computational thinking_ a particular approach to “solving problems, designing systems and understanding human behaviour that draws on concepts fundamental to computing” {cite}`wing_computational_2008`. Thus, computational thinking is the thought process involved when we formulate a problem and express the solution by using a language that a computer (either human or machine) can understand and execute.

Jeannette Wing provides an additional definition for clarifying what computational thinking is about {cite}`wing_computational_2008`:

> Computational thinking is a kind of analytical thinking. It shares with mathematical thinking in the general ways in which we might approach solving a problem. It shares with engineering thinking in the general ways in which we might approach designing and evaluating a large, complex system that operates within the constraints of the real world. It shares with scientific thinking in the general ways in which we might approach understanding computability, intelligence, the mind and human behaviour.

It is important to stress that computational thinking is not a new subject at all. Instead, it focuses on specific aspects concerning computer science: the founding principles and methods instead of those merely related to particular tools and systems that people (often and erroneously) associate with any computer scientist, e.g. the electronic computer {cite}`nardelli_we_2019`.

The primary notion related to computational thinking is _abstraction_: the “process of leaving out of consideration one or more properties of a complex object [...] by extracting common features from specific examples” {cite}`kramer_is_2007`. As highlighted in {numref}`queues`, the skill of abstracting situations and notions into symbols is crucial for automating task execution using a computer responsible for interpreting such abstractions. However, usually, we use these abstractions unconsciously. One of the goals of computational thinking is to _reshape_ the abstractions we have ingested as a consequence of our life experiences – that we are often unconsciously reusing. Thus, being again fully conscious of such abstractions, we can use an appropriate language to make them understandable to a computer to automatise them.

The final goal of computational thinking is to teach the basic notions of computer science to all students, independently from their academic roots. Computational thinking should complement the other thinking strategies one has already learned in the past {cite}`nardelli_we_2019`. And it applies either to academic research (including in the Humanities, e.g. see the use of computational models and techniques in History research {cite}`au_yeung_studying_2011,mullen_computational_2018,preiser-kapeller_calculating_2015`) or in real-life tasks. No one is saying that this way of thinking is the right one, of course. However, it indeed offers a complementary tool to describe reality {cite}`nardelli_we_2019`. In the future, computational thinking “will be an integral part of childhood education” {cite}`wing_computational_2008`. It will affect how people think and learn and “the way other learning takes place” {cite}`papert_mindstorms_1980`.


## References

```{bibliography}
:filter: docname in docnames
```


## Notes

[^1]: Cognitive science is concerned with the study of mind and its processes according to several interdisciplinary perspectives, including linguistics, psychology, and artificial intelligence.