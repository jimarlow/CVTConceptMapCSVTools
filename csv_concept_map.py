import graphviz # pip install graphviz
import csv

class Element:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

class Concept(Element):
    def __init__(self, id, name ):
        super().__init__(id)
        self.name = name

    def __repr__(self):
        return f"Concept({self.id}, {self.name})"

class LinkingWords(Element):
    def __init__(self, id, name ):
        super().__init__(id)
        self.name = name

    def __repr__(self):
        return f"Link({self.id}, {self.name})"

class DirectedEdge(Element):
    def __init__(self, start, end ):
        super().__init__(start + end)
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Edge({self.id}, {self.start}, {self.end})"

class ConceptMap:
    def __init__(self, title):
        self.title = title
        self.concepts = set()
        self.linking_words = set()
        self.edges = set()
        self.dot = None

    def add_concept(self, concept):
        self.concepts.add(concept)

    def add_linking_words(self, link):
        self.linking_words.add(link)

    def add_directed_edge(self, edge):
        self.edges.add(edge)

    def from_file(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 3:
                    self.add_proposition_elements(row[0].strip(), row[1].strip(), row[2].strip())

    def add_proposition_elements(self, concept1, linking_words, concept2):
        # Add the concepts.
        # The id (first argument) and name (second argument) are the same.
        self.add_concept(Concept(concept1, concept1))
        self.add_concept(Concept(concept2, concept2))

        # Add the linking_words
        # The linking_words_id is the concept1 name prepended to the linking_words name
        linking_words_id = concept1 + linking_words
        self.add_linking_words(LinkingWords(linking_words_id, linking_words))

        # Add the edge from concept1->linking_words
        self.add_directed_edge(DirectedEdge(concept1, linking_words_id))
        # Add the edge from linking_words->concept2
        self.add_directed_edge(DirectedEdge(linking_words_id, concept2))

    # Graph layout engines:
    # 'dot'         hierarchical - default
    # 'neato'       spring model
    # 'fdp'         force-directed
    # 'circo'       circular
    # 'twopi'       radial
    # 'osage'       for cluster / partition visualizations
    # 'patchwork'   for cluster / partition visualizations
    def render(self, format="png", engine='dot'):
        # Also "svg", "pdf"
        self.dot = graphviz.Digraph()
        for concept in self.concepts:
            self.dot.node(concept.id, concept.name, shape='rect', style='rounded,filled', fillcolor='lightblue')
        for link in self.linking_words:
            self.dot.node(link.id, link.name, shape='plaintext')
        for edge in self.edges:
            self.dot.edge(edge.start, edge.end)
        self.dot.render(self.title, view=True, format=format, engine=engine)  # Saves and opens the image