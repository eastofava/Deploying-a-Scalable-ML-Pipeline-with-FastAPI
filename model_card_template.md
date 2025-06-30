# Model Card

## Model Details
This model is a Random Forest Classifier trained to predict whether an individual's income exceeds $50K per year based on census data features such as age, education, occupation, and hours worked per week. It uses one-hot encoding for categorical features and label binarization for the target variable. 

## Intended Use
The model is intended for educational purposes and demonstration purposes to practice building and deploying ML pipelines and APIs. It is not intended for production deployment or for making any financial decisions.

## Training Data
The model was trained on the UCI Census dataset, constaining demographic data and income lables for approximately 30,000 individuals. The data was processed using one-hot encoding for categorical variables and split into an 80/20 train-test split.

## Evaluation Data
Evaluation was performed on the 20% test split from the original dataset, ensuring the model's performance metrics reflect unseen data within the same distribution.

## Metrics
Precision: 0.7419 
Recall: 0.6384 
F1: 0.6863
Additionally, slice metrics were computed across categorical slices to evaluate performance disparities between subgroups. Results were logged in slice_output.txt.

## Ethical Considerations
The model may reflect societal biases present in the data, particularly around sensitive attributes such as race, gender, or occupation. This model should not be used to make employment or financial decisions without extensive fairness and bias auditing.

## Caveats and Recommendations
This model is limited to the dataset's demographic distribution and may lack generality. As it was built for educational purposes, it lacks production-grade validation, monitoring, and explainability features. Future work could include hyperpareter tuning, bias mitigation strategies, and model interpretability tools for ethical deployment.
