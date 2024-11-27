import numpy as np

def px_distance(p1,p2, w_px = 2480/210):
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
    
    x1,y1 = tuple(p1)
    x2,y2 = tuple(p2)
    xl_px = np.abs(x1-x2)
    yl_px = np.abs(y1-y2)
    r_px  = np.linalg.norm([xl_px,yl_px])
    r_mm  = r_px / w_px
    d_mm  = np.round(r_mm,2)

    return d_mm