import os
from PIL import Image


def create_tiff(folder_list: list[str], output_file: str) -> None:
    padding = 100
    spacing = 50

    width = 200
    height = 200

    images = []
    for folder in folder_list:
        folder_path = os.path.join(os.getcwd(), folder)
        for filename in os.listdir(folder_path):
            images.append(Image.open(os.path.join(folder_path, filename)))

    total_images = len(images)

    # Количество строк и столбцов для размещения изображений
    num_rows = int(total_images ** 0.4)
    num_columns = (total_images // num_rows) + 1

    # Определение размера фона
    total_width = num_columns * width + (num_columns - 1) * spacing + 2 * padding
    total_height = num_rows * height + (num_rows - 1) * spacing + 2 * padding

    background_color = (255, 255, 255)
    background = Image.new('RGB', (total_width, total_height), background_color)

    # Расположение изображений на фоне
    current_x = padding
    current_y = padding
    images_counter = 0

    for image in images:
        image.thumbnail((width, height))
        background.paste(image, (current_x, current_y))
        current_x += image.width + spacing
        images_counter += 1
        if images_counter % num_columns == 0:
            current_x = padding
            current_y += image.height + spacing

    background.save(output_file, 'TIFF')


folder_list = ['1388_12_Наклейки 3-D_3', '1388_6_Наклейки 3-D_2', '1388_2_Наклейки 3-D_1', '1369_12_Наклейки 3-D_3']
output_file = 'Result.tiff'
create_tiff(folder_list, output_file)
