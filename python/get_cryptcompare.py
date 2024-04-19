"""depends on env var CRYPT_COMPARE_API_KEY"""
import logging
import os
from datetime import datetime

import pandas as pd
import requests


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BASE_URL = "https://min-api.cryptocompare.com/data/v2/histoday"
API_KEY = os.environ.get("CRYPT_COMPARE_API_KEY")
BTC_LAUNCH_DATE = 1230940800
LIMIT = 2000
params = {
    "fsym": "BTC",
    "tsym": "USD",
    "limit": LIMIT,
    "api_key": API_KEY
}


def fetch_data() -> None:
    results = []
    not_first = False
    max_responses = 5 # prevent infinite loop if sentinel not reached
    today = int(datetime.now().timestamp())
    time_to = today

    for _ in range(max_responses):
        if time_to == BTC_LAUNCH_DATE:
            logging.info("Final response received with less than limit records.")
            break

        if not_first:
            time_to -= (LIMIT + 1) * 86400
            if (time_to - LIMIT * 86400) < BTC_LAUNCH_DATE:
                params["limit"] = (time_to - BTC_LAUNCH_DATE) // 86400
                time_to = BTC_LAUNCH_DATE + (time_to - BTC_LAUNCH_DATE)

        params["toTs"] = time_to

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "Data" in data and "Data" in data["Data"]:
            records = data["Data"]["Data"]

            results[:0] = records

            not_first = True

            begin_time = datetime.utcfromtimestamp(records[0]["time"]).strftime("%Y-%m-%d %H:%M:%S")
            end_time = datetime.utcfromtimestamp(records[-1]["time"]).strftime("%Y-%m-%d %H:%M:%S")

            logging.info(f"Processed {len(records)} new records, current total: {len(results)} records.")
            logging.info(f"Processed from {begin_time} to {end_time}")
        else:
            logging.error("No data found in response or invalid API response.")
            break

    if results:
        df = pd.DataFrame(results)
        df.to_csv("btcdailyprice.csv", index=False)
        logging.info("Data successfully written to btcdailyprice.csv.")
    else:
        logging.info("No data to write.")

if __name__ == "__main__":
    logging.info("Starting data fetching operations.")
    fetch_data()
    logging.info("Data fetching operations completed.")
