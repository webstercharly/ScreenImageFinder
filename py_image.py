import pyautogui
import time

def find_all_images_on_screen(image_path, duration=1200):
    occurrences = {}
    step_size = 300  # Adjust this size based on the expected size of your image

    while True:
        current_time = time.time()
        screen_width, screen_height = pyautogui.size()
        found_positions = []

        for x in range(0, screen_width, step_size):
            for y in range(0, screen_height, step_size):
                try:
                    region = (x, y, step_size, step_size)
                    position = pyautogui.locateOnScreen(image_path, region=region, confidence=0.8)
                    if position:
                        center_position = pyautogui.center(position)
                        if center_position not in found_positions:
                            found_positions.append(center_position)
                            if center_position not in occurrences:
                                occurrences[center_position] = current_time
                except pyautogui.ImageNotFoundException:
                    continue

        if found_positions:
            print(f"Found {len(found_positions)} occurrences of the image.")
            for position, start in list(occurrences.items()):
                if current_time - start >= duration:
                    pyautogui.click(position)
                    print(f"Clicked on an image at {position}.")
                    del occurrences[position]

        time.sleep(10)  # Wait for a short period before checking again

find_all_images_on_screen('./back_button.png')
