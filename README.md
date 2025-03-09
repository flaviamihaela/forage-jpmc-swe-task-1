# Stock Market Simulation

## Overview
This project simulates a stock market data retrieval and analysis client. It fetches stock price data from a local API, processes bid-ask spreads, calculates stock prices, and determines the price ratio between two stocks (ABC and DEF). The project also includes unit tests to ensure the correctness of its computations.

## Features
- **Fetch stock data** from a simulated market server.
- **Calculate stock prices** using the midpoint of bid and ask prices.
- **Compute stock price ratios** to analyze relative stock performance.
- **Run automated tests** to validate computations.

## Prerequisites
- Python 3.x
- Internet connection (to simulate HTTP requests)
- A running server that provides stock quotes at `http://localhost:8080/query?id={}`

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd stock-market-simulation
   ```
2. Install dependencies (if required):
   ```sh
   pip install requests unittest
   ```

## Usage
Run the client to fetch stock data and compute price ratios:
```sh
python client.py
```

To execute unit tests:
```sh
python -m unittest client.py
```

## Code Breakdown
### `getDataPoint(quote)`
- Extracts stock name, bid price, ask price, and computes the price as the midpoint between bid and ask.

### `getRatio(price_a, price_b)`
- Computes the ratio of two stock prices while handling division by zero.

### Main Execution
- Fetches stock data `N` times and prints quotes.
- Calculates and prints the price ratio between ABC and DEF stocks.

### Unit Tests
- Tests correct computation of stock prices.
- Validates the behavior of `getRatio()` under different scenarios.

## License
This project is provided under the MIT License.

## Future Improvements
- Implement a visualization dashboard.

