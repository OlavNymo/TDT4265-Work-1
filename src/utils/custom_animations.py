from manim import *
from .constants import *

class TypewriterText(Text):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def create_animation(self, run_time=2):
        return AddTextLetterByLetter(self, run_time=run_time)

class FadeInFromPoint(Animation):
    def __init__(self, mobject, point, **kwargs):
        self.point = point
        super().__init__(mobject, **kwargs)

    def create_starting_mobject(self):
        start = self.mobject.copy()
        start.scale(0)
        start.move_to(self.point)
        return start

class PulsatingObject(Animation):
    def __init__(self, mobject, scale_factor=1.2, **kwargs):
        self.scale_factor = scale_factor
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        scale = 1 + (self.scale_factor - 1) * np.sin(alpha * 2 * np.pi)
        self.mobject.scale_to_fit_height(self.starting_mobject.get_height() * scale)

def create_brain_network(scene):
    """Creates an animated brain network visualization"""
    # Create nodes
    nodes = VGroup()
    connections = VGroup()
    
    # Create 6 nodes in a circular pattern
    radius = 2
    num_nodes = 6
    for i in range(num_nodes):
        angle = i * 2 * PI / num_nodes
        position = radius * np.array([np.cos(angle), np.sin(angle), 0])
        node = Circle(radius=0.2, color=MAIN_BLUE, fill_opacity=0.8)
        node.move_to(position)
        nodes.add(node)
    
    # Create connections between nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if np.random.random() < 0.5:  # 50% chance of connection
                start = nodes[i].get_center()
                end = nodes[j].get_center()
                line = Line(start, end, stroke_width=2, color=SECONDARY_BLUE)
                connections.add(line)
    
    return VGroup(connections, nodes)

def create_flowing_data(scene, start, end, color=MAIN_BLUE):
    """Creates flowing data visualization between two points"""
    path = Line(start, end)
    dot = Dot(color=color)
    dot.move_to(start)
    
    return MoveAlongPath(dot, path, rate_func=linear)

def create_hexagonal_grid(scene, n_rows=3, n_cols=3):
    """Creates a hexagonal grid of circles"""
    hex_group = VGroup()
    hex_radius = 0.5
    
    for i in range(n_rows):
        for j in range(n_cols):
            x = (j + (i % 2) * 0.5) * 1.7 * hex_radius
            y = i * 1.5 * hex_radius
            hexagon = RegularPolygon(n=6, radius=hex_radius, color=MAIN_BLUE)
            hexagon.move_to([x, y, 0])
            hex_group.add(hexagon)
    
    # Center the grid
    hex_group.move_to(ORIGIN)
    return hex_group 