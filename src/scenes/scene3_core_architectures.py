from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from src.utils.constants import *

class CoreArchitecturesScene(VoiceoverScene):
    def construct(self):
        # Setup voiceover
        self.set_speech_service(GTTSService())
        
        # Title
        title = Text("Core Architectures", color=TEXT_COLOR).to_edge(UP)
        subtitle = Text("Two Approaches to Multimodal Processing", color=TEXT_COLOR, font_size=24)
        subtitle.next_to(title, DOWN)

        with self.voiceover(
            """LMMs can be built in two main ways. Let's explore these different architectural approaches
            and understand their unique characteristics."""
        ):
            self.play(
                Write(title),
                Write(subtitle),
                run_time=2
            )

        # Setup initial elements for encoder-decoder
        self.setup_encoder_decoder()
        
        with self.voiceover(
            """The first approach, which we call Encoder-Decoder, is like having specialist translators 
            for each type of data, who then work together to create understanding. Watch how each colored 
            path represents a different type of data being processed by its expert."""
        ):
            self.animate_encoder_decoder_flow()

        with self.voiceover(
            """Each encoder transforms its input into a specialized representation, shown here as feature vectors.
            These representations capture the essential characteristics of each modality."""
        ):
            self.show_feature_vectors()

        with self.voiceover(
            """The second approach, Single-Tower, is more like having one super-translator who can handle 
            all types of data directly. Notice how in this case, everything flows through the same pathway 
            but gets processed together."""
        ):
            self.setup_and_animate_single_tower()

        with self.voiceover(
            """Each approach has its advantages - specialists can be very precise, while the generalist 
            approach can find unexpected connections between different types of information."""
        ):
            self.show_comparison()

        # Clean transition out
        self.clean_transition()

    def setup_encoder_decoder(self):
        # Input boxes setup
        self.input_boxes = VGroup()
        colors = [BLUE, RED, GREEN, PURPLE]
        labels = ["Text", "Image", "Audio", "Video"]
        
        for i, (color, label) in enumerate(zip(colors, labels)):
            box = Rectangle(width=2, height=1, color=color, fill_opacity=0.3)
            box.move_to(LEFT * (6 - i * 2.5))
            text = Text(label, font_size=24).next_to(box, DOWN)
            self.input_boxes.add(VGroup(box, text))
        
        self.input_boxes.to_edge(DOWN, buff=1)
        
        # Create encoders
        self.encoders = VGroup()
        for i, box in enumerate(self.input_boxes):
            encoder = Rectangle(width=1.5, height=2, color=box[0].get_color(), fill_opacity=0.2)
            encoder.next_to(box, UP, buff=1)
            label = Text("Encoder", font_size=20).next_to(encoder, DOWN)
            self.encoders.add(VGroup(encoder, label))
        
        # Create fusion decoder
        self.fusion_decoder = RegularPolygon(n=6, color=WHITE)
        self.fusion_decoder.scale(1.5)
        self.fusion_decoder.to_edge(UP, buff=1)
        self.decoder_label = Text("Fusion Decoder", font_size=24).next_to(self.fusion_decoder, DOWN)
        
        # Initial fade in
        self.play(
            *[Create(box) for box in self.input_boxes],
            run_time=2
        )
        self.play(
            *[Create(encoder) for encoder in self.encoders],
            Create(self.fusion_decoder),
            Write(self.decoder_label),
            run_time=2
        )

    def animate_encoder_decoder_flow(self):
        # Animate data flow from inputs to encoders to fusion
        for encoder in self.encoders:
            # Input to encoder flow
            start = encoder[0].get_bottom()
            end = encoder[0].get_top()
            path = Line(start, end)
            dot = Dot(color=encoder[0].get_color())
            self.play(
                MoveAlongPath(dot, path),
                run_time=1,
                rate_func=linear
            )
            
            # Encoder to fusion flow
            fusion_path = Line(
                encoder[0].get_top(),
                self.fusion_decoder.get_bottom()
            )
            self.play(
                Create(fusion_path),
                run_time=0.5
            )
            self.play(
                MoveAlongPath(dot, fusion_path),
                run_time=1,
                rate_func=linear
            )

    def show_feature_vectors(self):
        # Add feature vectors next to encoders
        for encoder in self.encoders:
            vector = MathTex(
                "[0.2, 0.5, 0.8]",
                color=encoder[0].get_color()
            ).scale(0.7)
            vector.next_to(encoder[0], RIGHT)
            self.play(
                Write(vector),
                run_time=0.8
            )

    def setup_and_animate_single_tower(self):
        # Move encoder-decoder to left
        encoder_decoder_group = VGroup(
            self.input_boxes,
            self.encoders,
            self.fusion_decoder,
            self.decoder_label
        )
        
        self.play(
            encoder_decoder_group.animate.shift(LEFT * 4),
            run_time=2
        )
        
        # Create VS text
        vs_text = Text("VS", font_size=36)
        vs_text.move_to(ORIGIN)
        self.play(Write(vs_text))
        
        # Create single tower
        tower = Rectangle(width=3, height=6)
        tower.set_fill(color=BLUE_E, opacity=0.3)
        tower.set_stroke(color=WHITE)
        tower.to_edge(RIGHT, buff=2)
        
        # Add internal layers
        layers = VGroup()
        for i in range(4):
            layer = Line(
                tower.get_left() + UP * (1.5 - i),
                tower.get_right() + UP * (1.5 - i),
                color=WHITE
            )
            label = Text("Shared Layer", font_size=16).next_to(layer, RIGHT)
            layers.add(VGroup(layer, label))
        
        self.play(
            Create(tower),
            run_time=1
        )
        
        self.play(
            *[Create(layer) for layer in layers],
            run_time=2
        )
        
        # Animate tokens
        tokens = VGroup()
        colors = [BLUE, RED, GREEN, PURPLE]
        for i, color in enumerate(colors):
            token = Square(side_length=0.3, color=color, fill_opacity=0.5)
            token.move_to(tower.get_bottom() + UP * 0.5 + RIGHT * (-1 + i * 0.5))
            tokens.add(token)
        
        self.play(
            *[FadeIn(token, shift=UP) for token in tokens],
            run_time=2,
            lag_ratio=0.2
        )

    def show_comparison(self):
        # Add comparison labels
        specialized = Text("Specialized Processing", font_size=24)
        specialized.to_edge(LEFT, buff=1)
        specialized.shift(UP * 2)
        
        unified = Text("Unified Processing", font_size=24)
        unified.to_edge(RIGHT, buff=1)
        unified.shift(UP * 2)
        
        self.play(
            Write(specialized),
            Write(unified),
            run_time=2
        )
        
        # Add arrows pointing to architectures
        arrow1 = Arrow(specialized.get_bottom(), LEFT * 4)
        arrow2 = Arrow(unified.get_bottom(), RIGHT * 4)
        
        self.play(
            Create(arrow1),
            Create(arrow2),
            run_time=1.5
        )

    def clean_transition(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        ) 