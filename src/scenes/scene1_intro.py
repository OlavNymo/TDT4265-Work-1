from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.utils.constants import *
import numpy as np

class IntroScene(VoiceoverScene):
    def construct(self):
        # Setup voiceover
        self.set_speech_service(GTTSService())

        # Title
        title = Text("Large Multimodal Models", **title_style)
        title.move_to(TITLE_POSITION)

        # Subtitle
        subtitle = Text("Understanding the Future of AI", **body_style)
        subtitle.next_to(title, DOWN)

        # Create modality icons in circular arrangement
        modalities = VGroup()
        
        # The group should be positioned down 1 unit from the title
        modalities.move_to(subtitle.get_center() + DOWN*1)
        
        # Text modality
        text_icon = VGroup()
        text_bg = Circle(radius=0.6, fill_opacity=0.2, color=MAIN_BLUE)
        text_symbol = Text("Aa", color=MAIN_BLUE, font_size=36)
        text_icon.add(text_bg, text_symbol)
        
        # Image modality
        image_icon = VGroup()
        image_bg = Circle(radius=0.6, fill_opacity=0.2, color=SECONDARY_BLUE)
        camera_body = Rectangle(height=0.4, width=0.6, color=SECONDARY_BLUE)
        lens = Circle(radius=0.15, color=SECONDARY_BLUE)
        flash = Circle(radius=0.05, color=SECONDARY_BLUE).move_to(camera_body.get_corner(UR))
        camera = VGroup(camera_body, lens, flash)
        image_icon.add(image_bg, camera)
        
        # Audio modality
        audio_icon = VGroup()
        audio_bg = Circle(radius=0.6, fill_opacity=0.2, color=HIGHLIGHT_COLOR)
        wave = FunctionGraph(
            lambda x: 0.3 * np.sin(3 * x),
            x_range=[-1, 1],
            color=HIGHLIGHT_COLOR
        ).scale(0.5)
        audio_icon.add(audio_bg, wave)
        
        # Video modality
        video_icon = VGroup()
        video_bg = Circle(radius=0.6, fill_opacity=0.2, color=TEXT_COLOR)
        play = Triangle(fill_opacity=1, color=TEXT_COLOR).scale(0.3).rotate(90)
        video_icon.add(video_bg, play)

        # Arrange icons in a circle
        modalities.add(text_icon, image_icon, audio_icon, video_icon)
        for i, icon in enumerate(modalities):
            angle = i * TAU / 4 + PI/4  # Offset by 45 degrees
            radius = 2
            icon.move_to([radius * np.cos(angle), radius * np.sin(angle), 0])

        # Create neural pathways
        pathways = VGroup()
        for i in range(len(modalities)):
            start = modalities[i].get_center()
            end = ORIGIN
            pathway = CurvedArrow(
                start, end,
                color=MAIN_BLUE,
                stroke_width=2,
                angle=PI/4
            )
            pathways.add(pathway)

        # Create mathematical representations
        input_labels = VGroup()
        for i, label in enumerate(["x_{text}", "x_{img}", "x_{audio}", "x_{video}"]):
            math_label = MathTex(label, color=TEXT_COLOR).scale(0.8)
            angle = i * TAU / 4 + PI/4
            radius = 2.8
            math_label.move_to([radius * np.cos(angle), radius * np.sin(angle), 0])
            input_labels.add(math_label)

        # Create main equation
        equation = MathTex(
            r"\mathbf{X} = \{",
            r"x_{text},",
            r"x_{img},",
            r"x_{audio},",
            r"x_{video}",
            r"\}",
            color=TEXT_COLOR
        ).scale(1.2)
        equation.to_edge(DOWN, buff=0.8)

        # Animation sequence with voiceover
        with self.voiceover(
            """Welcome to our exploration of Large Multimodal Models, or LMMs. 
            Imagine an AI system that can understand our world in all its richness - 
            through text, images, sound, and video."""
        ):
            # Animate title and subtitle
            self.play(FadeIn(title), run_time=1)
            self.play(Write(subtitle), run_time=1)
            
            # Animate modalities appearing with fade and scale
            for icon in modalities:
                self.play(
                    FadeIn(icon, scale=1.2, shift=UP*0.3),
                    run_time=0.5
                )

        with self.voiceover(
            """As we see here, each type of data flows into the system, 
            just like our human senses work together to help us understand our environment."""
        ):
            # Animate neural pathways
            self.play(Create(pathways), run_time=2)
            
            # Add mathematical labels
            self.play(Write(input_labels), run_time=1.5)
            
            # Animate data flow with moving dots
            for pathway in pathways:
                dot = Dot(color=MAIN_BLUE)
                dot.move_to(pathway.get_start())
                self.play(
                    MoveAlongPath(dot, pathway),
                    rate_func=smooth,
                    run_time=1
                )
                self.remove(dot)

        with self.voiceover(
            """These different types of information, which we call modalities, 
            are represented mathematically as inputs X, where each x represents 
            a different type of data our model can process."""
        ):
            # Show mathematical representation with sequential writing
            self.play(Write(equation[0]), run_time=0.5)  # Write X =
            for i in range(1, len(equation)):
                self.play(Write(equation[i]), run_time=0.3)

        # Hold final state
        self.wait(1) 