# Import necessary libraries
import fractal
import numpy as np
import matplotlib.pyplot as plt

# Function to generate fractal image
def generate_fractal(width, height, max_iter):
    # Generate Mandelbrot fractal
    mandelbrot = fractal.mandelbrot(width, height, max_iter)
    # Normalize fractal values to 0-255
    mandelbrot = (mandelbrot / mandelbrot.max()) * 255
    return mandelbrot

# Set parameters
width = 800  # Width of the fractal image
height = 600  # Height of the fractal image
max_iter = 256  # Maximum number of iterations

# Generate fractal image
fractal_image = generate_fractal(width, height, max_iter)

# Save fractal image to file
file_path = "fractal_image.png"
plt.imsave(file_path, fractal_image, cmap='viridis')

# Display success message
print("Fractal image generated and saved successfully!")

# Now, you can import the 'fractal_image.png' file into Power BI as an image visual.
