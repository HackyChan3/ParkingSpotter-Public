# APL Parking Spot Detector

A machine learning-powered web application that detects cars in overhead parking lot images using computer vision. This project uses a custom-trained YOLOv8 model fine-tuned on satellite imagery of APL (Applied Physics Laboratory) campus parking lots.

## Project Overview

This application allows users to upload overhead images of parking lots and automatically detects the number of cars present. The system uses deep learning to identify vehicles from a bird's-eye view, making it useful for:

- Real-time parking availability monitoring
- Parking lot occupancy analytics
- Smart parking management systems
- Campus resource planning

## Features

- **Custom-trained YOLO model** - Fine-tuned on overhead parking lot imagery
- **High accuracy** - Achieves 98.8% mAP@50, 97.5% precision, 94.4% recall
- **Web-based interface** - Easy-to-use upload and detection system
- **Real-time results** - Instant car detection and counting
- **Annotated outputs** - Visual bounding boxes around detected vehicles

## Tools Used

- **Model**: YOLOv8 (Ultralytics)
- **Training**: Roboflow
- **Backend**: Python, Flask
- **Frontend**: Streamlit
- **Data Collection**: MATLAB (satellite imagery via geoaxes)

## Model Performance

| Metric | Score |
|--------|-------|
| mAP@50 | 98.8% |
| Precision | 97.5% |
| Recall | 94.4% |


## Getting Started

### Requirements

See requirements.txt

Needs: 
```bash
python 3.8+
pip
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/apl-parking-detector.git
cd apl-parking-detector
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up Roboflow API key**
```bash
# Create a .env file
echo "ROBOFLOW_API_KEY=your_api_key_here" > .env
```

4. **Run the application, Open in browser**


## Usage

### Web Application

1. Navigate to the homepage
2. Click "Choose File" and select an overhead parking lot image
3. Click "Detect Cars"
4. View the annotated image with bounding boxes and car count

### Command Line (Batch Processing)

```python
python detect.py
```

This will process all images in the validation folder and save results to the output directory.

### Generating Test Images

If you have MATLAB installed:

```matlab
testimagegen
```

This generates 5 satellite images of APL campus parking lots for testing.

## Configuration

### Adjusting Confidence Threshold

In `app.py` or `detect.py`, modify the confidence parameter:

```python
result = model.predict(input_path, confidence=40)  # 40% confidence
```

Lower values (20-30) detect more objects but may include false positives.
Higher values (50-70) are more conservative but may miss some cars.

### Using Different Model Versions

Change the version number in the code:

```python
model = project.version(3).model  # Change to your version number
```

## Model Training Details

### Dataset Preparation

1. **Base Dataset**: CNRPark (pre-labeled overhead parking images)
2. **Custom Data**: APL campus satellite imagery via MATLAB geoaxes
3. **Annotation**: Roboflow annotation tool
4. **Augmentation**: Applied through Roboflow (rotation, brightness, noise)

### Training Process

- **Platform**: Google Colab (free GPU)
- **Model**: YOLOv8 nano (optimized for CPU inference)
- **Epochs**: 50-100
- **Transfer Learning**: Started from COCO pre-trained weights
- **Training Time**: ~2-3 hours on GPU

### Training Command (Reference)

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(data='data.yaml', epochs=100, imgsz=640)
```

## Considerations

- API keys stored in environment variables (not committed to Git)
- Only image file types accepted
- Works best with overhead/satellite imagery (NOT angled photos)
- CPU inference can be slow (1-3 seconds per image)
- Model trained primarily on APL-style parking lots

## Future Improvements

- [ ] Real-time webcam/drone feed support
- [ ] Distance calculation to find closest available spot
- [ ] Mobile app version (React Native)
- [ ] Support for angled parking lot photos
- [ ] Multi-lot comparison dashboard
- [ ] Occupancy analytics

## License

None

## Contact

**Abhijeet Ghodgaonkar**
- GitHub: [@HackyChan3](https://github.com/HackyChan3)
- Email: alphaspace24@gmail.com

---

**Note**: This project was developed as a proof-of-concept for smart parking management systems. The model is optimized for APL campus parking lots but can be retrained on other parking lot datasets for broader applicability.

