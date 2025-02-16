# Large Multimodal Models - Educational Video

An educational video project about Large Multimodal Models (LMMs) created using Manim animation library.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── storyboard.md
├── src/
│   ├── scenes/
│   │   ├── scene1_intro.py
│   │   ├── scene2_what_are_lmms.py
│   │   ├── scene3_architecture.py
│   │   ├── scene4_training.py
│   │   ├── scene5_applications.py
│   │   ├── scene6_challenges.py
│   │   ├── scene7_future.py
│   │   └── scene8_conclusion.py
│   ├── utils/
│   │   ├── constants.py
│   │   ├── voiceover.py
│   │   └── custom_animations.py
│   └── main.py
└── assets/
    ├── audio/
    └── images/
```

## Setup Instructions

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install system dependencies for Manim:
   - On MacOS: `brew install cairo ffmpeg`
   - On Ubuntu: `sudo apt install libcairo2-dev ffmpeg`
   - On Windows: Follow [Manim installation guide](https://docs.manim.community/en/stable/installation/windows.html)

## Running the Project

To render the complete video:

```bash
python src/main.py
```

To render individual scenes:

```bash
python src/main.py --scene SceneName
```

## Project Description

This educational video explores Large Multimodal Models (LMMs), covering their architecture, capabilities, and future directions. The video is created using the Manim animation library and includes:

- Animated illustrations of LMM concepts
- Text overlays and explanations
- Synthetic voice narration
- Synchronized animations and transitions

The content is structured into 8 main scenes, each focusing on different aspects of LMMs, making the complex topic accessible and engaging for students.
