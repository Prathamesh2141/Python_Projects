
from sketchpy import Canvas

def main():
    # Specify the path to the image you want to sketch
    image_path = "ironman.png"

    # Create a Canvas object and load the image
    canvas = Canvas(width=800, height=600)  # Adjust the canvas size as needed
    canvas.sketch_from_image(image_path)

    # Draw the sketch on the canvas
    canvas.draw()

if __name__ == "__main__":
    main()