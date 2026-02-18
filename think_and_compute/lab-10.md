---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(ch-lab-10)=
# Modelling data with Python classes

```{admonition} Learning objectives
:class: tip
By the end of this lab, you will be able to:
- Define Python classes with constructors and methods
- Use getter methods to access object attributes safely
- Create subclasses that extend existing classes using inheritance
- Combine multiple objects to build a simple data model
```

This lab puts into practice the concepts introduced in the [Implementation of data models via Python classes](16-data-models.ipynb) chapter. You will build a small data model for Italian Baroque painters, defining classes for artists, artworks, and galleries.

---

## Part 1: Defining your first class

In this part, you will create a class to represent artists.

### Exercise 1.1: The Artist class

Define a class `Artist` with a constructor `__init__(self, name, birth_year, nationality)` that stores these three values as attributes of the object. Add three getter methods: `get_name()`, `get_birth_year()`, and `get_nationality()`. Each method should return the corresponding attribute.

Create two instances: Caravaggio (born 1571, Italian) and Annibale Carracci (born 1560, Italian). Test each getter by printing the name, birth year, and nationality of both artists.

```{code-cell} python
:tags: [hide-cell]
class Artist(object):
    def __init__(self, name, birth_year, nationality):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality

    def get_name(self):
        return self.name

    def get_birth_year(self):
        return self.birth_year

    def get_nationality(self):
        return self.nationality

caravaggio = Artist("Caravaggio", 1571, "Italian")
carracci = Artist("Annibale Carracci", 1560, "Italian")

print(caravaggio.get_name(), "-", caravaggio.get_birth_year(), "-", caravaggio.get_nationality())
print(carracci.get_name(), "-", carracci.get_birth_year(), "-", carracci.get_nationality())
```

### Exercise 1.2: Comparing artists

Add a method `is_contemporary_of(self, other_artist)` to the `Artist` class. Two artists are considered contemporaries if the absolute difference between their birth years is 50 years or less. The method should return `True` or `False`.

Test it with:
- Caravaggio (1571) and Carracci (1560): 11 years apart, should return `True`
- Caravaggio (1571) and Gentileschi (1593): 22 years apart, should return `True`
- Caravaggio (1571) and Botticelli (1445): 126 years apart, should return `False`

```{code-cell} python
:tags: [hide-cell]
class Artist(object):
    def __init__(self, name, birth_year, nationality):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality

    def get_name(self):
        return self.name

    def get_birth_year(self):
        return self.birth_year

    def get_nationality(self):
        return self.nationality

    def is_contemporary_of(self, other_artist):
        difference = abs(self.birth_year - other_artist.get_birth_year())
        return difference <= 50

caravaggio = Artist("Caravaggio", 1571, "Italian")
carracci = Artist("Annibale Carracci", 1560, "Italian")
gentileschi = Artist("Artemisia Gentileschi", 1593, "Italian")
botticelli = Artist("Sandro Botticelli", 1445, "Italian")

print("Caravaggio and Carracci:", caravaggio.is_contemporary_of(carracci))
print("Caravaggio and Gentileschi:", caravaggio.is_contemporary_of(gentileschi))
print("Caravaggio and Botticelli:", caravaggio.is_contemporary_of(botticelli))
```

---

## Part 2: A class for artworks

Now that you have a class for artists, you will create a class to represent their artworks and a class to group artworks into a gallery.

### Exercise 2.1: The Artwork class

Define a class `Artwork` with a constructor that takes `title`, `year`, `technique`, and `artist` (an `Artist` object). Add getter methods `get_title()`, `get_year()`, `get_technique()`, and `get_artist()`. Also add a method `get_artist_name()` that returns the name of the artist by calling the `get_name()` method of the `Artist` object stored in the `artist` attribute.

Create two instances:

- *Bacco* (1597, oil on canvas, by Caravaggio)
- *Giuditta e Oloferne* (1599, oil on canvas, by Caravaggio)

