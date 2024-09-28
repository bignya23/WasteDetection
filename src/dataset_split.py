import os
import random
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))

parent_folder = os.path.join(base_dir, "../data/images")
output_train_folder = os.path.join(base_dir,"../data/images/train")
output_val_folder = os.path.join(base_dir,"../data/images/val")
train_ratio = 0.8

os.makedirs(output_val_folder, exist_ok=True)
os.makedirs(output_train_folder,exist_ok=True)

for class_folder in os.listdir(parent_folder):
    class_path = os.path.join(parent_folder, class_folder)

    if os.listdir(class_path):
        os.makedirs(os.path.join(output_train_folder, class_folder), exist_ok=True)
        os.makedirs(os.path.join(output_val_folder, class_folder), exist_ok=True)


        img_list = [f for f in os.listdir(class_path) if f.endswith(('.jpg'))]

        random.shuffle(img_list)
        train_size = (int)(len(img_list) * train_ratio)
        train_files = img_list[:train_size]
        val_files = img_list[train_size:]


        def copy_files(file_list, src_folder, dst_folder):
            for file_name in file_list:
                # Copy image
                src_image_path = os.path.join(src_folder, file_name)
                dst_image_path = os.path.join(dst_folder, file_name)
                shutil.copy(src_image_path, dst_image_path)



        copy_files(train_files, class_path, os.path.join(output_train_folder, class_folder))
        copy_files(val_files, class_path, os.path.join(output_val_folder, class_folder))

print("Dataset split complete!")