from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_slides(topic: str, max_slides: int, max_words: int) -> str:
    """
    Generate slides with optional small images for a given topic using Gemini API.

    Each slide is in the format:
    Slide X: Text | image: URL

    Parameters:
    - topic: Slide topic
    - max_slides: Maximum number of slides
    - max_words: Maximum words per slide

    Returns:
    - str: AI-generated slide content
    """
    prompt = f"""
You are a teaching compression system that creates concise educational slides with optional relevant visuals.
Topic: {topic}
Rules:
- Each slide = 1 concise sentence
- Max {max_slides} slides
- Max {max_words} words per slide
- Include optional small image URL relevant to slide content
- Output format:
Slide 1: Text here | image: URL
Slide 2: Text here | image: URL
Stop after {max_slides} slides.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        if not hasattr(response, "text") or not response.text.strip():
            raise RuntimeError("Empty response from AI model.")
        return response.text

    except Exception as e:
        raise RuntimeError(f"Slide generation failed: {str(e)}")
