from core.graph import process_image
from dotenv import load_dotenv
import gradio as gr
import traceback
import logging

load_dotenv('.env')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Image(type="pil"),
    title="Image to Knowledge Graph",
    description="Upload an image to generate a knowledge graph representation."
)
 
# Launch the app
if __name__ == "__main__":
    try:
        iface.launch()
    except Exception as e:
        logger.error(f"Error launching Gradio interface: {str(e)}")
        logger.error(traceback.format_exc())