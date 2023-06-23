import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("data/car_sales.csv")

# Question 1: What is the average price of the cars in the dataset?
average_price = df["Price"].mean()
print("Average price of the cars: $", average_price)

# Question 2: How many cars were sold in each year?
cars_sold_by_year = df.groupby("Year")["Car Model"].count()
print("Number of cars sold by year:")
print(cars_sold_by_year)

# Additional Data Analysis Tasks
# Calculate the total sales revenue
df["Revenue"] = df["Price"] * df["Quantity"]
total_revenue = df["Revenue"].sum()
print("Total sales revenue: $", total_revenue)

# Find the car model with the highest price
max_price_car = df.loc[df["Price"].idxmax(), "Car Model"]
print("Car model with the highest price:", max_price_car)

# Filter the dataset to include only cars sold after 2010
filtered_df = df[df["Year"] > 2010]

# Sort the dataset by price in descending order
sorted_df = df.sort_values("Price", ascending=False)

# Calculate the average price of cars sold in each year
average_price_by_year = df.groupby("Year")["Price"].mean()
print("Average price of cars sold by year:")
print(average_price_by_year)

# Calculate the total sales for each car model
total_sales_by_model = df.groupby("Car Model")["Quantity"].sum()
print("Total sales by car model:")
print(total_sales_by_model)

# Convert the "Year" column to datetime format
df["Year"] = pd.to_datetime(df["Year"], format="%Y")

# Calculate the number of cars sold each month
df["Month"] = df["Year"].dt.month
cars_sold_by_month = df.groupby("Month")["Quantity"].sum()
print("Number of cars sold by month:")
print(cars_sold_by_month)

# Export the updated DataFrame to a new CSV file
df.to_csv("data/car_sales_updated.csv", index=False)

# Visualization: Bar Plot of Sales by Car Model
import matplotlib.pyplot as plt

# Group the dataset by car model and calculate total sales
sales_by_model = df.groupby("Car Model")["Quantity"].sum()

# Sort the sales in descending order
sorted_sales = sales_by_model.sort_values(ascending=False)

# Extract the top 10 selling car models and their sales
top_10_models = sorted_sales.head(10)
top_10_model_names = top_10_models.index
top_10_model_sales = top_10_models.values

# Create a bar plot of sales by car model
plt.bar(top_10_model_names, top_10_model_sales)
plt.title("Top 10 Car Models by Sales")
plt.xlabel("Car Model")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Additional Analysis Tasks
# Calculate the total sales by brand
df["Brand"] = df["Car Model"].str.split(" ", n=1, expand=True)[0]
total_sales_by_brand = df.groupby("Brand")["Quantity"].sum()
print("Total sales by brand:")
print(total_sales_by_brand)

# Calculate the average price by brand
average_price_by_brand = df.groupby("Brand")["Price"].mean()
print("Average price by brand:")
print(average_price_by_brand)

# Calculate the total revenue by brand
df["Brand Revenue"] = df["Price"] * df["Quantity"]
total_revenue_by_brand = df.groupby("Brand")["Brand Revenue"].sum()
print("Total revenue by brand:")
print(total_revenue_by_brand)

# Calculate the total sales by year and brand
total_sales_by_year_brand = df.groupby(["Year", "Brand"])["Quantity"].sum()
print("Total sales by year and brand:")
print(total_sales_by_year_brand)

# Calculate the average price by year and brand
average_price_by_year_brand = df.groupby(["Year", "Brand"])["Price"].mean()
print("Average price by year and brand:")
print(average_price_by_year_brand)

# Calculate the total revenue by year and brand
df["Year Brand Revenue"] = df["Price"] * df["Quantity"]
total_revenue_by_year_brand = df.groupby(["Year", "Brand"])["Year Brand Revenue"].sum()
print("Total revenue by year and brand:")
print(total_revenue_by_year_brand)

# Export the updated DataFrame to a new Excel file
df.to_excel("data/car_sales_updated.xlsx", index=False)
