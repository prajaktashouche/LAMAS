from pyvis.network import Network


class Edges:
    def __init__(self, node1=None, node2=None, color=None):
        self.from_node_id = node1
        self.to_node_id = node2
        self.color = color

    def show_edge(self):
        print("from:{}, to:{}, color:{}".format(self.from_node_id, self.to_node_id, self.color))


class Node:

    def __init__(self, nodes=None, edges=None):
        self.net = Network()
        self.worlds = nodes     # dict
        self.edges = []         # List(Edges)

        self.get_edges(edges)

    @staticmethod
    def get_net_options():
        return '''var options = {
            "configure": {
                "enabled": false
            },
            "nodes": {
                "font": {
                    "size": 18
                }
            },
            "edges": {
                "arrows": {
                    "to": {
                        "enabled": true,
                        "scaleFactor": 0.3
                    }
                },
                "color": {
                    "inherit": true
                },
                "smooth": {
                "enabled": false,
                "type": "continuous"
                }
            },
            "interaction": {
                "dragNodes": true,
                "hideEdgesOnDrag": false,
                "hideNodesOnDrag": false
            },
            "physics": {
                "hierarchicalRepulsion": {
                    "centralGravity": 0
                },
                "minVelocity": 0.75,
                "solver": "hierarchicalRepulsion"
            }
        }
        '''

    def get_edges(self, edges):
        for e in edges:
            f, t, c = edges[e]
            self.edges.append(Edges(f, t, c))

    def add_net_nodes(self):
        text = '''<div>(
                <span style="color:{};">{}</span><span style="color:{};">&{};</span>
                <span style="color:{};">{}</span><span style="color:{};">&{};</span>
                )</div>'''

        suit_dict = {'H': 'hearts', 'S': 'spades'}
        color_dict = {'H': 'red', 'S': 'black'}

        root_color = 'MediumSlateBlue'
        real_color = 'MediumVioletRed'

        # Add root nodes, possible worlds
        for root_id in self.worlds:

            # code to generate the cards html for each world
            title = ""
            for player in self.worlds[root_id]:
                c1, c2 = list(player)
                title += text.format(color_dict[c1[1]], c1[0], color_dict[c1[1]], suit_dict[c1[1]], color_dict[c2[1]],
                                     c2[0], color_dict[c2[1]], suit_dict[c2[1]])

            # change color of real world
            if root_id == 0:
                self.net.add_node(root_id, label="w{}".format(root_id), title=title, color=root_color, shape="ellipse")
            else:
                self.net.add_node(root_id, label="w{}".format(root_id), title=title, color=root_color, shape="ellipse")

    def add_net_edges(self):

        for e in self.edges:
            self.net.add_edge(e.from_node_id, e.to_node_id, color=e.color)

    def show_kripke_model(self):

        # Add nodes, worlds
        self.add_net_nodes()

        # Add edges, relations
        self.add_net_edges()

        # Modify network options
        self.net.set_options(self.get_net_options())

        # display graph
        self.net.show('announcement.html')

        # save graph
        # self.net.save_graph('graph.html')



