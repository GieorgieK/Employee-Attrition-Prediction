# Employee Attrition Prediction

## Background Project

In an era of increasing business competition, companies need to optimize their human resource management to retain talented employees. High employee turnover can negatively impact productivity, operational costs, and team morale. Analyzing employee data through a machine learning approach can provide deep insights into the factors influencing employees' decisions to leave the company. Thus, companies can take proactive measures to reduce attrition rates and create a more stable and motivating work environment.

## Problem

Companies often face challenges in predicting which employees are at risk of leaving. The available employee data includes various attributes such as job satisfaction, performance ratings, and demographic information. Identifying patterns and key factors causing employee turnover can be very complex without the right analytical tools. The main challenge is how to effectively utilize this data to predict employee turnover and enable companies to take appropriate preventive actions.

## Objective

The goal of this project is to develop a machine learning model that can predict whether an employee will leave the company based on employee survey data and other related data. The specific objectives of this project are:

1. To use machine learning techniques to develop a classification model that can predict the attrition status of an employee.
2. To identify the most influential employee attributes affecting the decision to leave, so the company can understand the key risk factors.
3. To focus on improving the recall metric in the model evaluation, as recall is important for the company to identify as many at-risk employees as possible to reduce turnover.
4. To provide data-driven recommendations to company management to reduce attrition rates and improve employee retention.

By achieving these objectives, the company can reduce costs associated with employee turnover, retain valuable employees, and improve overall performance and job satisfaction within the organization.

## Tools
[<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Seaborn-388E3C?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" />](https://seaborn.pydata.org/)
[<img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />](https://numpy.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Scikit%20learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />](https://scikit-learn.org/)

## Data

The dataset includes the following columns:

| Column                    | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| EmployeeID                | Unique ID for each employee                                   |
| Age                       | Age of the employee                                           |
| Attrition                 | Whether the employee left (Yes) or not (No) in the last year  |
| BusinessTravel            | Frequency of business travel (Travel_Rarely, Travel_Frequently, Non-Travel) |
| Department                | Department of the employee (Sales, Research & Development, Human Resources) |
| DistanceFromHome          | Distance from home to work (in kilometers)                    |
| Education                 | Education level (1=Below College, 2=College, 3=Bachelor, 4=Master, 5=Doctor) |
| EducationField            | Field of education (Life Sciences, Medical, Marketing, Technical Degree, Other) |
| EmployeeCount             | Number of employees (constant, always 1)                      |
| Gender                    | Gender (Male, Female)                                         |
| JobLevel                  | Job level of the employee                                     |
| JobRole                   | Job role of the employee (Sales Executive, Research Scientist, etc.) |
| MaritalStatus             | Marital status (Single, Married, Divorced)                    |
| MonthlyIncome             | Monthly income of the employee                               |
| NumCompaniesWorked        | Number of companies the employee has worked for              |
| Over18                    | Whether the employee is over 18 years old (Yes)              |
| PercentSalaryHike         | Percentage salary hike                                       |
| StandardHours             | Standard working hours (constant, always 8)                  |
| StockOptionLevel          | Stock option level granted to the employee                   |
| TotalWorkingYears         | Total working years                                           |
| TrainingTimesLastYear     | Number of training sessions attended last year               |
| YearsAtCompany            | Years at the current company                                 |
| YearsSinceLastPromotion   | Years since the last promotion                               |
| YearsWithCurrManager      | Years with the current manager                               |
| JobInvolvement            | Job involvement level (1=Low, 2=Medium, 3=High, 4=Very High) |
| PerformanceRating         | Performance rating (1=Low, 2=Good, 3=Excellent, 4=Outstanding) |
| EnvironmentSatisfaction   | Environment satisfaction (1=Low, 2=Medium, 3=High, 4=Very High) |
| JobSatisfaction           | Job satisfaction (1=Low, 2=Medium, 3=High, 4=Very High)      |
| WorkLifeBalance           | Work-life balance (1=Bad, 2=Good, 3=Better, 4=Best)          |

## Model Definition

The selected models for comparison are:

1. **K-Nearest Neighbors (KNN)**: KNN is an instance-based learning model that classifies new data based on proximity to existing instances in the training dataset. As a non-parametric algorithm, KNN stores all data examples and determines the class of new data through majority voting of its k nearest neighbors. Its simplicity and ability to handle multi-class data are advantages, but high memory requirements and slow prediction speed for large datasets are drawbacks.

2. **Support Vector Classifier (SVC)**: SVC is a classification model that works by finding the best hyperplane that separates different classes with the maximum margin. This model can be extended to non-linear classification using the kernel trick, which allows data to be mapped to higher dimensions. SVC is effective for high-dimensional datasets and cases with clear class margins but may be less efficient for very large datasets due to high computational complexity.

3. **Decision Tree**: Decision Tree is a non-parametric model that splits data into smaller subsets by forming a tree structure of decisions, where each node represents a test on an attribute, each branch represents the outcome of the test, and each leaf represents a class label. This model is easy to understand and interpret and can handle both numerical and categorical data. However, Decision Trees are prone to overfitting, especially on small or complex datasets.

4. **Random Forest**: Random Forest is an ensemble model consisting of many decision trees trained on random subsets of the training data and using majority voting for classification or averaging for regression as the final prediction. It improves accuracy and reduces the risk of overfitting compared to a single decision tree. Random Forest is excellent at handling datasets with complex and varied features but may be less interpretable due to the complexity of the model.

5. **XGBoost (Extreme Gradient Boosting)**: XGBoost is an optimized gradient boosting algorithm known for its speed and performance. It builds models by adding decision trees sequentially, where each new tree corrects errors from the previous tree. XGBoost is known for its high efficiency in handling large and complex datasets and its ability to handle imbalanced data. However, tuning XGBoost hyperparameters can be complex and requires a deeper understanding of the model.

## Model Evaluation

The Decision Tree model, both in its basic version and after being optimized with grid search, showed excellent performance in predicting employee attrition, as reflected by various evaluation metrics:

- **Recall** for both training and testing data is perfect (1.0) for both versions of the model. Recall measures the proportion of actual positive cases (employees leaving) that the model successfully identified. In this case, the model identified all attrition cases, which is crucial in a business context to minimize employee turnover.
- **Precision** for the 'Attrition Yes' class is 0.96, indicating that 96% of the employees identified by the model as likely to leave were correct. High precision is important to avoid unnecessary interventions with employees who do not plan to leave.
- **F1-score** for the 'Attrition Yes' class is 0.97, balancing precision and recall, providing a single metric for overall performance.
- **Overall accuracy** of the model is 0.99, indicating that 99% of the predictions made by the model were correct. This high accuracy demonstrates the model's effectiveness in classifying attrition and non-attrition cases.
- The **confusion matrix** shows 714 true negatives (TN), 6 false positives (FP), 3 false negatives (FN), and 136 true positives (TP). This reveals that the model makes very few mistakes in predictions, both in terms of false positives and false negatives.

The model's ability to accurately predict employees at risk of leaving (recall) is essential for proactive retention strategies. Identifying all potential leavers allows the company to take preventive actions to retain valuable employees. With only 3 false negatives, the model ensures that almost all at-risk employees are identified, minimizing unexpected turnover.

However, the model's weakness is that when tested on larger datasets, decision trees tend to overfit.

## Deployment

You can access the live model via the following link: [Employee Attrition Prediction on Hugging Face](https://huggingface.co/spaces/Gieorgie/Employee_Attrition_Prediction).

