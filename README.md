## Agri-Yield Predictor: Multivariate Crop Analysis

# CSA2001 - Fundamentals in AI and ML (BYOP Capstone)

- NAME: KUNWAR SINGH
- REG NO.: 25BCE11021
- CSE[CORE]: 1st Year

# 📌 Project Overview

The Agri-Yield Predictor is a machine learning solution designed to address the unpredictability of agricultural productivity in the Indian context. By analyzing environmental and physical factors, this "Problem Solving Agent" provides farmers with data-driven yield estimates to assist in financial planning and risk management.

This project serves as a capstone activity for the CSA2001 course.


# 📊 Performance Summary
Based on the current model implementation:

- Model Accuracy (R2): 87.02%

- Prediction Margin of Error: ±4.50 Tons

- Visualization: Includes an "Actual vs. Predicted" scatter plot to verify low variance and model reliability.

# 📈 What the Results Mean
- 87.02% Accuracy: My model is highly reliable at finding the "sweet spot" for crop growth.

- ±4.50 Ton Error Margin: This is the "Risk" factor. It tells us exactly how much room for error to expect in the real world.

- The Visualization: If you look at the Actual vs. Predicted graph in this repo, you'll see the green dots hugging the red line—that's                        the sign of a model that truly "learned" the pattern.

# 🧠 How it Works (The "Student" Explanation)

Here is the logic I followed:

- Teaching the Computer to "See" Patterns: I used Multivariate Regression so the model could look at four different factors at once.

- Leveling the Playing Field: Since Rainfall is measured in thousands and Soil pH is a small number (like 6.5), I used Feature Scaling                                 to make sure the computer didn't ignore the soil just because its numbers were smaller.

- Preventing "Memorization": I used Ridge Regression. This acts like a filter that stops the model from overfitting (memorizing the                                   training data) so that it stays accurate when predicting for a brand-new farm.

# 🚀 Getting Started

## Prerequisites

- Python 3.8+

- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

## 🛠️ Set-Up 
- Get the Tools: Make sure you have Python installed.

- Install Requirements: Run `pip install pandas scikit-learn matplotlib`.

- Run the Predictor: Open your terminal and run `agri-yield_predictor.py`.

- See the Magic: The script will train itself on historical data and then output a prediction for a sample farm scenario.
