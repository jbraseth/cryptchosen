# btcdailyprice dataset

## Daily Bitcoin Price Data

### Description

Daily pricing data for Bitcoin (BTC), capturing market dynamics and trading volumes.

### Usage with downloaded CSV

> ℹ️ Make sure that the `btcdailyprice.csv` file is in your current working directory. If it's in another directory, you would need to specify the correct path to the file.

```R
library(readr)
btcdailyprice <- read_csv("btcdailyprice.csv")
```

### Usage with installed package (Not Implemented)

```R
devtools::install_github("jbraseth/cryptchosen")
cryptchosen::btcdailyprice
```

### Format

A data frame with the following columns:

- `year`: Year of recording.
- `month`: Month of recording.
- `day`: Day of recording.
- `high`: The highest price of Bitcoin on the day (in USD).
- `low`: The lowest price of Bitcoin on the day (in USD).
- `open`: The price of Bitcoin at the market open (in USD).
- `close`: The price of Bitcoin at the market close (in USD).
- `volumefrom`: The total volume of Bitcoin traded.
- `volumeto`: The total value in USD of the volume of Bitcoin traded.
- `conversionType`: The type of price conversion used (e.g., "direct").
- `conversionSymbol`: Any symbol used for conversion, if applicable (typically empty if conversionType is "direct").

### Details

The `btcdailyprice` dataframe provides a structured format for storing and analyzing Bitcoin's price data over time. This can be useful for historical analysis, forecasting models, and understanding market behavior on a day-to-day basis.

### Source

This dataset is compiled using data retrieved from the CryptoCompare API, specifically through a REST API call retrieving 2000 days of daily historical price information for Bitcoin (BTC) up to and including the specified date, 03/22/2024, in terms of USD. 

### API Call Used On [CryptoCompare](https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistoday)

```
https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&toTs=1711065600
````
