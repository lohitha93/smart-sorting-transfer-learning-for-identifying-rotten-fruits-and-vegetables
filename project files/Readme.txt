Smart Sorting - Transfer Learning for Identifying Rotten Fruits and Vegetables
================================================================================

Team ID: LTVIP2026TMIDS83701
Team Leader: Gajjala Kalpana
Team Members: B Somesh, K Lohitha, Vanarasi Sandhyasree

Project Description:
--------------------
This project uses a Convolutional Neural Network (CNN) to classify fruits into
six categories: Fresh Apple, Fresh Banana, Fresh Orange, Rotten Apple,
Rotten Banana, and Rotten Orange.

The model is trained on 1,212 images with data augmentation and achieves
high classification accuracy. A Flask web application provides a simple
interface for uploading fruit images and viewing predictions.

How to Run:
-----------
1. Install dependencies: pip install tensorflow flask keras numpy
2. Run the app: python app.py
3. Open browser: http://127.0.0.1:5000/
4. Upload a fruit image and click "Classify Fruit"

Files:
------
- app.py                   : Main Flask application
- healthy_vs_rotten.h5     : Trained CNN model
- templates/index.html     : Upload page
- templates/blog.html      : Blog page
- templates/portfolio-details.html : Project details
- ipython.html             : Exported training notebook
- static/uploads/          : Uploaded images directory

Dataset:
--------
Fruits Fresh and Rotten for Classification (Kaggle)
https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification
