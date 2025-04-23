import pandas as pd

# Load dataset
file_path = "C:/Users/hp/OneDrive/Desktop/Amazon_Sales_Analysis/data/raw/amazon_sales_raw.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicates
df = df.drop_duplicates()

# Convert order_date to datetime if it exists
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Remove whitespace from product_name
if 'product_name' in df.columns:
    df['product_name'] = df['product_name'].astype(str).str.strip()

# Drop rows with missing values in key columns
df = df.dropna(subset=['sales']) if 'sales' in df.columns else df
df = df.dropna(subset=['order_date']) if 'order_date' in df.columns else df

# --- Safer currency cleaning function ---
def clean_currency(x):
    try:
        x = str(x).replace('₹', '').replace('%', '').replace(',', '').strip()
        return float(x)
    except:
        return None  # return None if conversion fails

# Clean numeric columns
for col in ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: clean_currency(x) if pd.notnull(x) else None)

# Save cleaned data
clean_path = "C:/Users/hp/OneDrive/Desktop/Amazon_Sales_Analysis/data/processed/amazon_sales_cleaned.csv"
df.to_csv(clean_path, index=False)

print(f"\n✅ Cleaned data saved to: {clean_path}")
