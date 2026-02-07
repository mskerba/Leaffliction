from pathlib import Path
import random
import matplotlib.pyplot as plt
import argparse
import sys


def get_image_distribution(directory):
    extentions = [".jpg", ".jpeg", ".png"]
    subdirectories = [x for x in Path(directory).iterdir() if x.is_dir()]
    
    distribution = {}

    for dir in subdirectories:
        files =[]
        for file in dir.iterdir():
            if file.is_file() and file.suffix.lower() in extentions:
                files.append(file)
        distribution[dir.name] = len(files)
    num_subdirs = len(subdirectories)
    total_images = sum(distribution.values())
    print(f"FOLDERS: {num_subdirs}")
    print(f"TOTAL IMAGES: {total_images} \n")
    for key, value in distribution.items():
        print(f"    {key}: {value}")
    return distribution

def pie_chart(distribution):
    plt.title('Image Distribution Across Folders')
    plt.pie(distribution.values(), labels=distribution.keys(), autopct='%1.1f%%')
    plt.show()
    
def random_color(n):
    colors = []
    for _ in range(n):
        colors.append("#" + ("%06x" % random.randint(0, 0xFFFFFF)))
    return colors

def bar_chart(distribution):
    colors = random_color(len(distribution))
    plt.grid(True)
    plt.bar(distribution.keys(), distribution.values(), color=colors)
    plt.xlabel('Folders')
    plt.ylabel('Number of Images')
    plt.title('Image Distribution Across Folders')
    plt.xticks(rotation=45)
    plt.show()
    
def plot_distribution(distribution):
    pie_chart(distribution)
    bar_chart(distribution)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str, help="Path to the source dir.")
    args = parser.parse_args()

    directory = args.src
    if not Path(directory).is_dir():
        sys.exit("Invalid directory path")
    image_distribution = get_image_distribution(directory)
    plot_distribution(image_distribution)
