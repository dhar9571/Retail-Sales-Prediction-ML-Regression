# Retail-Sales-Prediction-ML-Regression

Link to the Live Server of my Sales Predicting Application:

https://retail-sales-prediction-ml-regression-dharmendra.streamlit.app/

## Business Use Case:
The business use case of this project is to leverage machine learning techniques to predict retail sales accurately. Forecasting sales, retailers can optimize their operations, reduce costs, and enhance overall profitability.

## Potential Impact:
The potential impact of this project is significant for both retailers and the broader retail industry. Using and End to End deployed Sales forecasting model, retailers can have an understanding on their business goals and changes into their marketing and sales strategies.

## Approach:

-Dataset Explanation: The project used two datasets, 'rossmann_data' and 'store_data,' comprising a total of 1,017,209 entries and 18 columns including a Date column which is required in order to capture the seasonality of the timeseries data. The integration of these datasets provided comprehensive information for sales prediction.

-Feature Engineering: Data preprocessing involved handling missing values, outliers, and categorical encoding. Techniques like label encoding and feature manipulation were employed to create meaningful features. This step was crucial for preparing the data for machine learning modelling.

-Algorithms: Multiple machine learning algorithms were trained, including Linear Regression, Ridge, Lasso, ElasticNet, DecisionTree, and RandomForest Regression, XGBoost and Artificial Neural Networks. Among them, the RandomForest Regression model demonstrated the best performance, achieving an accuracy of 93% on Sales and 85% on Customers data. However, opted XGBoost Regression model with 92% accuracy on Sales and 82% on Customers prediction due to unavailability of higher computational resources.

Training: training two different models. One is for customers prediction, as it cannot be assumed by the retailers. This prediction number of customers can then be used to predict the Sales using second trained model.

-End Output: The end output of the project is a successfully deployed predictive model application capable of forecasting retail sales.

## Challenges Faced:
-Computational Memory: The project encountered challenges related to computational memory, likely due to the large dataset size and complexity. Therefore, I switched to opt XGBoost ML model for both Sales and Customers prediction as RandomForest was not loading properly due to its large size.

## Future Scope:
While the project has already achieved a significant milestone by deploying the best-performing model for live predictions, there are several avenues for further enhancement and expansion:

Continued Model Refinement: The journey to excellence in predictive accuracy is ongoing. We will continue to fine-tune our machine learning models, explore advanced algorithms, and optimize hyperparameters to further improve the precision of our sales predictions.

Data Augmentation: Expanding the dataset by collecting more historical sales and relevant data can enhance the model's performance. Incorporating additional features and data sources can provide richer insights and better forecasting capabilities.

Real-Time Data Integration: Integrating real-time data sources, such as current sales, weather conditions, or market trends, can provide the model with up-to-the-minute information, resulting in more accurate and responsive predictions.

In conclusion, our project's potential extends beyond its current deployment. By focusing on these future initiatives, we aim to further revolutionize the retail industry, providing retailers with cutting-edge predictive analytics that drive better decision-making and increased profitability. This expanded future scope outlines several directions for improvement and development, even though the model is already deployed. It demonstrates your commitment to continuous improvement and highlights the potential for further impact in the retail industry.
