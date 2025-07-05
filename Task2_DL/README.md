# 🤖 Task 2 – Deep Learning Project: Image Classification using CNN | CodTech Data Science Internship

This project is part of my internship with **CodTech IT Solutions**, where I implemented a **Convolutional Neural Network (CNN)** using **TensorFlow & Keras** to perform handwritten digit classification on the **MNIST dataset**.

---

## 📌 Objective

To build a deep learning model for image classification that:
- Recognizes handwritten digits (0–9)
- Uses CNN architecture
- Visualizes training and validation metrics

---

## 🖼️ Dataset Overview

**Name:** MNIST Handwritten Digits  
**Source:** TensorFlow Datasets  
**Description:** 70,000 grayscale images (28x28) of digits (0 to 9)  
- Training Set: 60,000 images  
- Test Set: 10,000 images

No manual download required – loaded via `tensorflow.keras.datasets`.

---

## 🧪 Steps Performed

1. **Data Loading and Preprocessing**
   - Loaded MNIST dataset from Keras
   - Normalized pixel values (0–255 → 0–1)
   - Reshaped input for CNN compatibility

2. **CNN Model Architecture**
   - 2 Convolutional Layers + MaxPooling
   - Flatten → Dense → Output (Softmax)

3. **Model Training**
   - Optimizer: `adam`
   - Loss: `sparse_categorical_crossentropy`
   - Epochs: 5

4. **Evaluation and Visualization**
   - Plotted training vs validation accuracy and loss
   - Evaluated on test set for final performance

---

## 🧠 Model Summary

| Layer Type      | Output Shape  | Parameters |
|------------------|----------------|-------------|
| Conv2D (32 filters) | (26, 26, 32) | 320 |
| MaxPooling2D     | (13, 13, 32) | 0 |
| Conv2D (64 filters) | (11, 11, 64) | 18496 |
| MaxPooling2D     | (5, 5, 64)  | 0 |
| Flatten          | (1600)       | 0 |
| Dense (64)       | (64)         | 102464 |
| Dense (Output - 10) | (10)        | 650 |

**Test Accuracy Achieved:** _~98%_

---

## 📊 Visual Output

- Accuracy vs Epochs  
- Loss vs Epochs  
- Both graphs plotted using `matplotlib`

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Libraries:** TensorFlow, Keras, Matplotlib
- **Platform:** Visual Studio Code

---

## 📁 Project Structure

| File                          | Description                            |
|-------------------------------|----------------------------------------|  
| `Deep_Learning_image_classification.py` | Python script version        |
| `README.md`                   | Project documentation                  |

---

## ▶️ How to Run

1. Clone this repository or download the folder `Task2_DL`
2. Open the `.py` file in VS Code
3. Run each cell step by step to reproduce the results.

---

## 🏁 Outcome

Successfully built and trained a deep learning model using CNN to classify handwritten digits. Achieved high accuracy and visualized training performance metrics.

---

## 🏅 Internship

This project was completed as part of the **Data Science Internship** with [CodTech IT Solutions](https://www.codtechit.com/).

---

### Learning never exhausts the mind,it only fuels innovation. Task 2 completed with clarity and confidence!

