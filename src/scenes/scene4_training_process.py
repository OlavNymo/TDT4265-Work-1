#!/usr/bin/env python3
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.utils.constants import *

class TrainingProcessScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # Pre-training Phase Narration and Animation
        top_nodes = VGroup(*[Circle(radius=0.3, color=YELLOW, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT, buff=0.5)
        mid_nodes = VGroup(*[Circle(radius=0.3, color=BLUE, fill_opacity=0.5) for _ in range(3)]).arrange(RIGHT, buff=0.8)
        bottom_nodes = VGroup(*[Circle(radius=0.3, color=GREEN, fill_opacity=0.5) for _ in range(5)]).arrange(RIGHT, buff=0.5)
        top_nodes.to_edge(UP, buff=1)
        mid_nodes.move_to(ORIGIN)
        bottom_nodes.to_edge(DOWN, buff=1)

        with self.voiceover("In the pre-training phase, we set up the network structure—a series of nodes arranged in three layers representing the model's foundational learning."):
            self.play(Create(top_nodes), run_time=1)
            self.play(Create(mid_nodes), run_time=1)
            self.play(Create(bottom_nodes), run_time=1)

        # Connect top to middle and middle to bottom
        connections1 = VGroup(*[Line(top.get_center(), mid.get_center(), stroke_width=1, stroke_opacity=0.3)
                                 for top in top_nodes for mid in mid_nodes])
        connections2 = VGroup(*[Line(mid.get_center(), bot.get_center(), stroke_width=1, stroke_opacity=0.3)
                                 for mid in mid_nodes for bot in bottom_nodes])
        with self.voiceover("Next, notice how connections form between the layers, simulating how the model begins to understand relationships between data points."):
            self.play(Create(connections1), run_time=2)
            self.play(Create(connections2), run_time=2)

        # Data Stream Animation: Create data source containers on left side
        image_box = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.5)
        text_box = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.5)
        audio_box = Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.5)
        boxes = VGroup(image_box, text_box, audio_box).arrange(DOWN, buff=0.3)
        boxes.to_edge(LEFT, buff=1)
        with self.voiceover("Now, we represent data sources as containers on the left, symbolizing image, text, and audio inputs."):
            self.play(FadeIn(boxes), run_time=1)

        # Streaming Animation: Animate small icons representing data
        dog_image = Circle(radius=0.2, color=BLUE, fill_opacity=1)  # placeholder for dog's image
        dog_text = Text("Dog", font_size=24, color=GREEN)
        sound_icon = Square(side_length=0.4, color=RED, fill_opacity=1)  # placeholder for sound icon

        # Set starting positions near their respective boxes
        dog_image.move_to(image_box.get_right() + RIGHT * 0.5)
        dog_text.move_to(text_box.get_right() + RIGHT * 0.5)
        sound_icon.move_to(audio_box.get_right() + RIGHT * 0.5)
        
        # Define target as the network center (ORIGIN)
        target = ORIGIN
        
        # Create curved paths for the icons
        path_image = ArcBetweenPoints(dog_image.get_center(), target, angle=PI/4)
        path_text = ArcBetweenPoints(dog_text.get_center(), target, angle=-PI/4)
        path_sound = ArcBetweenPoints(sound_icon.get_center(), target, angle=PI/6)

        with self.voiceover("Observe how data icons—representing the dog's image, its label, and a sound icon—move from the data sources to the network center, symbolizing data integration."):
            self.play(MoveAlongPath(dog_image, path_image), run_time=1)
            self.play(MoveAlongPath(dog_text, path_text), run_time=1)
            self.play(MoveAlongPath(sound_icon, path_sound), run_time=1)
            self.play(FadeOut(dog_image), FadeOut(dog_text), FadeOut(sound_icon), run_time=0.5)

        # Connection Formation: Highlight one network connection with a flash effect
        if connections1:
            with self.voiceover("Notice the highlighted connection—this flash effect emphasizes a key moment when the model starts associating related concepts."):
                self.play(ShowPassingFlash(connections1[0].copy(), time_width=0.5, color=YELLOW), run_time=1)

        # Loss Curve Animation: Create axes and a decreasing loss curve at bottom right
        axes = Axes(x_range=[0, 10, 1], y_range=[0, 5, 1], x_length=4, y_length=3,
                    axis_config={"color": WHITE}).to_edge(DR, buff=1)
        labels = axes.get_axis_labels(x_label=Text("Training Time", font_size=24),
                                        y_label=Text("Learning Progress", font_size=24))
        def loss_function(x):
            return 4 - 0.4 * x

        with self.voiceover("The loss curve represents the model's learning progress over time, decreasing as training improves performance."):
            self.play(Create(axes), Write(labels), run_time=2)
            loss_curve = axes.plot(
                loss_function,
                x_range=[0, 8],
                color=HIGHLIGHT_COLOR
            )
            self.play(Create(loss_curve), run_time=2)

        # Instruction Tuning Phase: Create a split screen effect
        input_box = Rectangle(width=3, height=4, color=BLUE, fill_opacity=0.3).to_edge(LEFT, buff=1)
        output_box = Rectangle(width=3, height=4, color=GREEN, fill_opacity=0.3).to_edge(RIGHT, buff=1)
        input_label = Text("Input", font_size=24).move_to(input_box.get_top() + UP * 0.5)
        output_label = Text("Output", font_size=24).move_to(output_box.get_top() + UP * 0.5)
        with self.voiceover("Finally, in the instruction tuning phase, a split screen shows the input instructions on the left and the model's responses on the right, illustrating refined behavior."):
            self.play(FadeIn(input_box), FadeIn(output_box), run_time=1)
            self.play(Write(input_label), Write(output_label), run_time=1)

        self.wait(2) 