import os
from PIL import Image
import numpy as np

def clean_images(input_folder, output_folder, threshold=(220, 220, 220)):
    """
    Process images in the input folder, replace colors above the threshold with white,
    and save the cleaned images in the output folder.

    Parameters:
    -----------
    input_folder : str
        Path to the folder containing the input images.
    output_folder : str
        Path to the folder where cleaned images will be saved.
    threshold : tuple of int
        RGB threshold (default: (220, 220, 220)).

    Returns:
    --------
    None
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        try:
            # Open the image
            img = Image.open(input_path)
            img_array = np.array(img)

            # Ensure the image is RGB
            if len(img_array.shape) == 2:  # Grayscale
                img_array = np.stack([img_array] * 3, axis=-1)
            
            # Replace colors above the threshold with white
            mask = (img_array[..., 0] > threshold[0]) & \
                   (img_array[..., 1] > threshold[1]) & \
                   (img_array[..., 2] > threshold[2])
            img_array[mask] = [255, 255, 255]

            # Save the cleaned image
            cleaned_img = Image.fromarray(img_array.astype('uint8'))
            cleaned_img.save(output_path)
            print(f"Processed and saved: {output_path}")
        except Exception as e:
            print(f"Failed to process {image_file}: {e}")

input_folder = r"data\steps_png"         # Folder with noisy images
output_folder = r"data\steps_png_clean" # Folder for cleaned images
clean_images(input_folder, output_folder)