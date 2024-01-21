# ScreenImageFinder

ScreenImageFinder is a Python utility designed to assist in finding all occurrences of a specific image on the screen. Utilizing the `pyautogui` library, this tool automates the process of dividing the screen into regions and methodically searches each to locate instances of the desired image. Ideal for GUI automation testing, screen monitoring, and any scenario where visual verification is required.

## Features

- **Efficient Image Search:** Quickly finds all occurrences of a specified image on the screen.
- **Customizable Search Duration:** Allows setting a maximum duration for the search to prevent endless scanning.
- **Flexible:** Easy to integrate with other Python scripts or projects requiring screen monitoring.

## Installation

Ensure you have Python installed on your system (Python 3.6 or later is recommended). You can then install the required dependencies with pip:

```bash
pip install pyautogui
```

Clone the repository to your local machine:

```bash
git clone https://github.com/webstercharly/ScreenImageFinder.git
cd ScreenImageFinder
```

## Usage

To use ScreenImageFinder, you need to specify the path to the image you're searching for and the duration for the search. Here's a simple example:

```python
from py_image import find_all_images_on_screen

# Replace 'path/to/your/image.png' with the actual image path
image_path = 'path/to/your/image.png'
duration = 120  # Duration in seconds

# Perform the search
find_all_images_on_screen(image_path, duration)
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
