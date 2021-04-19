from typing import List, Iterator, Set


class Vertice:
    def __init__(self, index):
        self.neigh: Set[Vertice] = set()
        self.color = 0
        self.index = index
    def connect(self, other: "Vertice"):
        self.neigh.add(other)
        other.neigh.add(self)
    def get_neigh(self) -> Set["Vertice"]:
        return self.neigh

class Graph:
    def __init__(self, matrix: List[List[str]]):
        self.vertices: List[Vertice] = [Vertice(i) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == "1"):
                    self.add_edge(self.vertices[i], self.vertices[j])
    def add_edge(self, vertice1: Vertice, vertice2: Vertice):
        vertice1.connect(vertice2)


    def traverse_color(self, from_vertice: Vertice) -> bool:
        color_other = from_vertice.color * -1
        for v in from_vertice.get_neigh():
            if v.color == from_vertice.color:
                return False
            if v.color == color_other:
                continue
            v.color = color_other
            self.traverse_color(v)
        return True
    def get_uncolored(self):
        vs = list(filter(lambda x: x.color == 0, self.vertices))
        if (len(vs) == 0):
            return None
        else:
            return vs[0]
    def get_by_color(self):
        return [[i for i in self.vertices if i.color == 1],
                [i for i in self.vertices if i.color == -1]]








if __name__ == '__main__':
    filein = open("input.txt", "r")
    graph: Graph = Graph([filein.readline().split(" ") for i in range(int(filein.readline()))])
    result = True
    while graph.get_uncolored() != None:
        beg = graph.get_uncolored()
        beg.color = 1
        result &= graph.traverse_color(beg)
    file = open("output.txt", "w")
    if result is False:
        print("N", file=file)
    else:
        print("Y", file=file)
        r = graph.get_by_color()
        d1 = sorted(map(lambda x: x.index, r[0]))
        d2 = sorted(map(lambda x: x.index, r[1]))
        res = sorted([d1, d2], key= lambda x: min(x))
        print(" ".join(map(lambda x: str(x), res[0])), file=file)
        print(0, file=file)
        print(" ".join(map(lambda x: str(x), res[1])), file=file)
    file.close()