# 3_exploratory_data_analysis.ipynb

# 🛠 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder to save plots if it doesn't exist
os.makedirs("../plots", exist_ok=True)

# Set visual style
sns.set(style="whitegrid")
plt.style.use('ggplot')

# 📥 Load Cleaned Data
df = pd.read_csv("../data/processed/amazon_sales_cleaned.csv")

# 👁 Basic Info
print("Shape of the dataset:", df.shape)
df.info()
df.describe(include="all")

# 🔍 Check Missing Values
missing = df.isnull().sum()
print("\nMissing values:\n", missing[missing > 0])

# 🧹 Fill missing values
df["rating_count"] = df["rating_count"].fillna(0)
df["rating"] = df["rating"].fillna(df["rating"].mean())

# 📊 Distribution of Ratings
plt.figure(figsize=(8, 5))
sns.histplot(df['rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Product Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("../plots/rating_distribution.png")
plt.show()

# 🔢 Most Common Actual Prices
plt.figure(figsize=(10, 6))
df['actual_price'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Most Common Actual Prices')
plt.xlabel('Price (₹)')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../plots/top_actual_prices.png")
plt.show()

# 🔢 Most Common Discounted Prices
plt.figure(figsize=(10, 6))
df['discounted_price'].value_counts().head(10).plot(kind='bar', color='teal')
plt.title('Top 10 Most Common Discounted Prices')
plt.xlabel('Price (₹)')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../plots/top_discounted_prices.png")
plt.show()

# 💰 Average Discount % by Category
df['main_category'] = df['category'].apply(lambda x: str(x).split('|')[0])
avg_discount = df.groupby('main_category')['discount_percentage'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
avg_discount.plot(kind='bar', color='orange')
plt.title('Average Discount Percentage by Main Category')
plt.xlabel('Main Category')
plt.ylabel('Average Discount (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../plots/avg_discount_by_category.png")
plt.show()

# ⭐ Average Rating by Main Category
avg_rating = df.groupby('main_category')['rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
avg_rating.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by Main Category')
plt.xlabel('Main Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../plots/avg_rating_by_category.png")
plt.show()

# 📈 Rating vs. Discount Percentage
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='discount_percentage', y='rating', alpha=0.6)
plt.title('Discount % vs. Rating')
plt.xlabel('Discount Percentage')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig("../plots/discount_vs_rating.png")
plt.show()

# 💬 Top 10 Most Reviewed Products
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')
top_reviewed = df.sort_values(by='rating_count', ascending=False).head(10)
top_reviewed['short_name'] = top_reviewed['product_name'].apply(lambda x: x[:40] + '...' if len(x) > 40 else x)

plt.figure(figsize=(16, 9))
sns.barplot(data=top_reviewed, x='short_name', y='rating_count')
plt.title('Top 10 Most Reviewed Products', fontsize=16)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Rating Count', fontsize=12)
plt.xticks(rotation=60, ha='right')
plt.tight_layout(pad=2.0)
plt.savefig("../plots/top_reviewed_products.png")
plt.show()

print("\n✅ Step 3 EDA completed successfully and plots saved to '../plots/' folder!")
