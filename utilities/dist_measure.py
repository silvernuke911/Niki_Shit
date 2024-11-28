import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def px_distance(p1, p2, w_px=2480/210):
    """
    Function to measure the distance in millimeters between the paws and toes and such

    Input:
        int:   p1   - first point pixel xy coordinates
        int:   p2   - second point pixel xy coordinates
        float: w_px - pixels per millimeter of the image, default is 2480/210, the image width in px 
                      and the ISO standard mm width of A4 paper
        
    Output:
        float: d_mm - distance between the points in mm, 0.01 mm precision 
    
    Note:
        From w_px, on average, each measurement has an uncertainty of 0.04 mm
    """
    x1, y1 = tuple(p1)
    x2, y2 = tuple(p2)
    xl_px = np.abs(x1 - x2)
    yl_px = np.abs(y1 - y2)
    r_px = np.linalg.norm([xl_px, yl_px])
    r_mm = r_px / w_px
    d_mm = f'{r_mm:.2f}'

    return d_mm

def record_and_measure_with_enter(image_path):
    # Load and display the image
    img = mpimg.imread(image_path)
    scale = 2
    fig, ax = plt.subplots(figsize = (2.1*scale, 2.97*scale))
    ax.imshow(img)
    #ax.set_title("Hover and press Enter to record points")
    ax.set_xlabel('$x$ (px)')
    ax.set_ylabel('$y$ (px)')
    clicks = []  # Store cursor positions
    lines = []
    dots = []

    def on_key_press(event):
        if event.key == "enter":  # Check if Enter is pressed
            if event.xdata is not None and event.ydata is not None:
                x, y = int(event.xdata), int(event.ydata)
                clicks.append((x, y))
                # Draw a dot at the recorded position and store the dot
                dot = ax.scatter(x, y, marker='.', s=2, color='k')
                dots.append(dot)  # Store the dot object
                plt.draw()  # Update the plot to display the dot

                if len(clicks) == 2:
                    # Get the two points
                    p1, p2 = clicks
                    # Calculate the distance
                    distance = px_distance(p1, p2)
                    print(f"Distance: {distance} mm")

                    # Draw a line between the points and store the line object
                    line, = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', linewidth=0.75)
                    lines.append(line)  # Add the line to the list
                    plt.draw()  # Update the plot

                    clicks.clear()  # Reset for the next measurement

        elif event.key == "z" and lines:
            # Remove the last line and corresponding dot
            last_line = lines.pop()
            last_line.remove()
            last_dot = dots.pop()
            last_dot.remove()
            plt.draw()  # Update the plot after removing the line and dot

        elif event.key == "c":
            # Clear all lines and dots
            while lines:
                line = lines.pop()
                line.remove()
            while dots:
                dot = dots.pop()
                dot.remove()
            plt.draw()  # Update the plot after clearing all lines and dots

    # Connect the key press event to the handler
    fig.canvas.mpl_connect('key_press_event', on_key_press)
    plt.show()

# Example usage
image_path = r'data\steps_png\NO5W1.png'  # Image path
record_and_measure_with_enter(image_path)
