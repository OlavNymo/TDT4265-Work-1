from manim import *
from manim_voiceover import VoiceoverScene
from ..utils.constants import *
from ..utils.voiceover import VoiceoverMixin
from ..utils.custom_animations import TypewriterText, create_brain_network

class IntroScene(VoiceoverScene):
    def construct(self):
        # Setup voiceover
        self.set_speech_service(GTTSService())

        # Create title
        title = Text("Large Multimodal Models", **title_style)
        title.move_to(TITLE_POSITION)

        # Create subtitle
        subtitle = Text("Understanding the Future of AI", **body_style)
        subtitle.move_to(SUBTITLE_POSITION)

        # Create animated icons for different data types
        icons = VGroup()
        
        # Text icon
        text_icon = Text("Aa", color=MAIN_BLUE, font_size=36)
        
        # Image icon
        image_icon = Square(side_length=1, color=SECONDARY_BLUE)
        image_icon.add(Triangle(color=SECONDARY_BLUE).scale(0.3))
        
        # Audio icon
        audio_icon = Circle(radius=0.5, color=HIGHLIGHT_COLOR)
        audio_wave = FunctionGraph(
            lambda x: 0.2 * np.sin(4 * x),
            x_range=[-1, 1],
            color=HIGHLIGHT_COLOR
        ).scale(0.5)
        audio_icon.add(audio_wave)
        
        # Video icon
        video_icon = Rectangle(height=1, width=1.6, color=TEXT_COLOR)
        play_symbol = Triangle(color=TEXT_COLOR).scale(0.3)
        video_icon.add(play_symbol)

        # Arrange icons in a circle
        icons.add(text_icon, image_icon, audio_icon, video_icon)
        icons.arrange_in_grid(2, 2, buff=1)
        icons.move_to(CONTENT_POSITION)

        # Animation sequence with voiceover
        with self.voiceover(
            """Welcome to our exploration of Large Multimodal Models, or LMMs - 
            the cutting-edge AI systems that can understand and process multiple 
            types of data simultaneously."""
        ) as tracker:
            self.play(
                Write(title),
                run_time=2
            )
            self.play(
                FadeIn(subtitle),
                run_time=1
            )
            
            # Animate icons appearing one by one with rotation
            for icon in icons:
                self.play(
                    FadeIn(icon, shift=UP),
                    Rotate(icon, angle=TAU),
                    run_time=0.7
                )

        # Create and transform into brain network
        brain_network = create_brain_network(self)
        self.play(
            Transform(icons, brain_network),
            run_time=2
        )

        # Hold the final state
        self.wait(1) 