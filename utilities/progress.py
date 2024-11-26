import time

def progress_bar(progress, total, start_time, scale=0.50):
    # Creates a progress bar on the command line, input is progress, total, and a present start time
    # progress and total can be any number, and this can be placed in a for or with loop
    """
    Displays a dynamic progress bar in the command line.

    This function creates a visually appealing progress bar with elapsed time and estimated remaining time, 
    which updates dynamically as progress is made. It is designed for use in loops or other iterative processes.

    Parameters:
    -----------
    progress : int or float
        The current progress value. It represents how much of the total task is completed.
    total : int or float
        The total value of the task. When `progress` equals `total`, the task is complete.
    start_time : float
        The start time of the task, typically generated using `time.time()` when the task begins.
    scale : float, optional
        A scaling factor for the progress bar width (default is 0.50). Increasing `scale` creates a longer bar.

    Output:
    -------
    Prints the progress bar to the terminal, displaying:
    - The progress bar graphic.
    - The current percentage of progress.
    - The estimated time remaining for the task.
    - The elapsed time since the task started.

    Notes:
    ------
    - The function calculates the elapsed and remaining times based on the progress rate.
    - It ensures smooth updates in a loop by using `end='\r'` to overwrite the previous line.
    """
    percent = 100 * (float(progress) / float(total))                        # Calculate the percentage of progress
    bar = '█' * round(percent*scale) + '-' * round((100-percent)*scale)     # Create the progress bar string
    elapsed_time = time.time() - start_time                                 # Calculate elapsed time
    if progress > 0:                                                        # Estimate total time and remaining time
        estimated_total_time = elapsed_time * total / progress
        remaining_time = estimated_total_time - elapsed_time
        remaining_seconds = int(remaining_time)
        remaining_milliseconds = int((remaining_time - remaining_seconds) * 1_000)
        elapsed_milliseconds = int((elapsed_time -int(elapsed_time)) * 1_000)
        remaining_str = time.strftime("%H:%M:%S", time.gmtime(remaining_seconds))
        remaining_str = f"{remaining_str}.{remaining_milliseconds:03d}"
        elapsed_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        elapsed_str = f"{elapsed_str}.{elapsed_milliseconds:03d}"
    else:
        elapsed_str   = '...'
        remaining_str = '...'
    print(f'|{bar}| {percent:.2f}% Time remaining: {remaining_str}  Time Elapsed = {elapsed_str}', end='\r')    # Print the progress bar with the remaining time
