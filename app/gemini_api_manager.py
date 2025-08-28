import os
import itertools
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiApiManager:
    """
    Manages a pool of Gemini API keys and provides a method to get the next key in a round-robin fashion.
    """
    def __init__(self):
        # Retrieve keys from environment variable, split by comma, and remove any whitespace
        keys_str = os.getenv("GEMINI_API_KEYS", "")
        self.api_keys = [key.strip() for key in keys_str.split(',') if key.strip()]
        
        if not self.api_keys:
            raise ValueError("GEMINI_API_KEYS environment variable is not set or is empty.")
        
        # Use itertools.cycle to create a generator that cycles through the keys indefinitely
        self.key_iterator = itertools.cycle(self.api_keys)
        self.current_key = next(self.key_iterator)

    def get_next_key(self):
        """
        Rotates to the next API key in the pool and returns it.
        """
        self.current_key = next(self.key_iterator)
        return self.current_key

# Create a single instance of the manager to be used throughout the application
api_manager = GeminiApiManager()