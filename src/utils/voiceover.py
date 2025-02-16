from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from pathlib import Path

# Configure default voiceover service
default_voiceover_service = GTTSService(
    language="en",
    tld="com",  # Top level domain for accent (com = US)
    pitch=1.0,  # Default pitch
    speed=1.0,  # Default speed
)

class VoiceoverMixin:
    """Mixin to add voiceover capabilities to any scene"""
    def setup_voiceover(self):
        """Configure voiceover for the scene"""
        self.voiceover_config.update({
            "rate": "+0%",  # Can be adjusted for speed
            "voice_dir": Path("assets/audio"),
        })
        self.set_speech_service(default_voiceover_service)

    def start_voiceover(self, text):
        """Start a voiceover section"""
        return self.voiceover(text)

# Singleton instance
voice_over = VoiceOver() 