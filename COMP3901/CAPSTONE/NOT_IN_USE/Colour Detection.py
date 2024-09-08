#DETECTS COLOURS
import cv2
import numpy as np

def bgr_to_colour_name(bgr_colour):
    '''
    Converts a BGR colour to a human-readable colour name using predefined colour mappings.

    Args:
        bgr_colour (tuple): BGR colour tuple in the format (B, G, R), where B, G, and R are integers in the range 0-255.

    Returns:
        str: The corresponding colour name based on predefined mappings, or 'Unknown' if no match is found.
    '''
    # Define colour name mappings for various BGR colours
    colour_names = {
        (0, 0, 0): 'Black',         # B
        (255, 255, 255): 'White',   # W
        (0, 0, 255): 'Red',         # Primary
        (0, 255, 0): 'Green',       # Primary
        (255, 0, 0): 'Blue',        # Primary
        (0, 255, 255): 'Yellow',    # Secondary
        (255, 0, 255): 'Magenta',   # Secondary
        (255, 255, 0): 'Cyan',      # Secondary
        (0, 128, 255): 'Orange',    # Tertiary
        (255, 128, 0): 'Brown',     # Tertiary
        (128, 0, 255): 'Purple',    # Tertiary
        (255, 0, 128): 'Pink',      # Tertiary
        (128, 255, 0): 'Lime',      # Tertiary
        (0, 255, 128): 'Teal',       # Tertiary
        (128, 128, 128): 'Gray',
        (255, 255, 255): 'White',
        (0, 0, 0): 'Black',
        (128, 0, 0): 'Maroon',
        (0, 128, 0): 'Olive',
        (128, 0, 128): 'Purple',
        (128, 128, 0): 'Olive Green',
        (0, 128, 128): 'Teal Green',
        (128, 0, 64): 'Rose',
        (0, 128, 64): 'Moss Green',
        
        # Shades of Blue
        (0, 0, 128): 'Navy Blue',
        (0, 0, 205): 'Medium Blue',
        (0, 0, 139): 'Dark Blue',
        (0, 0, 255): 'Electric Blue',
        
        # Shades of Green
        (0, 100, 0): 'Dark Green',
        (0, 128, 0): 'Green (RGB)',
        (34, 139, 34): 'Forest Green',
        (60, 179, 113): 'Medium Sea Green',
        
        # Shades of Yellow
        (218, 165, 32): 'Goldenrod',
        (255, 215, 0): 'Gold',
        (255, 255, 102): 'Lemon Yellow',
        (255, 255, 0): 'Yellow (RGB)',
        
        # Shades of Purple
        (128, 0, 128): 'Violet',
        (148, 0, 211): 'Dark Violet',
        (218, 112, 214): 'Orchid',
        (138, 43, 226): 'Blue Violet',
        
        # Shades of Brown
        (139, 69, 19): 'Saddle Brown',
        (139, 69, 0): 'Chocolate',
        (205, 133, 63): 'Peru',
        (210, 105, 30): 'Chocolate (Web)',
        
        # Shades of Pink
        (255, 20, 147): 'Deep Pink',
        (255, 105, 180): 'Hot Pink',
        (255, 192, 203): 'Pink (Light)',
        (255, 182, 193): 'Pink (Light Pink)',
    }

    colours = np.array(list(colour_names.keys()))  # Array of BGR colours from the colour_names dictionary
    colour_names_array = np.array(list(colour_names.values()))  # Array of colour names corresponding to the BGR colours

    distances = np.linalg.norm(colours - np.array(bgr_colour), axis=1)  # Calculate the Euclidean distances between the 
                                                                        # input BGR colour and all colours in the dictionary

    nearest_colour_index = np.argmin(distances)  # Index of the nearest colour in the distances array

    # Check if the nearest colour is within a threshold distance
    if distances[nearest_colour_index] < 100:  
        return colour_names_array[nearest_colour_index]  # Return the name of the nearest colour
    else:
        return 'Unknown'  # Return 'Unknown' if no suitable colour is found within the threshold

# Initialize the video capture object for camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the height and width of the frame from the camera properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the coordinates of the center point of the top half of the frame
x_top_center = width // 2
y_top_center = height // 4  # Assuming the top half is the first quarter of the frame

# Define the coordinates of the center point of the bottom half of the frame
x_bottom_center = width // 2
y_bottom_center = height * 3 // 4  # Assuming the bottom half is the last quarter of the frame

while True:
    # Capture frame-by-frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Get the BGR colours at the specified points in the frame
    colour_top_center = frame[y_top_center, x_top_center]
    colour_bottom_center = frame[y_bottom_center, x_bottom_center]
    
    # Print the colour names corresponding to the BGR colours at the specified points
    print("Top colour:", bgr_to_colour_name(colour_top_center), "   Bottom colour:", bgr_to_colour_name(colour_bottom_center))

    # Display circles at the specified points on the frame (top center in blue, bottom center in green)
    cv2.circle(frame, (x_top_center, y_top_center), 5, (255, 0, 0), -1)  # Blue circle at top center
    cv2.circle(frame, (x_bottom_center, y_bottom_center), 5, (0, 255, 0), -1)  # Green circle at bottom center

    # Show the frame with marked points in a window titled 'Camera Feed'
    cv2.imshow('Camera Feed', frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
