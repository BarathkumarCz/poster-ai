import numpy as np
from PIL import Image

def load_image(uploaded_file, max_size=2048):
    """
    Loads image at high resolution for analysis.
    Resizes only if image is extremely large.
    Returns NumPy array (H x W x C)
    """

    image = Image.open(uploaded_file).convert("RGB")

    # Prevent memory explosion (very large posters)
    w, h = image.size
    if max(w, h) > max_size:
        scale = max_size / max(w, h)
        new_size = (int(w * scale), int(h * scale))
        image = image.resize(new_size, Image.LANCZOS)

    return np.array(image)
