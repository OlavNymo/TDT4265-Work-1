#!/usr/bin/env python3
import sys
from manim import *
from pathlib import Path
import argparse

# Import all scenes
from scenes.scene1_intro import IntroScene
from scenes.scene2_what_are_lmms import WhatAreLMMsScene
from scenes.scene3_architecture import ArchitectureScene
from scenes.scene4_training import TrainingScene
from scenes.scene5_applications import ApplicationsScene
from scenes.scene6_challenges import ChallengesScene
from scenes.scene7_future import FutureScene
from scenes.scene8_conclusion import ConclusionScene

# Scene mapping
SCENES = {
    'intro': IntroScene,
    'what_are_lmms': WhatAreLMMsScene,
    'architecture': ArchitectureScene,
    'training': TrainingScene,
    'applications': ApplicationsScene,
    'challenges': ChallengesScene,
    'future': FutureScene,
    'conclusion': ConclusionScene
}

def main():
    parser = argparse.ArgumentParser(description='Render LMM educational video scenes')
    parser.add_argument('--scene', type=str, help='Specific scene to render')
    parser.add_argument('--quality', type=str, default='production',
                       choices=['production', 'medium_quality', 'low_quality'],
                       help='Quality of the render')
    args = parser.parse_args()

    # Set up the configuration
    config.background_color = WHITE
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