import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the image
print("AAchal Patidar")
image_path = "matarani.jpg"
img = Image.open(image_path)

# Convert the image to grayscale and apply threshold for silhouette effect
img = img.convert("L")  # Convert to grayscale
threshold = 100  # Adjust this value as needed
img = img.point(lambda p: 0 if p < threshold else 255)

# Convert to numpy array
img_array = np.array(img)

# Create a figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img_array, cmap="gray", interpolation="nearest")

# Hide axes
ax.axis("off")

# Save the generated silhouette image
plt.savefig("durga_silhouette.png", bbox_inches="tight", dpi=300)
plt.show()
