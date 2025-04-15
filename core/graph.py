from core.generate_graph import generate_graph
from core.visualize_graph import visualize_graph


def process_image(input_image):
    try:
        graph = generate_graph(input_image)
        output_image = visualize_graph(graph)
        return output_image
    except Exception as e:
        return None