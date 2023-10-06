# Retail-Sales-Prediction-ML-Regression

# Business Use Case:
The business use case of this project is to leverage machine learning techniques to predict retail sales accurately. forecasting sales, retailers can optimize their operations, reduce costs, and enhance overall profitability.

# Potential Impact:
The potential impact of this project is significant for both retailers and the broader retail industry.

# Approach:

-Dataset Explanation: The project used two datasets, 'rossmann_data' and 'store_data,' comprising a total of 1,017,209 entries and 18 columns. The integration of these datasets provided comprehensive information for sales prediction.

-Feature Engineering: Data preprocessing involved handling missing values, outliers, and categorical encoding. Techniques like label encoding and feature manipulation were employed to create meaningful features. This step was crucial for preparing the data for machine learning modelling.

-Algorithms: Multiple machine learning algorithms were trained, including Linear Regression, Ridge, Lasso, ElasticNet, DecisionTree, and RandomForest Regression. Among them, the RandomForest Regression model demonstrated the best performance, achieving an accuracy of 92%.

-End Output: The end output of the project is a predictive model capable of forecasting retail sales.

# Challenges Faced:
-Handling Null Values was a difficult task as 4 of the features were having a high number of missing values. In order to handle this, I used median for the features having potential outliers and mean for the features not having outliers.

-Computational Memory: The project encountered challenges related to computational memory, likely due to the large dataset size and complexity. Therefore, I switched to use simple ML models such as Linear regression, decision tree and random forest techniques.

# Future Scope:
The immediate future scope includes deploying the best-performing model for live predictions, making it accessible to retailers for real-time decision support.

In conclusion, this project has the potential to bring significant benefits to the retail industry by providing accurate sales predictions. The combination of data preprocessing, feature engineering, and machine learning models forms a strong foundation for future enhancements and real-world applications.
