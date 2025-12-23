import json


def analyze_transactions(file_path):
    """
    Analyze XRPL-like transactions in JSON and return a summary.
    """
    with open(file_path, "r") as f:
        transactions = json.load(f)

    summary = {
        "total_tx": len(transactions),
        "tx_types": {},
        "total_payments": 0,
        "total_fees": 0
    }

    for tx in transactions:
        tx_type = tx.get("TransactionType", "Unknown")
        fee = int(tx.get("Fee", 0))
        summary["total_fees"] += fee

        # Count transaction types
        summary["tx_types"][tx_type] = summary["tx_types"].get(tx_type, 0) + 1

        # Sum payment amounts
        if tx_type == "Payment":
            amount = int(tx.get("Amount", 0))
            summary["total_payments"] += amount

    return summary