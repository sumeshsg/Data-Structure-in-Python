class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def set_neighbour(self, v, w):
        self.neighbours.append((v, w))


class Graph(object):
    vertices = {}

    def add_vertex(self, v):
        if v.name not in self.vertices.keys():
            self.vertices[v.name] = v
            return True

    def add_edge(self, v1_name, v2_name, w=0):
        if v1_name in self.vertices.keys() and v2_name in self.vertices.keys():
            v1 = self.vertices.get(v1_name)
            v2 = self.vertices.get(v2_name)
            v1.set_neighbour(v2, w)
            v2.set_neighbour(v1, w)
        return False

    def get_graph(self):
        for key, val in self.vertices.items():
            childes = ''
            for neighbour in val.neighbours:
                childes += f'({neighbour[0].name}:{neighbour[1]})'
            print(f'{key}:{childes}')


if __name__ == '__main__':
    v_a = Vertex('A')
    v_b = Vertex('B')
    v_c = Vertex('C')
    v_d = Vertex('D')
    v_e = Vertex('E')

    graph = Graph()
    for v in [v_a, v_b, v_c, v_d, v_e]:
        graph.add_vertex(v)

    for e in ['AB', 'AC', 'AE', 'BD', 'CE']:
        graph.add_edge(e[:1], e[1:])

    graph.get_graph()
