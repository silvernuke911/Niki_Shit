from pdf2image import convert_from_path

def pdf_to_png(pdf_path, png_path, dpi=300):
    """
    Convert a single-page PDF to a PNG image.

    Parameters:
    -----------
    pdf_path : str
        Path to the input PDF file (assumes the PDF contains a single page).
    png_path : str
        Path where the output PNG file will be saved, including the filename (e.g., "output.png").
    dpi : int, optional
        Resolution of the output PNG image (default is 300 DPI).

    Returns:
    --------
    None
    """
    # Convert the single-page PDF to an image
    images = convert_from_path(pdf_path, dpi=dpi)

    # Ensure the PDF has only one page
    if len(images) != 1:
        raise ValueError("The provided PDF must be a single-page document.")

    # Save the single image as a PNG file
    images[0].save(png_path, "PNG")
    print(f"Saved PNG to {png_path}")
