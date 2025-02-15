import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def latexfont():
    plt.rcParams.update({
        'text.usetex' : True,
        'font.family' : 'serif',
        'font.size' : 12
    })
latexfont()
# Load the star data
starfile = r'data\bright_stars.csv'
star_pos = pd.read_csv(starfile)

vmag_lim = 8
print(np.max(star_pos['Vmag']))
# Filter stars with Vmag < 4.0
filtered_stars = star_pos[star_pos['Vmag'] <= vmag_lim].copy() # 4.5 seems ideal

# Extract filtered data
ra = 360 - filtered_stars['RA_2000_Deg']
dec = filtered_stars['Dec_2000_Deg']
magnitude = filtered_stars['Vmag']
spectra = filtered_stars['Spct']

# Convert magnitude to size using an exponential scale (brighter stars = larger dots)
dot_size = 10 ** (-magnitude / 2.5)  # Adjust to control size scaling
dot_size = dot_size * 50  # Scale for visualization

# Map spectral types to colors (approximate)
spectral_colors = {
    'W': 'blue', # Wolf Rayet stars
    'O': 'blue',      # Hot, blue stars
    'B': 'lightblue',
    'A': 'white',     # White stars
    'F': 'lightyellow',
    'G': 'yellow',    # Yellow stars (like the Sun)
    'K': 'orange',    # Orange stars
    'M': 'red'        # Cool, red stars
}
# Map spectral types to colors and handle missing values
filtered_stars.loc[:, 'Color'] = filtered_stars['Spct'].map(spectral_colors).fillna('gray')
print(filtered_stars)

# Create the scatter plot
plt.figure(figsize=(12, 6),dpi = 100)
plt.scatter(
    ra, dec,
    s=dot_size,
    facecolors='white',  # White inside color
    edgecolors=filtered_stars['Color'],  # Colored edges
    linewidth=0.7,  # Thickness of the edge
    alpha=0.9
)

# Set plot limits
xlims = (0,  360)
ylims = (-90, 90)
# xlims = (275.94-30, 275.94+30)
# ylims = (-1.2-30,-1.2+30)
plt.xlim(*xlims)
plt.ylim(*ylims)


# Add grid, labels, and title
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlabel(r'Right Ascension (RA) [$^\circ$]')
plt.ylabel(r'Declination (Dec) [$^\circ$]')
plt.title(r'\textbf{Star Chart [BSC]}')
dx = 10
plt.xticks(np.arange(xlims[0], xlims[1]+dx, dx), rotation = 90)
plt.yticks(np.arange(ylims[0], ylims[1]+dx, dx))

# Set background color
plt.gca().set_facecolor('black')
plt.gca().set_aspect('equal')

# Show the plot
plt.tight_layout()
plt.savefig(r'data\star_map_45.png')
plt.show()