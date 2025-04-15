# Plan2Graph

A tool for converting floor plans and layout images into interactive knowledge graphs.

## Overview

Plan2Graph uses AI to analyze images of floor plans, generating a detailed knowledge graph that visualizes the relationships between rooms, doors, windows, and other architectural elements. The application creates a graphical representation showing how different spaces connect and relate to each other.

## Features

- Convert floor plan images to knowledge graphs
- Visualize spatial relationships between rooms
- Identify entrances, exits, and pathways between spaces
- Generate labeled nodes and edges to represent rooms and connections
- Color-coded visualization for easy interpretation

## Requirements

- Python 3.8+
- OpenAI API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plan2graph.git
   cd plan2graph
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create an environment file:
   ```bash
   cp .env.example .env
   ```

4. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://127.0.0.1:7860)

3. Upload a floor plan image through the Gradio interface

4. The application will process the image and display a knowledge graph visualization

## How It Works

1. The application takes an input image containing a floor plan
2. It processes the image using OpenAI's vision capabilities
3. AI analyzes the image and extracts information about rooms and their relationships
4. A knowledge graph is generated with nodes (rooms) and edges (connections)
5. The graph is visualized using NetworkX and Matplotlib

## Project Structure

- `app.py` - Main application file with Gradio interface
- `core/` - Core functionality modules
  - `generate_graph.py` - Handles the AI-based graph generation
  - `visualize_graph.py` - Creates visual representation of the graph
  - `graph.py` - Manages the image processing pipeline
  - `uitility.py` - Utility functions

