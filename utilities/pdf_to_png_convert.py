import os
import converters
import progress
import time
from pdf2image import convert_from_path

input_folder = r'data\steps_pdf'
output_folder = r'data\steps_png'

os.makedirs(output_folder, exist_ok=True)
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
for file in pdf_files:
    print(file)
time_start = time.time()
for i, pdf_file in enumerate(pdf_files):
    progress.progress_bar(i,len(pdf_files),time_start)
    pdf_path = os.path.join(input_folder, pdf_file)
    png_filename = os.path.splitext(pdf_file)[0] + ".png"  # Use the PDF title for the PNG
    png_path = os.path.join(output_folder, png_filename)

    # Skip if the PNG already exists
    if os.path.exists(png_path):
        print(f"Skipping {pdf_file}: {png_filename} already exists.")
        continue

    try:
        # Convert the single-page PDF to PNG
        images = convert_from_path(pdf_path, dpi=300)
        if len(images) != 1:
            raise ValueError(f"The file {pdf_file} contains more than one page.")

        # Save the converted image
        images[0].save(png_path, "PNG")
        print(f"Converted {pdf_file} to {png_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_file}: {e}")
