import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
import io


def visualize_graph(graph):
    try:
        G = nx.DiGraph()

        for node in graph.nodes:
            G.add_node(node.id, label=node.label, color=node.color)

        for edge in graph.edges:
            G.add_edge(edge.source, edge.target, label=edge.label, color=edge.color)

        pos = nx.spring_layout(G, k=0.9, iterations=50)

        plt.figure(figsize=(14, 10))
        plt.title("Enhanced Home Layout Visualization", fontsize=16, fontweight='bold')

        # Enhance node appearance
        node_colors = [mcolors.to_rgba(node[1]['color'], alpha=0.8) for node in G.nodes(data=True)]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, edgecolors='gray', linewidths=2)

        # Improve label rendering
        labels = {node[0]: node[1]['label'] for node in G.nodes(data=True)}
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')

        # Enhance edge appearance
        edge_colors = [mcolors.to_rgba(edge[2]['color'], alpha=0.6) for edge in G.edges(data=True)]
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, arrowsize=20)

        # Improve edge label rendering
        edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='darkblue')

        plt.axis('off')
        plt.tight_layout()

        # Create a color to room type mapping
        color_to_room = {}
        for node in G.nodes(data=True):
            color = node[1]['color']
            room = node[1]['label']
            if color not in color_to_room:
                color_to_room[color] = room

        # Add a legend with color names and corresponding room types
        legend_elements = [
            plt.Line2D(
                [0], [0], marker='o', color='w',
                label=f"{color}: {room}",
                markerfacecolor=color, markersize=10)
            for color, room in color_to_room.items()
        ]
        
        plt.legend(handles=legend_elements, title="Room Types", loc='best', fontsize=8)

        # Save the image with higher DPI
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png', dpi=300, bbox_inches='tight')
        img_buf.seek(0)
        return Image.open(img_buf)
    except Exception as e:
        raise
