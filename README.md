# smart sorting transfer learning for identifying rotten fruits and vegetables

## Team Details

- **Team ID**: LTVIP2026TMIDS83701  
- **Team Size**: 4  
- **Team Leader**: Gajjala Kalpana 
- **Team Members**:  
  - B Somesh
  - K Lohitha
  - Vanarasi Sandhyasree

---
> Dataset Link:  https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification

## Project Overview

Smart Sorting is an innovative project aimed at developing an accurate and efficient model for identifying fresh and rotten fruits. It leverages **Deep Learning** techniques with Convolutional Neural Networks (CNNs) to automate the sorting process and significantly enhance classification accuracy. The project provides a reliable and scalable tool for farmers and the agricultural industry, improving the precision and efficiency of fruit quality analysis.

## Features

- **Accurate Fruit Classification**: Classifies six distinct types of fruits: Fresh Apple, Rotten Apple, Fresh Banana, Rotten Banana, Fresh Orange, and Rotten Orange.
- **Deep Learning Model**: Utilizes a custom CNN architecture to achieve high accuracy in distinguishing between fresh and rotten produce.
- **Web Application Interface**: A user-friendly Flask-based web application for easy image upload and real-time prediction display.
- **Production-Ready**: Designed for deployment, with a clear project structure.

## Project Structure

```
SimpleFruitClassifier-main/
├── static/
│   ├── assets/
│   ├── forms/
│   └── uploads/
├── templates/
│   ├── blog-single.html
│   ├── blog.html
│   ├── index.html
│   └── portfolio-details.html
├── app.py
├── healthy_vs_rotten.h5
├── ipython.html
└── Readme.txt
```

## Installation and Setup (Local)

### Prerequisites

- Python 3.8+
- pip
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lohithak096-dot/smart-sorting-transfer-learning-for-identifying-rotten-fruits-and-vegetables.git
   ```

2. **Create and activate a virtual environment** (Optional but recommended):
   ```bash
   python -m venv venv
   ```

   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install tensorflow flask keras numpy
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open in browser**: Visit `http://127.0.0.1:5000/`

## Usage

- **Step 1**: Upload a fruit image (valid formats: PNG, JPG, JPEG).
- **Step 2**: Click the "Submit" button to classify the fruit.
- **Step 3**: View the classification result (e.g., "Fresh Apple" or "Rotten Banana") on the result page.

## Model Details

- **Architecture**: Custom Convolutional Neural Network (CNN)
- **Dataset**: Fruits Fresh and Rotten for Classification (Kaggle)
- **Classes**: 6 (Fresh Apple, Fresh Banana, Fresh Orange, Rotten Apple, Rotten Banana, Rotten Orange)
- **Training**: Adam optimizer, categorical cross-entropy loss
- **Model File**: `healthy_vs_rotten.h5`

## Contributing

Fork the repository, create pull requests, or submit issues to contribute.



