import re
import glob
import os

FILENAME = './data.js'


class Data:
    def __init__(self):
        self.p1_files = []
        self.p2_files = []
        self.p3_files = []

        self.p1_nodes = {}
        self.p1_edges = {}

        self.p2_nodes = {}
        self.p2_edges = {}

        self.p3_nodes = {}
        self.p3_edges = {}

        self.get_files()

        self.read_files(self.p1_files, self.p1_nodes, self.p1_edges)
        self.read_files(self.p2_files, self.p2_nodes, self.p2_edges)
        self.read_files(self.p3_files, self.p3_nodes, self.p3_edges)

        if os.path.exists(FILENAME):
            os.remove(FILENAME)

    def get_files(self):

        for file in glob.glob("*.html"):
            if file.startswith("p1_"):
                self.p1_files.append(file)
            elif file.startswith("p2_"):
                self.p2_files.append(file)
            elif file.startswith("p3_"):
                self.p3_files.append(file)

        self.p1_files.sort()
        self.p2_files.sort()
        self.p3_files.sort()

    @staticmethod
    def read_files(in_files, in_nodes, in_edges):

        ni = 1
        ei = 1

        for file in in_files:
            reader = open(file, 'r')

            while True:
                line = reader.readline().strip()

                if line.startswith("nodes"):
                    s = line[line.find("["):line.find("]")+1]
                    in_nodes[ni] = s
                    ni += 1
                elif line.startswith("edges"):
                    s = line[line.find("["):line.find("]")+1]
                    in_edges[ei] = s
                    ei += 1
                    break
            reader.close()

    @staticmethod
    def write_files(data, var_name):

        with open(FILENAME, 'a+') as file:
            file.write("\n")

        start = 'var {} = {{'.format(var_name)
        end = '};'
        content = ""
        for key, val in data.items():
            content += "{}: {},".format(key, val)

        with open(FILENAME, 'a+') as f:
            f.write(start + content + end)


d = Data()
d.write_files(d.p1_nodes, "play1_nodes_dict")
d.write_files(d.p1_edges, "play1_edges_dict")

d.write_files(d.p2_nodes, "play2_nodes_dict")
d.write_files(d.p2_edges, "play2_edges_dict")

d.write_files(d.p3_nodes, "play3_nodes_dict")
d.write_files(d.p3_edges, "play3_edges_dict")
