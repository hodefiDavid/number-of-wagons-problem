import functools
import random

import networkx as nx
import matplotlib.pyplot as plt

random.seed(1)


def plotlive(func):
    plt.ion()

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        # Clear all axes in the current figure.
        axes = plt.gcf().get_axes()
        for axis in axes:
            axis.cla()

        # Call func to plot something
        result = func(*args, **kwargs)

        # Draw the plot
        plt.draw()
        plt.pause(0.01)

        return result

    return new_func


@plotlive
def drawG():
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=300,
                           node_color=[c[1]["color"] for c in G.nodes.data()])
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=G.edges(), width=1)
    nx.draw_networkx_labels(G, pos, ax=ax)


# get random color, yellow or gray
def get_rnd_color():
    if random.randint(0, 1):
        return "yellow"
    return "gray"


G = nx.Graph()
num_of_v = 20
plt.figure(figsize=(5, 5))
ax = plt.gca()
ax.set_title('Random graph')
_ = ax.axis('off')

for i in range(num_of_v):
    G.add_node(i, color=get_rnd_color())

for i in range(num_of_v):
    G.add_edge(i, (i + 1) % num_of_v)

pos = nx.circular_layout(G)

notfound = True
whereAmI = 0
index = 0
G.nodes[whereAmI]['color'] = "yellow"
while notfound:
    whereAmI = (whereAmI + 1) % num_of_v
    index += 1
    G.nodes[whereAmI]['color'] = "red"
    drawG()
    G.nodes[whereAmI]['color'] = "gray"
    drawG()
    tnpcol = G.nodes[0]['color']
    G.nodes[0]['color'] = "green"
    drawG()
    G.nodes[0]['color'] = tnpcol

    if G.nodes[whereAmI - whereAmI]["color"] == "gray":
        notfound = False

print("num of wagon is ", index)

plt.show()
