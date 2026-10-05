import json

import pandas as pd


def load_raw_products():
    with open(
        "data/raw/products/products.json",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def format_products(data):
    df = pd.json_normalize(data)

    df = df.rename(
        columns={
            "rating.rate": "rating_rate",
            "rating.count": "rating_count",
        }
    )

    df = df.astype(
        {
            "id": "int64",
            "title": "string",
            "price": "float64",
            "description": "string",
            "category": "string",
            "image": "string",
            "rating_rate": "float64",
            "rating_count": "int64",
        }
    )

    return df


def main():
    data = load_raw_products()
    df = format_products(data)

    print(df)

    print("\n=== DATA QUALITY REPORT ===")

    # Missing values
    print("\nMissing values:")
    print(df.isna().sum())

    # Duplicate rows
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # Duplicate IDs
    print("\nDuplicate product IDs:")
    print(df["id"].duplicated().sum())

    # Range validation
    print("\nInvalid IDs:")
    print((df["id"] <= 0).sum())

    print("\nInvalid prices:")
    print((df["price"] < 0).sum())

    print("\nInvalid ratings:")
    print(((df["rating_rate"] < 0) | (df["rating_rate"] > 5)).sum())

    print("\nInvalid rating counts:")
    print((df["rating_count"] < 0).sum())


if __name__ == "__main__":
    main()