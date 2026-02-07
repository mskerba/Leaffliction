import cv2 as cv
from pathlib import Path
import argparse
import sys
import shutil
import numpy as np
import matplotlib.pyplot as plt

LABELS = ["Original", "Rotated", "Flipped", "Sheared", "Skewed", "Cropped", "Distorted"]


def split_images(split_ratio):
    augmented_dir = Path("augmented_directory")
    val_dir = Path("augmented_directory_test")
    for subdir in augmented_dir.iterdir():
        if subdir.is_dir():
            val_subdir = val_dir / subdir.name
            val_subdir.mkdir(parents=True, exist_ok=True)
            images = list(subdir.glob("*.*"))
            num_val_images = int(len(images) * split_ratio)
            val_images = np.random.choice(images, num_val_images, replace=False)
            for img in val_images:
                shutil.move(str(img), str(val_subdir / img.name))

def rotate_image(image):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv.getRotationMatrix2D(center, 15, 1.0)
    rotated = cv.warpAffine(image, M, (w, h), borderMode=cv.BORDER_REFLECT_101)
    return rotated

def flip_image(image):
    flip_img = cv.flip(image, 1)
    return flip_img

def shear_image(image):
    (h, w) = image.shape[:2]
    shear_factor = 0.2
    M = np.array([
        [1, shear_factor, 0],
        [0, 1, 0]
    ], dtype=np.float32)

    sheared = cv.warpAffine(image, M, (w, h), borderMode=cv.BORDER_REFLECT_101)
    return sheared

def skew_image(image):
    (h, w) = image.shape[:2]
    pts1 = np.float32([[0,0], [w,0], [0,h], [w,h]])
    pts2 = np.float32([[20,0], [w-20,10], [0,h-20], [w,h]])

    M = cv.getPerspectiveTransform(pts1, pts2)
    skewed = cv.warpPerspective(image, M, (w, h), borderMode=cv.BORDER_REFLECT_101)
    return skewed

def crop_image(image):
    (h, w) = image.shape[:2]
    crop = image[int(0.1*h):int(0.9*h), int(0.1*w):int(0.9*w)]
    crop = cv.resize(crop, (w, h))
    return crop

def distort_image(image):
    distorted = cv.GaussianBlur(image, (5, 5), 0)
    return distorted

def augment_image_save(image_path, images):
    base_path = Path(image_path).parts[1:]
    new_path = Path("augmented_directory").joinpath(*base_path[:-1])
    print(f"Saving augmented images to: {new_path}")
    new_path.mkdir(parents=True, exist_ok=True)
    for idx, (img, label) in enumerate(zip(images, LABELS)):
        if label == "Original":
            new_name = f"{Path(image_path).stem}{Path(image_path).suffix}"
        else:
            new_name = f"{Path(image_path).stem}_{label}{Path(image_path).suffix}"
        new_full_path = new_path / new_name
        cv.imwrite(str(new_full_path), img)

def image_augmentation(image_path, mode):
    img = cv.imread(image_path)
    if img is None:
        sys.exit("Failed to read the image. Please check the file path and ensure it's a valid image.")
    rotated = rotate_image(img)
    flipped = flip_image(img)
    sheared = shear_image(img)
    skewed = skew_image(img)
    cropped = crop_image(img)
    distorted = distort_image(img)
    images = [img, rotated, flipped, sheared, skewed, cropped, distorted]
    augment_image_save(image_path, images)

    if mode == "single":
        fig, axes = plt.subplots(1, 7, figsize=(20, 4))
        for ax, image, label in zip(axes, images, LABELS):
            ax.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
            ax.set_title(label)
            ax.axis("off")
        plt.tight_layout()
        plt.show()


def forlder_augmentation(folder_path):
    for file in Path(folder_path).iterdir():
        if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            image_augmentation(str(file), "folder")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str, help="Path to the folder or image to augment.")
    parser.add_argument("-s", "--split", type=float, default=0, help="Ratio of augmented images reserved for validation (0.0 to 1.0). E.g., 0.2 = 20%% validation / 80%% training. Default: 0 (no split).")
    args = parser.parse_args()
    
    src = args.src
    if not Path(src).exists():
        sys.exit("Invalid path")
    if not Path(src).is_dir() and not Path(src).is_file():
        sys.exit("Path must be a folder or an image")
    if args.split < 0 or args.split > 1:
        sys.exit("Split ratio must be between 0.0 and 1.0")

    if Path(src).is_dir():
        if Path("augmented_directory").exists():
            shutil.rmtree("augmented_directory")
        forlder_augmentation(src)
        
        if args.split > 0:
            if Path("augmented_directory_test").exists():
                shutil.rmtree("augmented_directory_test")
            split_images(args.split)
    elif Path(src).is_file():
        if Path(src).suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid image file type. Supported types: .jpg, .jpeg, .png")
        image_augmentation(src, "single")
        