# Image to Binary Converter

This Python script converts images to binary format. It uses Python's image processing libraries to read an image file and convert it into a binary representation.

## Usage

1. **Clone or Download Repository:**
   Clone or download this repository to your local machine.

2. **Install Dependencies:**
   Make sure you have Python 3.x installed on your system. Install the required dependencies by running:
   ```
   pip install pillow
   pip install image
   ```

3. **Specify Image Path and Dimensions:**
   Open the `imageToBinary` script in a text editor. Replace `"path\\to\\image"` with the path to your image file. Use double backslashes (`\\`) instead of single backslashes (`\`).
   ```
   image_path = "path\\to\\image"
   ```
   Specify the desired width (`x`) and height (`y`) of the output image that will be displayed.
   ```
   x = 32  # Specify the width of the image
   y = 32  # Specify the height of the image
   ```

4. **Run the Script:**
   In order to get any results just press the Run button in your IDE.
   
6. **View Binary Representation:**
   The script will print the binary representation of the resized image to the console.

## Notes

- Ensure that the image file exists at the specified path and that it is accessible.
- The script converts the image to a binary representation using the specified dimensions (`x` and `y`). It resizes the image accordingly before converting it to binary format.
- The binary representation consists of 0s and 1s, where each pixel in the image is represented by a binary value based on its intensity or color.

## Dependencies

- Python 3.x
- Pillow (Python Imaging Library)

---

