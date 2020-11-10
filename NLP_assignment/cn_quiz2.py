import networkx as nx
from pylab import show


nodes = 9
edges = 12
do_not_want = 3
def edge_gen_1(nodes,edges,do_not_want):
    group = nodes // (do_not_want+1)
    aviliable_v = nodes % (do_not_want+1)
    aviliable_e = edges - group*(do_not_want+1)
    edge = []
    for i in range(group):
        # print(i*(do_not_want+1),'---')
        for j in range(do_not_want):
            # print(i*(do_not_want+1)+j)
            edge.append([i*(do_not_want+1)+j,i*(do_not_want+1)+j+1])
        edge.append([(i+1) * (do_not_want + 1) - 1,i *(do_not_want + 1),])

print(edge)

print(group,aviliable_v,aviliable_e)


# G = nx.Graph()
#
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(3,4)
#
# nx.draw(G,node_color='green',node_size=300,with_labels=True)
# show()