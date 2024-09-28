import os

base_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_dir, '../data/images/val')
save_path = os.path.join(base_dir, '../data/labels/val')
i = 0

for sub_folder in os.listdir(folder_path):
    label = i
    sub_folder_path = os.path.join(folder_path,sub_folder)
    for filename in os.listdir(sub_folder_path):
        if filename.endswith('.jpg'):
            x_center = 0.5
            y_center = 0.5
            box_width = 1.0
            box_height = 1.0

            os.makedirs(os.path.join(save_path, sub_folder),exist_ok=True)

            # Create label file
            label_file_path = os.path.join(save_path, sub_folder, f"{os.path.splitext(filename)[0]}.txt")
            with open(label_file_path, 'w') as f:
                f.write(f"{label} {x_center} {y_center} {box_width} {box_height}\n")

    print(f"Class {i} labeling complete!")

    i = i + 1




