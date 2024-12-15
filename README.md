# Stable Diffusion Image Generator

This project allows you to generate images using the Stable Diffusion model via a command-line interface (CLI). You can specify a description and a model of your choice, and the generated image will be saved with a timestamped filename.

## Testing System Specifications

- **OS**: Ubuntu 24.04
- **GPU**: NVIDIA RTX 4060
- **CPU**: Intel® Core™ i5-12400 (12 cores)

## Installation

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.10+
- `pip` for package management
- NVIDIA drivers for your own GPU and CUDA support

### Install Required Python Libraries

You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

Note: If you're using the GPU, ensure that you have the correct CUDA version installed. You can check if PyTorch detects your GPU using:
```bash
import torch
print(torch.cuda.is_available())  # Should return True if CUDA is properly configured
```

## Usage
Once the dependencies are installed, you can run the image generation script by specifying a description and optionally a model. The image will be saved automatically with a timestamped filename.

Example Command
```bash
python main.py -d "man walk into universe" -m "stable-diffusion-v1-5/stable-diffusion-v1-5"
```
Parameters:
- `-d` or `--description`: The description for the image generation (required).
- `-m` or `--model`: The model to use for image generation (optional, default is "CompVis/stable-diffusion-v1-4").

The generated image will be saved with the filename format generated_image_YYYYMMDD_HHMMSS.png.

## Performance Comparison
- GPU (NVIDIA RTX 4060)

  - Command: `python main.py -d "man walk into universe"`
  - Time: ~13 seconds

- CPU (Intel® Core™ i5-12400, 12 cores)

  - Command: `python main.py -d "man walk into universe"`
  - Time: Over 12 minutes

Using the GPU for image generation results in a significant speedup compared to using the CPU.
