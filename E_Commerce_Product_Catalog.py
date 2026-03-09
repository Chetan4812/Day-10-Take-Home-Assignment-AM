from collections import defaultdict

# -----------------------------
# Product Catalog (15+ products)
# -----------------------------

catalog = {
    "SKU001": {"name": "Laptop", "price": 65000, "category": "electronics",
               "stock": 15, "rating": 4.5, "tags": ["computer", "work", "portable"]},

    "SKU002": {"name": "Smartphone", "price": 35000, "category": "electronics",
               "stock": 20, "rating": 4.6, "tags": ["mobile", "android", "camera"]},

    "SKU003": {"name": "Bluetooth Headphones", "price": 3000, "category": "electronics",
               "stock": 0, "rating": 4.2, "tags": ["audio", "music", "wireless"]},

    "SKU004": {"name": "Gaming Mouse", "price": 1500, "category": "electronics",
               "stock": 25, "rating": 4.3, "tags": ["gaming", "computer"]},

    "SKU005": {"name": "Smartwatch", "price": 7000, "category": "electronics",
               "stock": 12, "rating": 4.1, "tags": ["wearable", "fitness", "mobile"]},

    "SKU006": {"name": "T-Shirt", "price": 800, "category": "clothing",
               "stock": 40, "rating": 3.9, "tags": ["casual", "cotton"]},

    "SKU007": {"name": "Jeans", "price": 2000, "category": "clothing",
               "stock": 18, "rating": 4.0, "tags": ["denim", "casual"]},

    "SKU008": {"name": "Jacket", "price": 3500, "category": "clothing",
               "stock": 10, "rating": 4.4, "tags": ["winter", "fashion"]},

    "SKU009": {"name": "Sneakers", "price": 4000, "category": "clothing",
               "stock": 0, "rating": 4.2, "tags": ["shoes", "sports"]},

    "SKU010": {"name": "Python Programming Book", "price": 1200, "category": "books",
               "stock": 30, "rating": 4.7, "tags": ["programming", "education"]},

    "SKU011": {"name": "Data Science Handbook", "price": 1500, "category": "books",
               "stock": 22, "rating": 4.6, "tags": ["data", "education"]},

    "SKU012": {"name": "Mystery Novel", "price": 600, "category": "books",
               "stock": 0, "rating": 3.8, "tags": ["fiction", "story"]},

    "SKU013": {"name": "Organic Honey", "price": 500, "category": "food",
               "stock": 35, "rating": 4.5, "tags": ["organic", "healthy"]},

    "SKU014": {"name": "Almonds", "price": 900, "category": "food",
               "stock": 50, "rating": 4.4, "tags": ["snack", "healthy"]},

    "SKU015": {"name": "Dark Chocolate", "price": 250, "category": "food",
               "stock": 0, "rating": 4.3, "tags": ["sweet", "snack"]}
}


# ---------------------------------
# 1. Search products by tag
# ---------------------------------

def search_by_tag(tag):
    tag_map = defaultdict(list)

    for sku, product in catalog.items():
        for t in product.get("tags", []):
            tag_map[t].append(product)

    return tag_map.get(tag, [])


# ---------------------------------
# 2. Out of stock products
# ---------------------------------

def out_of_stock():
    return {
        sku: product
        for sku, product in catalog.items()
        if product.get("stock", 0) == 0
    }


# ---------------------------------
# 3. Filter products by price range
# ---------------------------------

def price_range(min_price, max_price):
    if min_price > max_price:
        return {}

    return {
        sku: product
        for sku, product in catalog.items()
        if min_price <= product.get("price", 0) <= max_price
    }


# ---------------------------------
# 4. Category summary
# ---------------------------------

def category_summary():
    category_data = defaultdict(list)

    for product in catalog.values():
        category = product.get("category")
        if category:
            category_data[category].append(product)

    summary = {}

    for category, items in category_data.items():
        count = len(items)

        avg_price = sum(p.get("price", 0) for p in items) / count if count else 0
        avg_rating = sum(p.get("rating", 0) for p in items) / count if count else 0

        summary[category] = {
            "count": count,
            "avg_price": round(avg_price, 2),
            "avg_rating": round(avg_rating, 2)
        }

    return summary


# ---------------------------------
# 5. Apply discount to category
# ---------------------------------

def apply_discount(category, percent):

    if percent < 0 or percent > 100:
        return catalog

    discount_factor = (100 - percent) / 100

    return {
        sku: (
            {**product, "price": round(product.get("price", 0) * discount_factor, 2)}
            if product.get("category") == category
            else product
        )
        for sku, product in catalog.items()
    }


# ---------------------------------
# 6. Merge catalogs
# ---------------------------------

def merge_catalogs(catalog1, catalog2):
    merged = catalog1 | catalog2
    return merged


# ---------------------------------
# Example Usage
# ---------------------------------

print("Search tag 'healthy':")
print(search_by_tag("healthy"))

print("\nOut of Stock:")
print(out_of_stock())

print("\nProducts between 500 and 2000:")
print(price_range(500, 2000))

print("\nCategory Summary:")
print(category_summary())

print("\nDiscount on electronics (10%):")
print(apply_discount("electronics", 10))
