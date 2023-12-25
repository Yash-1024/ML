# USE CASE 1: Drowsiness detection using LSTM

Network Architecture reference: 
CNN + LSTM 
https://arxiv.org/pdf/1411.4389.pdf * Data Labelling/annotation files
https://journals.ekb.eg/article_257197_afc57de559f2a5a28ba7c6000e27c0c6.pdf
Output Labels: 
Based on Karolinska Sleepiness Scale (KSS), scale is calculated ranging from 
1(Alert) ,2, 3 and 4(Sleepy)
Other inputs: Students are free to choose transfer learning/fresh training from 
article_257197_afc57de559f2a5a28ba7c6000e27c0c6.pdf (ekb.eg)
Reference: Human Activity Recognition using TensorFlow (CNN + LSTM) | 2 Methods 
 YouTube

Expected Outputs:
* Dataset used for training & testing
* Model training code
* Trained model output
* Model architecture and code
* Evaluation parameters such as: 
Confusion matrix, Accuracy. Precision, 
Recall, Specificity, F1 score etc as 
applicable

## Project Description
This project utilizes Long Short Term Memory(LSTM) techniques and a Convolutional Neural Network (CNN) model to detect drowsiness in a person's eyes through a webcam feed. It aims to enhance safety by alerting individuals who may be feeling drowsy while operating machinery, driving, or performing tasks that demand attention.

The main components of this project include:
- **Lstm:** Used to model temporal dependencies in eye state sequences, improving the prediction of drowsiness patterns
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
  - [Yash Anand]((https://www.linkedin.com/in/yash-anand-349a69227/))
  - [Siddhant Mohanta]
  - [Sidhharth Shivam]
- **Haar Cascades:** [OpenCV Documentation](link-to-opencv)
- **CNN Model:** [Keras Documentation](link-to-keras)

## License
This project is licensed under the [Yash Anand] - see the [LICENSE](link-to-license) file for details.
