import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import os

# ---- CONFIG ----
IMAGE_PATH = 'Test.JPG'

# Constants (Must match image size)
WIDTH = 6080
HEIGHT = 3040

# Store clicks
points = []
line_artists = []
text_artists = []

def onkey(event):
    if len(line_artists) > 0 and len(text_artists) > 0:
        if event.key == 'c':
            print("🔄 Clearing all lines and labels...\n")
            # Remove all line and text artists
            for line in line_artists:
                line.remove()
            for text in text_artists:
                text.remove()
            line_artists.clear()
            text_artists.clear()
            
        elif event.key == 'backspace':
            print("🔄 Removing last line and label...\n")
            # Remove last line and text artists
            line_artists[-1].remove()
            text_artists[-1].remove()
            line_artists.pop()
            text_artists.pop()

        fig.canvas.draw()

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        print(f"Clicked at: ({x}, {y})")
        points.append((x, y))
        
        if len(points) == 2:
            # Calculate angular distance
            ang_distance = calculate_angular_distance(points[0], points[1])

            # Draw line between the points
            x1, y1 = points[0]
            x2, y2 = points[1]
            line = mlines.Line2D([x1, x2], [y1, y2], color='yellow', linewidth=2)
            ax.add_line(line)
            line_artists.append(line)  # save for later removal

            # Add angular distance as text at midpoint
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            text = ax.text(mid_x, mid_y, f"{ang_distance:.2f}°", color='cyan',
                           fontsize=14, weight='bold', bbox=dict(facecolor='black', alpha=0.5))
            text_artists.append(text)

            fig.canvas.draw()
            points.clear()

def calculate_angular_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Convert to spherical coordinates
    theta1 = (x1 / WIDTH) * 360
    phi1 = 90 - (y1 / HEIGHT) * 180

    theta2 = (x2 / WIDTH) * 360
    phi2 = 90 - (y2 / HEIGHT) * 180

    print(f"\nPoint 1: Azimuth={theta1:.2f}°, Altitude={phi1:.2f}°")
    print(f"Point 2: Azimuth={theta2:.2f}°, Altitude={phi2:.2f}°")

    # Convert to radians
    theta1_rad = math.radians(theta1)
    phi1_rad = math.radians(phi1)
    theta2_rad = math.radians(theta2)
    phi2_rad = math.radians(phi2)

    # Spherical law of cosines
    cos_dsigma = (
        math.sin(phi1_rad) * math.sin(phi2_rad) +
        math.cos(phi1_rad) * math.cos(phi2_rad) * math.cos(theta1_rad - theta2_rad)
    )
    dsigma_rad = math.acos(cos_dsigma)

    # Convert to degrees
    angular_distance = math.degrees(dsigma_rad)
    print(f"\n🌕 Angular distance: {angular_distance:.2f} degrees\n")

    return angular_distance

# --- Load image ---
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"\n❌ ERROR: Cannot find image file '{IMAGE_PATH}' in the current folder.\n")

# Use matplotlib to load (more reliable)
img = mpimg.imread(IMAGE_PATH)

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(img)
ax.set_title('Click 2 points to measure the angular distance between them.')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
kid = fig.canvas.mpl_connect('key_press_event', onkey)
plt.show()
