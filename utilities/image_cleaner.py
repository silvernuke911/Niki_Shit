import os
import time
from PIL import Image
from PIL import Image, ImageEnhance
import numpy as np
import progress

def clean_images(input_folder, output_folder, threshold=(210, 210, 210)):
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
    time_start = time.time()
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    for i,image_file in enumerate(image_files):
        progress.progress_bar(i, len(image_files), time_start)
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
        except Exception as e:
            print(f"Failed to process {image_file}: {e}")

    output_files = [f for f in os.listdir(output_folder) if f.endswith('.png')]
    print('')
    for output_file in output_files:
        print(f"Processed and saved: {output_file}")

def increase_contrast(image_path, output_path, contrast_factor=1.5):
    """
    Increases the contrast of an image and saves the enhanced image.

    Parameters:
    -----------
    image_path : str
        Path to the input image.
    output_path : str
        Path to save the contrast-enhanced image.
    contrast_factor : float
        Factor by which to enhance the contrast. Default is 1.5 (50% increase).
        Values:
            - 1.0: Original contrast.
            - >1.0: Higher contrast.
            - <1.0: Lower contrast.

    Returns:
    --------
    None
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Enhance the contrast
        enhancer = ImageEnhance.Contrast(img)
        img_contrasted = enhancer.enhance(contrast_factor)
        
        # Save the enhanced image
        img_contrasted.save(output_path)
        print(f"Contrast increased and saved to: {output_path}")
    except Exception as e:
        print(f"Error enhancing contrast for {image_path}: {e}")

input_folder = r"data\steps_png"         # Folder with noisy images
output_folder = r"data\steps_png_clean"  # Folder for cleaned images
clean_images(input_folder, output_folder)