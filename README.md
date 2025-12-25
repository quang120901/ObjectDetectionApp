# Object Detection App
A full-featured object detection application built with Python, OpenCV, and CustomTkinter for real-time object detection in images and videos.

## 🚀 Features

### Object Detection
- Real-time object detection using SSD MobileNet V3
- Detection in both images and videos
- 80+ object classes from COCO dataset
- Adjustable confidence threshold and NMS (Non-Maximum Suppression)
- Visual bounding boxes with object labels

### Image Processing
- Image rotation with custom angles
- Image resizing with custom dimensions
- Display original and processed images
- Save processed results

### Video Processing
- Video frame extraction
- Object detection on video frames
- Save detected objects as separate images
- Frame-by-frame analysis

### Audio Features
- Text-to-Speech (TTS) for detected objects
- Multi-language support (Vietnamese and English)
- Audio playback with pygame

### User Interface
- Modern dark-themed GUI using CustomTkinter
- File browser for easy file selection
- Interactive controls for rotation and resizing
- Real-time processing feedback

## 🛠️ Technology Stack

**Core Technologies:**
- Python 3.x
- OpenCV (cv2) 4.11.0.86
- Deep Learning (DNN module)

**GUI Framework:**
- CustomTkinter 5.2.2
- Tkinter (built-in)

**Machine Learning Model:**
- SSD MobileNet V3 Large COCO
- Pre-trained on COCO dataset
- 80 object classes

**Additional Libraries:**
- NumPy 2.2.3 - Numerical operations
- gTTS 2.5.4 - Google Text-to-Speech
- deep-translator 1.11.4 - Translation services
- pygame 2.6.1 - Audio playback
- requests 2.32.3 - HTTP requests
- beautifulsoup4 4.13.3 - Web scraping

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- pip (Python package installer)
- Webcam (optional, for live detection)

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/quang120901/ObjectDetectionApp.git
cd ObjectDetectionApp
```

### 2. Install Required Dependencies
```bash
cd Source
pip install -r requirements.txt
```

### 3. Verify Model Files
Ensure the following model files exist in `Source/Models/`:
- `coco.names` - Object class names
- `frozen_inference_graph.pb` - Pre-trained model weights
- `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` - Model configuration

### 4. Run the Application
```bash
python GUI.py
```

## 📁 Project Structure

```
ObjectDetectionApp/
├── Source/
│   ├── GUI.py                  # Main application GUI
│   ├── ObjectDetection.py      # Object detection logic
│   ├── Function.py             # Image/Video processing functions
│   ├── requirements.txt        # Python dependencies
│   ├── Models/
│   │   ├── coco.names          # 80 COCO object classes
│   │   ├── frozen_inference_graph.pb       # Model weights
│   │   └── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config
│   ├── Demo/                   # Demo images/videos
│   ├── VideoFrame/             # Extracted video frames
│   └── __pycache__/            # Python cache files
└── README.md
```

## 🎯 Usage

### For Image Detection:
1. Launch the application by running `GUI.py`
2. Click **"Browse File"** to select an image
3. Click **"Show Image"** to view the original image
4. Click **"Detect Image"** to perform object detection
5. Detected objects will be displayed with bounding boxes and labels

### Image Processing:
1. **Rotate Image**: Enter rotation angle (e.g., 45) and click "Rotate"
2. **Resize Image**: Enter width and height, then click "Resize"
3. Processed images will be displayed automatically

### For Video Detection:
1. Click **"Browse File"** to select a video file
2. Click **"Detect Video"** to process the video
3. Frames will be extracted to `VideoFrame/` directory
4. Detected objects will be saved as separate images

### Audio Features:
- The application can announce detected objects using Text-to-Speech
- Supports Vietnamese and English languages
- Audio files are temporarily created and played automatically

## 🌐 Supported Object Classes

The application can detect 80 object classes from the COCO dataset, including:
- **People**: person
- **Vehicles**: car, motorcycle, airplane, bus, train, truck, boat
- **Animals**: bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe
- **Furniture**: chair, couch, bed, dining table, toilet
- **Electronics**: tv, laptop, mouse, remote, keyboard, cell phone
- **Kitchen**: bottle, wine glass, cup, fork, knife, spoon, bowl
- **Food**: banana, apple, sandwich, orange, broccoli, carrot, pizza, donut, cake
- And many more...

## 🔒 Model Information

**Model**: SSD MobileNet V3 Large COCO 2020
- **Architecture**: Single Shot MultiBox Detector (SSD)
- **Backbone**: MobileNet V3 Large
- **Training Dataset**: COCO (Common Objects in Context)
- **Input Size**: 320x320 pixels
- **Detection Threshold**: Configurable (default: 0.45)
- **NMS Threshold**: Configurable (default: 0.2)

## 🎨 GUI Features

- **Modern Dark Theme**: Easy on the eyes
- **File Selection Labels**: Shows selected file paths
- **Interactive Buttons**: Clear action buttons for all functions
- **Input Fields**: Custom rotation angles and resize dimensions
- **Error Handling**: User-friendly error messages
- **Confirmation Dialogs**: Safe exit confirmation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes. Please check local laws regarding software licensing.