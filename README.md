
# YouTube Comments Spam Detection

## Overview

This project focuses on detecting spam comments on YouTube videos using machine learning techniques. The dataset consists of comments collected from various YouTube videos, with features such as the author, date, content, video name, and a target variable indicating whether the comment is spam.

## Dataset Description

The dataset used in this project contains the following columns:

- **comment_id**: A unique identifier for each comment. This feature is not used in modeling.
- **Author**: The username of the person who posted the comment. This feature may reveal patterns related to spam accounts.
- **Date**: The date on which the comment was posted. Analyzing this can reveal trends in spam activity over time.
- **Content**: The actual text of the comment. This is the primary feature used to train the spam detection model.
- **video_name**: The name of the YouTube video on which the comment was posted. This could provide context or reveal patterns in spam activity across different types of videos.
- **class**: The target variable, where `1` indicates a spam comment and `0` indicates a legitimate comment. This is the feature the model aims to predict.

## Model and Techniques

- **Model**: Support Vector Classifier (SVC)
- **Accuracy**: 96%
- **Preprocessing**: The text content of the comments is processed and transformed into a format suitable for machine learning models. This involves techniques such as tokenization, vectorization (e.g., TF-IDF), and possibly other text preprocessing methods like stemming or lemmatization.
- **Feature Engineering**: Apart from the `Content` feature, other features like `Author`, `Date`, and `video_name` might be used to capture additional patterns that could help improve model performance.

## Deployment

The model has been deployed using FastAPI, a modern web framework for building APIs with Python. This allows for real-time spam detection on new comments via a RESTful API.

### FastAPI Setup

1. **Install FastAPI and Uvicorn**:
    ```bash
    pip install fastapi uvicorn
    ```

2. **Run the API**:
    ```bash
    uvicorn main:app --reload
    ```

3. **Endpoints**:
    - `POST /predict`: Takes a comment's content as input and returns a prediction indicating whether it is spam or not.

## Usage

1. **Dataset**: Ensure the dataset is available in the appropriate format.
2. **Training the Model**: The SVC model is trained using the preprocessed `Content` of the comments.
3. **Prediction**: After training, the model can predict whether a new comment is spam or not.
4. **Evaluation**: The model's performance is evaluated using accuracy, precision, recall, and other relevant metrics.

## Results

The SVC model achieved an accuracy of 96% on the test data, demonstrating its effectiveness in distinguishing between spam and legitimate comments.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request if you have any ideas or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

