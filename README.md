# FogVision AI - Foggy Object Detection

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)](https://flask.palletsprojects.com/)
[![YOLOv10](https://img.shields.io/badge/YOLOv10-Ultralytics-blueviolet.svg)](https://ultralytics.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

See Through the Fog. FogVision AI is an end-to-end web application that uses a state-of-the-art deep learning model to detect vehicles and people in challenging, low-visibility conditions.

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Key Features](#-key-features)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [User Guide](#-user-guide)

## Introduction

Foggy weather presents a significant challenge for autonomous driving and surveillance systems, as it severely degrades the performance of standard object detection algorithms. FogVision AI was developed to address this critical safety issue.

This project is a fully functional, end-to-end application demonstrating a comprehensive skill set in frontend development, backend architecture, and the implementation of advanced deep learning models. The core of the application is a **custom-trained, lightweight YOLOv10 model** specifically optimized for robust performance in foggy environments. It leverages advanced preprocessing techniques to cut through the haze and identify objects that would otherwise be obscured.

## Key Features

- **🔐 Secure User Authentication**: Features a complete user registration and login system to manage access.
- **🌫️ AI-Powered Fog Detection**: Upload an image of a foggy scene, and the custom-trained YOLOv10 model accurately identifies objects like cars, buses, motorbikes, bicycles, and people.
- **🖼️ Advanced Image Preprocessing**: Utilizes novel techniques including **Dehaze Formers** and **dark channel methods** to computationally remove haze and improve image quality before detection.
- **🚀 Optimized Lightweight Architecture**: The YOLOv10 model is enhanced with a lightweight module, ensuring a balance between high detection performance and computational efficiency.
- **✨ Enhanced Attention Module**: Incorporates an advanced attention mechanism to help the model focus on relevant object features, even when they are small or partially obscured by fog.
- **🖥️ Interactive Web Interface**: A clean and responsive user interface for easy image uploads and clear visualization of detection results.

## Tech Stack

This project integrates a variety of modern technologies to deliver a robust and effective solution.

| Category         | Technology / Library                             |
| ---------------- | ------------------------------------------------ |
| **Backend** | `Python`, `Flask`                                |
| **AI / ML** | `YOLOv10 (Ultralytics)`, `PyTorch`, `OpenCV`      |
| **Frontend** | `HTML5`, `CSS3`                                  |
| **Data/Session** | `Flask Session` (for user management)            |

## Getting Started

### Prerequisites

-   Python 3.10 or higher
-   `pip` 
-   Git version control

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/FogVisionAI-Foggy-Object-Detection.git](https://github.com/your-username/FogVisionAI-Foggy-Object-Detection.git)
    cd FogVisionAI-Foggy-Object-Detection
    ```

2.  **Create a Virtual Environment**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Flask Secret Key**
    The application uses a secret key for session management. You can change the default key in `app.py`:
    ```python
    app.secret_key = 'your_super_secret_key'  # Change this line
    ```

5.  **Run the Flask Application**
    Once the dependencies are installed, you can start the Flask server.
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`. Open this URL in your web browser.

## User Guide

1.  **Homepage**: The homepage provides links to Register or Login.
2.  **Register**: Create a new account with a unique username and password.
3.  **Login**: Sign in with your registered credentials.
4.  **Upload**: After logging in, you'll be directed to the upload page.
    -   Click "Choose File" and select an image containing a foggy scene.
    -   Click "Upload and Detect".
5.  **Results**: The application will process the image and display the result with bounding boxes drawn around detected objects.
6.  **Upload Another**: Click the "Upload Another Image" button to return to the upload page.
