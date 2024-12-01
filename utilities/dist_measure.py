import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import csv 

def transpose_csv(file_name):
    # Read data from the CSV file
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Flatten the data (if it's stored in multiple columns/rows)
    flat_data = [item for sublist in data for item in sublist]

    # Group the data into rows of three
    transposed_data = [flat_data[i:i+3] for i in range(0, len(flat_data), 3)]

    # Rewrite the CSV file with transposed data
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(transposed_data)

    print(f"The file '{file_name}' has been updated with transposed data.")

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


def update_csv(value, file_name="foots.csv"):
    # Check if 'd' is pressed to delete the last entry
    if value == 'd':
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                lines = file.readlines()
            if lines:  # Ensure there are lines to delete
                with open(file_name, "w") as file:
                    file.writelines(lines[:-1])  # Write all lines except the last one
                print("Last entry deleted.")
            else:
                print("The file is empty. Nothing to delete.")
        else:
            print("The file does not exist. Nothing to delete.")
    else:
        # Append the new value to the file
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([value])
            # print(f"Added '{value}' to {file_name}.")

def open_excel_file(file_name):
    # This will open the Excel file with the default program (Excel)
    #excel_path = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
    print('Opening excel...')
    os.startfile(file_name)

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
                    update_csv(distance,'foots.csv')

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
        
        elif event.key == "d":
            update_csv("d")
        elif event.key == 'n':
            update_csv("---")
            update_csv("---")
            update_csv("---")
            print('New foot')
    # Connect the key press event to the handler
    fig.canvas.mpl_connect('key_press_event', on_key_press)
    plt.show()

# Example usage
image_path = r'data\steps_png\S5W2.png'  # Image path
record_and_measure_with_enter(image_path)
update_csv("---")
update_csv("---")
update_csv("---")
transpose_csv('foots.csv')
open_excel_file('foots.csv')
