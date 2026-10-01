import json
import logging
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


API_URL = "https://fakestoreapi.com/products"
RAW_DIR = Path("data/raw/products")


def fetch_products():
    logger.info("Starting product extraction")

    response = requests.get(
        API_URL,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    logger.info(
        "Successfully extracted %d products",
        len(data),
    )

    return data


def save_raw_data(data):
    RAW_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = RAW_DIR / "products.json"

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
        )

    logger.info(
        "Raw data saved to %s",
        output_file,
    )

    return output_file


def main():
    products = fetch_products()
    save_raw_data(products)


if __name__ == "__main__":
    main()