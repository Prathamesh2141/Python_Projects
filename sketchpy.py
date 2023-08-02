from sketchpy import canvas

def main():
    # Specify the path to the image you want to sketch
    image_path = r"C:\Users\prath\Desktop\Python_Projects\ironman.png"

    # Create a Canvas object and load the image
    # canvas = Canvas(width=800, height=600)  # Adjust the canvas size as needed
    obj=canvas.sketch_from_image(image_path)

    # Draw the sketch on the canvas
    obj.draw()

if __name__ == "__main__":
    main()