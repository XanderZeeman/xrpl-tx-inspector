# XRPL Transaction Inspector

A lightweight Python tool for analyzing and visualizing XRP Ledger (XRPL)-style transaction data from JSON files.

This project parses transaction records, aggregates key network metrics, and provides a simple visualization of transaction activity by type.

---

## Features

- Parses XRPL-like transaction data from JSON
- Counts total transactions and transaction types
- Aggregates total payment amounts and fees
- Visualizes transaction type distribution using matplotlib
- CLI-based usage for flexible analysis of different datasets

---

## Example Output

```bash
XRPL Transaction Summary
------------------------
Total transactions: 6
Transaction types: {'Payment': 3, 'AccountSet': 1, 'OfferCreate': 2}
Total payments: 9400000
Total fees: 96
```

---

## Usage

```bash
python3 src/main.py data/sample_tx.json
```
