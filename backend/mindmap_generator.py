import networkx as nx
import matplotlib.pyplot as plt

def create_mind_map(concepts):
    G = nx.Graph()
    
    main_topic = "Lecture"
    G.add_node(main_topic)

    for concept in concepts:
        G.add_edge(main_topic, concept)

    nx.draw(G, with_labels=True, node_color="lightblue", font_size=12)
    plt.show()

if __name__ == "__main__":
    create_mind_map(["Machine Learning", "Data Science", "Neural Networks", "Regression"])
