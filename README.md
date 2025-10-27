## 🪴 Leaffliction — Leaf Disease Detection using Computer Vision

### 📄 Project Description

**Leaffliction** is a computer vision project focused on **image classification for leaf disease recognition**.
Using deep learning and image processing, it aims to **analyze, augment, transform, and classify** plant leaf images to detect specific diseases with high accuracy (above 90%).
This project involves dataset analysis, data augmentation, image transformation, and model training for disease prediction.

---

## 🌱 Project Overview

Leaffliction uses **image processing and machine learning** techniques to identify plant leaf diseases from images.
The pipeline is divided into 4 main parts:

1. **Dataset Analysis**

   * Extracts and analyzes image datasets from subdirectories.
   * Generates visual reports (pie and bar charts) to represent disease distribution per plant type.

2. **Data Augmentation**

   * Balances the dataset by generating new images through techniques like flip, rotate, crop, skew, shear, and distortion.

3. **Image Transformation**

   * Applies multiple transformations such as Gaussian blur, masking, ROI detection, color histogram, and pseudolandmarks extraction.

4. **Classification**

   * Trains a model to classify leaf diseases with >90% accuracy.
   * Supports prediction from individual images with output showing the disease type.

---

## 🧠 Features

* Automated dataset analysis and visualization.
* Multiple image augmentation and transformation techniques.
* Deep learning–based classification system.
* High validation accuracy (>90%).
* CLI (Command-Line Interface) for all major operations.

---

## 🌿 Dataset

Organized as:

```
./Apple/
   ├── apple_healthy/
   ├── apple_apple_scab/
   ├── apple_black_rot/
   ├── apple_cedar_apple_rust/
```

Each subfolder contains images of specific conditions of plant leaves.

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/leaffliction.git
cd leaffliction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1️⃣ Dataset Analysis

```bash
python Distribution.py ./Apple
```

### 2️⃣ Data Augmentation

```bash
python Augmentation.py ./Apple/apple_healthy/image1.jpg
```

### 3️⃣ Image Transformation

```bash
python Transformation.py -src ./Apple/apple_healthy/ -dst ./dst_directory -mask
```

### 4️⃣ Training and Prediction

```bash
python train.py ./Apple/
python predict.py ./Apple/apple_healthy/image1.jpg
```

---

## 📁 Project Structure

```
Leaffliction/
│
├── data/                        # Dataset directory
├── augmented_data/              # Augmented dataset
├── models/                      # Saved models
├── scripts/                     # Utility scripts
│   ├── Distribution.py
│   ├── Augmentation.py
│   ├── Transformation.py
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
├── signature.txt
└── README.md
```

---

## 🧩 Evaluation & Turn-in

* Only your **programs** and **signature.txt** should be submitted in the GitHub repository.
* The dataset itself **must not be included**.
* Use the SHA1 hash to verify your dataset and model:

  ```bash
  shasum directory.zip
  ```
* The signature in `signature.txt` will be compared during evaluation.

---

## 🧰 Technologies

* **Python 3.x**
* **OpenCV / PlantCV**
* **TensorFlow / PyTorch**
* **Matplotlib / Seaborn** (for visualization)
* **NumPy / Pandas**


