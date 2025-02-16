#!/usr/bin/env python3
import sys
from manim import *
from pathlib import Path
import argparse

# Import all scenes
from src.scenes.scene1_intro import IntroScene
from src.scenes.scene2_multimodal_architecture import MultimodalArchitectureScene
from src.scenes.scene3_core_architectures import CoreArchitecturesScene
from src.scenes.scene4_training_process import TrainingProcessScene

# Scene mapping
SCENES = {
    'intro': IntroScene,
    'multimodal_architecture': MultimodalArchitectureScene,
    'core_architectures': CoreArchitecturesScene,
    'training_process': TrainingProcessScene,
}

def main():
    parser = argparse.ArgumentParser(description='Render LMM educational video scenes')
    parser.add_argument('--scene', type=str, help='Specific scene to render')
    parser.add_argument('--quality', type=str, default='production_quality',
                       choices=['fourk_quality', 'production_quality', 'high_quality', 
                               'medium_quality', 'low_quality', 'example_quality'],
                       help='Quality of the render')
    args = parser.parse_args()

    # Set up the configuration
    config.background_color = BLACK
    config.frame_width = 16
    config.frame_height = 9
    config.pixel_width = 1920
    config.pixel_height = 1080
    config.quality = args.quality

    if args.scene:
        if args.scene not in SCENES:
            print(f"Scene {args.scene} not found. Available scenes: {', '.join(SCENES.keys())}")
            sys.exit(1)
        scene_class = SCENES[args.scene]
        scene = scene_class()
        scene.render()
    else:
        # Render all scenes in sequence
        for scene_name, scene_class in SCENES.items():
            print(f"Rendering scene: {scene_name}")
            scene = scene_class()
            scene.render()

if __name__ == "__main__":
    main() 