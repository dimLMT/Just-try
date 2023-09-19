# Prediction of Product Sales
This report comprises two sections: Part 1 for data exploration and Part 2 for machine learning modeling of food item sales. The goal is to help the retailer better understand the properties of products and outlets that play crucial roles in increasing sales.

## Data Dictionary
<img width="800" alt="image" src="https://github.com/dimLMT/Prediction-of-Product-Sales/assets/36935946/343dc394-2763-4bd4-9361-a3c0fa4f0aa4">

## To prepare this data, the data was cleaned, and the data visualization was performed.
Some key visualizations are shown as follows:

<img width="500" alt="image" src="https://github.com/dimLMT/Prediction-of-Product-Sales/assets/36935946/a9c35fcf-39b0-47df-a47d-8088158b6345">

- This histogram shows that the majority of outlet sales are below $4,000.

<img width="700" alt="image" src="https://github.com/dimLMT/Prediction-of-Product-Sales/assets/36935946/53bade43-7383-4622-a3be-345a772a1a94">

- This countplot shows the types of food ranked from most popular to least popular in terms of sales quantity.
  
## Machine learning models and analysis
The finely tuned Random Forest model yielded our best results, as evidenced by the following metrics:

<img width="500" alt="image" src="https://github.com/dimLMT/Prediction-of-Product-Sales/assets/36935946/567c2c64-9da9-4dd5-97e9-3ceb502889dc">

- With this model, the error in predicting product sales is expected to fall within a range of ±$1,048.798. However, it's important to note that this model is not perfect, as indicated by an R-squared value of approximately 0.6.
- It is recommended to explore additional models to potentially improve predictive accuracy.

<img width="700" alt="image" src="https://github.com/dimLMT/Prediction-of-Product-Sales/assets/36935946/115fb79c-9c65-4fa7-8373-a88db4575074">

The random forest permutation importances had the following features as important: Item_MRP, Outlet_Type_Grocery Store, Outlet_Identifier_OUT027, Outlet_Type_Supermarket Type3, Outlet_Establishment_Year























