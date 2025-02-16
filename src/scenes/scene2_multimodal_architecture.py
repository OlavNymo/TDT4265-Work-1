from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.utils.constants import *
import numpy as np
import random

class MultimodalArchitectureScene(VoiceoverScene):
    def construct(self):
        # Setup voiceover
        self.set_speech_service(GTTSService())

        # Title
        title = Text("Multimodal Architecture", color=TEXT_COLOR).to_edge(UP)
        subtitle = Text("Translation of Different Data Types", color=TEXT_COLOR, font_size=24)
        subtitle.next_to(title, DOWN)

        # Create input examples
        def create_input_box(content, label_text, color):
            box = VGroup()
            bg = RoundedRectangle(
                height=1.5, width=2.5,
                corner_radius=0.1,
                fill_opacity=0.2,
                stroke_color=color,
                fill_color=color
            )
            label = Text(label_text, color=color, font_size=20).next_to(bg, UP, buff=0.1)
            content.move_to(bg)
            box.add(bg, content, label)
            return box

        # Text input example
        text_input = Text("A dog playing", color=GREEN, font_size=20)
        text_box = create_input_box(text_input, "Text", GREEN)

        # Image input example (simplified dog image using shapes)
        dog_image = VGroup()
        # Body
        body = Circle(radius=0.3, fill_opacity=0.8, color=BLUE)
        # Head
        head = Circle(radius=0.2, fill_opacity=0.8, color=BLUE)
        head.next_to(body, RIGHT, buff=-0.1)
        # Ears
        ear1 = Triangle(fill_opacity=0.8, color=BLUE).scale(0.2)
        ear2 = ear1.copy()
        ear1.next_to(head, UP+LEFT, buff=-0.1)
        ear2.next_to(head, UP+RIGHT, buff=-0.1)
        dog_image.add(body, head, ear1, ear2)
        image_box = create_input_box(dog_image, "Image", BLUE)

        # Audio input example (waveform)
        audio_wave = FunctionGraph(
            lambda x: 0.3 * np.sin(3 * x) * np.exp(-0.5 * x**2),
            x_range=[-2, 2],
            color=RED
        ).scale(0.5)
        audio_box = create_input_box(audio_wave, "Audio", RED)

        # Arrange inputs
        input_group = VGroup(text_box, image_box, audio_box)
        input_group.arrange(RIGHT, buff=0.8)
        input_group.next_to(subtitle, DOWN, buff=0.8)

        # Create embedding representations
        def create_embedding(color):
            embedding = VGroup()
            # Vector representation as a column of numbers
            for i in range(5):
                num = DecimalNumber(
                    random.uniform(-1, 1),
                    num_decimal_places=2,
                    color=color,
                    font_size=16
                )
                num.move_to([0, -i*0.3, 0])
                embedding.add(num)
            return embedding

        # Create embeddings for each input
        text_embedding = create_embedding(GREEN)
        image_embedding = create_embedding(BLUE)
        audio_embedding = create_embedding(RED)

        # Create embedding boxes
        embeddings_group = VGroup()
        for emb, color in [(text_embedding, GREEN), (image_embedding, BLUE), (audio_embedding, RED)]:
            box = Rectangle(
                height=1.8, width=1,
                stroke_color=color,
                fill_opacity=0.1,
                fill_color=color
            )
            emb.move_to(box)
            group = VGroup(box, emb)
            embeddings_group.add(group)

        embeddings_group.arrange(RIGHT, buff=0.8)
        embeddings_group.next_to(input_group, DOWN, buff=1.5)

        # Create unified representation space
        unified_space = VGroup()
        # Background sphere
        sphere = Sphere(
            radius=1.5,
            fill_opacity=0.1,
            stroke_width=1,
            stroke_color=WHITE
        )
        
        # Vector points in unified space
        points = VGroup()
        for _ in range(15):
            theta = random.uniform(0, TAU)
            phi = random.uniform(0, PI)
            r = random.uniform(1, 1.5)
            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)
            point = Dot3D([x, y, z], color=WHITE)
            points.add(point)
        
        unified_space.add(sphere, points)
        unified_space.next_to(embeddings_group, DOWN, buff=1)

        # Animation sequence
        with self.voiceover(
            """The magic of LMMs lies in how they process these different types of information. 
            Think of it like translation - each type of data speaks its own language, and our 
            model needs to translate everything into a common language it can understand."""
        ):
            self.play(
                Write(title),
                Write(subtitle),
                run_time=2
            )
            
            # Show input examples
            self.play(
                *[FadeIn(box, shift=UP) for box in input_group],
                run_time=2
            )

        # Show translation process
        with self.voiceover(
            """As we see here, text becomes word embeddings, images are broken down into 
            meaningful features, and audio becomes frequency patterns."""
        ):
            # Transform inputs into embeddings with traces
            for input_box, emb_group in zip(input_group, embeddings_group):
                # Create flowing dots
                dots = VGroup(*[Dot(color=input_box[1].get_color()) for _ in range(5)])
                dots.arrange(RIGHT, buff=0.1)
                dots.next_to(input_box, DOWN)
                
                self.play(
                    FadeIn(dots),
                    run_time=0.3
                )
                
                self.play(
                    ReplacementTransform(dots, emb_group),
                    run_time=1
                )

        # Show unification in embedding space
        with self.voiceover(
            """Notice how all these different forms of data gradually transform into a similar format - 
            this is what we call embedding space, where our model can understand and connect 
            information from all sources together."""
        ):
            # Create flowing paths to unified space
            paths = VGroup()
            for emb_group in embeddings_group:
                path = ArcBetweenPoints(
                    emb_group.get_bottom(),
                    unified_space.get_top() + UP * 0.5,
                    angle=-TAU/4
                )
                paths.add(path)
            
            self.play(
                Create(unified_space),
                run_time=1
            )
            
            # Animate embeddings flowing into unified space
            for path in paths:
                dot = Dot(color=WHITE)
                dot.move_to(path.get_start())
                self.play(
                    MoveAlongPath(dot, path),
                    run_time=0.8
                )
                self.remove(dot)

            # Show connections in unified space
            for _ in range(3):
                start_point = random.choice(points)
                end_point = random.choice(points)
                line = DashedLine(
                    start_point.get_center(),
                    end_point.get_center(),
                    color=YELLOW,
                    dash_length=0.1
                )
                self.play(
                    Create(line),
                    run_time=0.5
                )

        # Example of understanding
        example_text = Text("'A dog'", color=GREEN, font_size=20)
        example_text.to_edge(LEFT)
        arrow = Arrow(LEFT, RIGHT, color=WHITE)
        arrow.next_to(example_text, RIGHT)
        understanding = Text("✓ Matched!", color=YELLOW, font_size=20)
        understanding.next_to(arrow, RIGHT)

        with self.voiceover(
            """For example, when we input the text 'a dog' and an image of a dog, 
            the model can understand they refer to the same concept."""
        ):
            self.play(
                Write(example_text),
                GrowArrow(arrow),
                Write(understanding),
                run_time=2
            )

        # Hold final state
        self.wait(1) 