from dataclasses import dataclass
from pathlib import Path


@dataclass()
class StoryTellerConfig:
    story: str = "Unicorn Earth"
    output_dir: str = Path(__file__).parent.parent / "out"
    nsfw_check: bool = False
    seed: int = 42
    num_images: int = 10

    writer: str = "gpt2"
    writer_device: str = "cuda:0"
    max_new_tokens: int = 50
    writer_prompt_prefix: str = (
        f"Acting as a story teller. Tell a fascinating, {num_images} sentence story from begining to end about the following:\n"
    )
    writer_prompt: str = "Once upon a time, unicorns roamed the Earth."

    painter: str = "stabilityai/stable-diffusion-2-1"
    painter_device: str = "cuda:0"
    image_size: int = 512
    painter_prompt_prefix: str = "beautiful painting"
    painter_prompt_postfix: str = "\n\n"

    speaker: str = "tts_models/en/ljspeech/glow-tts"
