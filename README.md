# Book Recommendation System

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Project File Structure](#project-file-structure)

## Overview

The Book Recommendation System is a collaborative filter-based recommendation engine that suggests similar books to users based on their search history and preferences. By leveraging a comprehensive books dataset, this system provides personalized book recommendations to enhance user experience and discovery.

## Technologies Used

- **Python:** For implementing recommendation algorithms and data processing.
- **Pickle:** For serialization and deserialization of the recommendation model.
- **Flask:** For developing the web application interface.

## Features

- **Collaborative Filtering:** Utilizes collaborative filtering techniques to recommend books similar to those the user has shown interest in.
- **Book Dataset:** Uses a dataset that includes book titles, authors, genres, and user ratings to generate recommendations.
- **Web Application Interface:** Built with Flask, providing an interactive user interface for searching and receiving book recommendations.
- **Model Serialization:** Implements Pickle to save and load the recommendation model efficiently.

## Installation

To set up the project locally, follow these steps:

1. **Create and Activate a Virtual Environment:**
    
    - **On Linux/macOS:**

    ```bash
    python3 -m venv virtual_env
    source virtual_env/bin/activate
    ```
    
    - **On Windows:**
    
    ```bash
    python -m venv virtual_env
    virtual_env\Scripts\activate

    ```
    
3. **Create and Navigate to the Project Directory:**

    ```bash
    mkdir book-recommendation-system
    cd book-recommendation-system
    ```
    
2. **Clone the Repository:**

   ```bash
   git clone https://github.com/Raj-Dusane/Book-Recommendation-System.git
   ```

4. **Install Required Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
5. **Run the Flask Application:**

    ```bash
    python app.py
    ```
    The application will be accessible at `'http://127.0.0.1:5000'`.
    

### Project File Structure

- **`dataset/`:** Directory contaning raw dataset.

- **`webapp/`:** Directory structure for web app.

    - **`models/`:**  Directory for serialized recommendation model.
    
        **Serialized models:**
        1) **`books.pkl`**: Contains a DataFrame with book details.
        2) **`popular.pkl`**: Provides recommendations for the top 50 books based on user ratings. 
        3) **`pt.pkl`**: Holds the pivot table mapping books to user ratings.
        4) **`similarity_score.pkl`**: Stores the similarity scores between books.

    - **`templates/`:** Standard directory for HTML templates used by Flask.

      - **`index.html`:** Main page.
      - **`recommend.html`:** Renders the recommendations based on user search input.

- **`app.py`:** The main Flask application file.

- **`requirements.txt`:** List of required Python packages.

- **`Based_Book_Recommendation_System.ipynb`:** Illustrates the data flow and the operation of the recommendation model.