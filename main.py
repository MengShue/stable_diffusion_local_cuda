
import argparse
import torch
from diffusers import StableDiffusionPipeline
from datetime import datetime

# Setting CPU or GPU as main drawing process unit
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Using device: {device}")

# Setup commandline args
def parse_args():
    parser = argparse.ArgumentParser(description="Generate images using Stable Diffusion.")
    parser.add_argument("-d", "--description", type=str, required=True, help="The description for the image generation.")
    parser.add_argument("-m", "--model", type=str, default="CompVis/stable-diffusion-v1-4", help="The model to use for image generation.")
    return parser.parse_args()

# Generate image and save
def generate_image(description, model_name):
    # Loading pre-trained model and switch to GPU/CPU
    pipe = StableDiffusionPipeline.from_pretrained(model_name)
    pipe = pipe.to(device)

    # Generate Image
    image = pipe(description).images[0]

    # Save file and timestamp as image name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"generated_image_{timestamp}.png"

    # Save file
    image.save(output_filename)
    print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    # Analyze args
    args = parse_args()

    # Generate image and save
    generate_image(args.description, args.model)