Print the title, year, and artist name of each artwork.

```{code-cell} python
:tags: [hide-cell]
class Artwork(object):
    def __init__(self, title, year, technique, artist):
        self.title = title
        self.year = year
        self.technique = technique
        self.artist = artist

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_technique(self):
        return self.technique

    def get_artist(self):
        return self.artist

    def get_artist_name(self):
        return self.artist.get_name()

bacco = Artwork("Bacco", 1597, "oil on canvas", caravaggio)
giuditta = Artwork("Giuditta e Oloferne", 1599, "oil on canvas", caravaggio)

print(bacco.get_title(), "-", bacco.get_year(), "-", bacco.get_artist_name())
print(giuditta.get_title(), "-", giuditta.get_year(), "-", giuditta.get_artist_name())
```

### Exercise 2.2: The Gallery class

Define a class `Gallery` with:
- A constructor that takes a `name` (string) and initializes an empty list of artworks
- A method `add_artwork(artwork)` that appends an `Artwork` object to the list
- A method `get_artworks()` that returns a **copy** of the list of artworks
- A method `size()` that returns the number of artworks in the gallery

Create a gallery called "Caravaggio a Roma", add both artworks to it, and print its size.

```{admonition} Why return a copy?
:class: note
The method `get_artworks()` returns `list(self.artworks)` instead of `self.artworks` directly. This creates a new list containing the same elements. If we returned `self.artworks`, the caller could modify the internal list of the gallery (for example, by calling `append()` on it), bypassing the `add_artwork()` method. Returning a copy protects the internal state of the object.
```

```{code-cell} python
:tags: [hide-cell]
class Gallery(object):
    def __init__(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def get_artworks(self):
        return list(self.artworks)

    def size(self):
        return len(self.artworks)

gallery = Gallery("Caravaggio a Roma")
gallery.add_artwork(bacco)
gallery.add_artwork(giuditta)

print("Gallery:", gallery.name)
print("Number of artworks:", gallery.size())
```

---

## Part 3: Inheritance

In this part, you will create a subclass of `Artwork` to represent a specific type of artwork. When a class inherits from another, it receives all the methods and attributes of the parent class and can add new ones. If a subclass needs no extra attributes, it can simply use `pass` as its body. When it needs additional attributes, its constructor should call the parent constructor using `super().__init__()` before setting the new attributes.

### Exercise 3.1: A subclass with extra attributes

Create a class `Altarpiece` that extends `Artwork` with an additional attribute `chapel`. The constructor should accept `title`, `year`, `technique`, `artist`, and `chapel`. It should call the constructor of `Artwork` using `super().__init__()` to handle the first four parameters, then set `self.chapel`. Add a `get_chapel()` method.

Create *Vocazione di san Matteo* by Caravaggio (1600, oil on canvas, chapel: "Cappella Contarelli"). Print its title, artist name, and chapel.

```{code-cell} python
:tags: [hide-cell]
class Altarpiece(Artwork):
    def __init__(self, title, year, technique, artist, chapel):
        super().__init__(title, year, technique, artist)
        self.chapel = chapel

    def get_chapel(self):
        return self.chapel

vocazione = Altarpiece("Vocazione di san Matteo", 1600, "oil on canvas", caravaggio, "Cappella Contarelli")

print(vocazione.get_title())
print(vocazione.get_artist_name())
print(vocazione.get_chapel())
```

---

## Summary

In this lab, you practised:

- **Defining classes**: using `__init__` and `self` to create objects with attributes
- **Getter methods**: providing safe access to object attributes
- **Object composition**: storing objects as attributes of other objects (e.g., an `Artist` inside an `Artwork`)
- **Inheritance**: creating subclasses with additional attributes via `super().__init__()`

---

## Additional resources

- [Python tutorial on classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-oriented programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [How To Code in Python: Understanding Inheritance](https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python)
