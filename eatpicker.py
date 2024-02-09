import os
import random
from PIL import Image, ImageDraw
import pyttsx3

def load_food_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        print(f"Image file '{image_path}' not found.")
        return None

def display_category(image, category_coordinates, label):
    region_coordinates = category_coordinates
    draw = ImageDraw.Draw(image)
    draw.rectangle(region_coordinates, outline="red", width=2)
    draw.text((10, 10), label, fill="red")  # Adjust text position as needed
    image.show()

def speak_category(category):
    engine = pyttsx3.init()
    engine.say(category)
    engine.runAndWait()

def main():
    image_data = [
        {'path': 'C:\\Users\\ads\\Downloads\\PHYTON PROJECTS\\food_options_image1.png', 'label': 'Image 1'},
        {'path': 'C:\\Users\\ads\\Downloads\\PHYTON PROJECTS\\food_options_image2.png', 'label': 'Image 2'},
        {'path': 'C:\\Users\\ads\\Downloads\\PHYTON PROJECTS\\food_options_image3.png', 'label': 'Image 3'},
        # Add more images and labels as needed
    ]

    categories = {
        'pizza': (0, 0, 400, 300),   # Adjust coordinates for the "pizza" category
        'burger': (400, 0, 800, 300),  # Adjust coordinates for the "burger" category
        'salad': (800, 0, 1200, 300),  # Adjust coordinates for the "salad" category
        # Add more categories and coordinates as needed
    }

    # Randomly select an image
    selected_image_info = random.choice(image_data)
    selected_image_path = selected_image_info['path']
    selected_image_label = selected_image_info['label']

    print(f"Checking image file: {selected_image_path}")
    image = load_food_image(selected_image_path)

    if image:
        print("Image loaded successfully.")