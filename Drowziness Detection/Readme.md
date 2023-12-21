# Drowsiness Detection using Computer Vision and CNN

## Project Description
This project utilizes Long Short Term Memory(LSTM) techniques and a Convolutional Neural Network (CNN) model to detect drowsiness in a person's eyes through a webcam feed. It aims to enhance safety by alerting individuals who may be feeling drowsy while operating machinery, driving, or performing tasks that demand attention.

The main components of this project include:
- **lstm** Used to model temporal dependencies in eye state sequences, improving the prediction of drowsiness patterns
- **OpenCV:** Used for capturing and processing video frames from the webcam.
- **Haar Cascades:** Employed for detecting faces and eyes within the video frames.
- **Keras with CNN:** Utilized for eye state prediction, determining whether eyes are open, closed, or slightly drowsy.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Scoring System](#scoring-system)
- [Alert Mechanism](#alert-mechanism)
- [Credits](#credits)
- [License](#license)

## Installation
To run this project locally:
1. **Clone the Repository:** `git clone https://github.com/Yash-1024/ML/main/Drowziness%20Detection/drowsiness-detection.git`
2. **Install Dependencies:** Navigate to the project directory and run `pip install -r requirements.txt`.
3. **Run the Script:** Execute the script using `python drowsiness_detection.py`.

## Usage
Once the script is running:
- The webcam feed captures video frames.
- Face and eye detection are performed using Haar Cascades.
- The CNN model predicts eye states (open, closed, slightly drowsy) for each eye independently.
- A scoring system tracks the individual's alertness level based on eye predictions.
- If the cumulative score exceeds 15, an alarm sounds to alert potential drowsiness.

Press 'q' to exit the program.

### Scoring System
- Closed Eyes (Both): +1 point
- One Eye Slightly Drowsy: -1 point
- One Eye Closed, One Awake: -2 points
- Both Eyes Awake: -3 points

### Alert Mechanism
- When the cumulative score surpasses 15, an alarm is triggered.
- A red bounding box is drawn around the frame to visually alert the user.

## Credits
- **Team Members:** 
  - [Yash Anand]([link-to-profile](https://www.linkedin.com/in/yash-anand-349a69227/))
  - [Siddhant Mohanta]
  - [Sidhharth Shivam]
- **Haar Cascades:** [OpenCV Documentation](link-to-opencv)
- **CNN Model:** [Keras Documentation](link-to-keras)

## License
This project is licensed under the [Yash Anand] - see the [LICENSE](link-to-license) file for details.
