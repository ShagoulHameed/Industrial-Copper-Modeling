# Industrial Copper Modeling  

Streamlit Cloud Demo link ::   https://industrial-copper-modeling-juezw8nudqcttw6vgvlqxv.streamlit.app/

![image](https://github.com/user-attachments/assets/e1ca563e-0031-4901-884e-4537107bf6ab)
## Overview
The Industrial Copper Modeling project addresses the challenges in the copper industry's sales and pricing data. This data often suffers from skewness and noise, affecting the accuracy of manual predictions. This project leverages machine learning techniques to enhance the accuracy and efficiency of predictions.

## Problem Statement
The copper industry deals with less complex data related to sales and pricing. However, this data may suffer from issues such as skewness and noisy data, which can affect the accuracy of manual predictions. Dealing with these challenges manually can be time-consuming and may not result in optimal pricing decisions. A machine learning regression model can address these issues by utilizing advanced techniques such as data normalization, feature scaling, and outlier detection, and leveraging algorithms that are robust to skewed and noisy data.

Another area where the copper industry faces challenges is in capturing the leads. A lead classification model is a system for evaluating and classifying leads based on how likely they are to become a customer. You can use the STATUS variable with WON being considered as Success and LOST being considered as Failure and remove data points other than WON, LOST STATUS values.

## Solution
The solution involves the following steps:
1. **Data Exploration**: Exploring skewness and outliers in the dataset.
2. **Data Transformation**: Transforming the data into a suitable format and performing necessary cleaning and pre-processing steps.
3. **Regression Model**: Building a machine learning regression model to predict the continuous variable `Selling_Price`.
4. **Classification Model**: Building a machine learning classification model to predict `Status` (WON or LOST).
5. **Streamlit Application**: Creating a Streamlit app for users to input column values and receive predictions for `Selling_Price` or `Status`.

## Data Preprocessing
### Data Loading
- The dataset is loaded into a Pandas DataFrame for initial exploration.

### Handling Missing Values
- Identified and handled missing values appropriately. Missing values were filled using suitable strategies such as mean, median, or mode imputation.

### Log Transformation
- Applied log transformation to reduce skewness and stabilize variance for the following features:
  - `quantity_tons`
  - `customer`
  - `thickness`
  - `selling_price`

### Feature Engineering
- Created new features to enhance the dataset:
  - Extracted day, month, and year from `item_date` and `delivery_date`.
  - Created interaction terms and polynomial features to capture non-linear relationships.

### Data Normalization
- Normalized features to ensure they are on a similar scale, which is crucial for the performance of many machine learning algorithms.

### Outlier Detection and Removal
- Detected and removed outliers using statistical techniques to prevent them from adversely affecting the model's performance.

### Encoding Categorical Variables
- Encoded categorical features using techniques such as one-hot encoding to convert them into a format suitable for machine learning models.

### Splitting Data
- Split the dataset into training and testing sets to evaluate the model's performance on unseen data.

## Model Building
### Regression Model
- Built a regression model to predict the selling price of copper. The model uses features such as country, item type, application, width, product reference, quantity (log-transformed), customer (log-transformed), thickness (log-transformed), and date features.
- Utilized algorithms like Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
- Tuned hyperparameters using GridSearchCV for optimal model performance.

### Classification Model
- Built a classification model to predict the status (WON or LOST) of leads. The model uses similar features as the regression model.
- Utilized algorithms like Logistic Regression, Decision Tree Classifier, and Random Forest Classifier.
- Applied techniques like SMOTE to handle class imbalance.
- Tuned hyperparameters using GridSearchCV for optimal model performance.

## Model Evaluation
- Evaluated the performance of the models using metrics such as RMSE for regression and accuracy, precision, recall, and F1-score for classification.
- Visualized the results using plots like scatter plots, ROC curves, and confusion matrices.

## Streamlit Application
- Developed a Streamlit app to provide an interactive interface for users to input feature values and obtain predictions for `Selling_Price` and `Status`.


## Results
- The regression model predicts the selling price of copper with improved accuracy.
- The classification model predicts the status of leads as WON or LOST, aiding in better decision-making.

## Contact
For any queries, please reach out to Shagoul Hameed at Shagoul04@gmail.com. 
https://www.linkedin.com/in/shagoul-hameed/

## Project Demo Video
https://www.linkedin.com/posts/shagoul-hameed_machinelearning-datascience-python-activity-7219675014315352065-eUk9?utm_source=share&utm_medium=member_desktop 
![image](https://github.com/user-attachments/assets/62dee14e-23be-4a00-b28c-92261afe176d)
