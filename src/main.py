import json
import matplotlib.pyplot as plt

TX_FILE = 'data/sample_tx.json'

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

def print_summary(summary):
    print("XRPL Transaction Summary")
    print("------------------------")
    print(f"Total transactions: {summary['total_tx']}")
    print(f"Transaction types: {summary['tx_types']}")
    print(f"Total payments: {summary['total_payments']}")
    print(f"Total fees: {summary['total_fees']}")

def plot_tx_types(summary):
    types = list(summary['tx_types'].keys())
    counts = list(summary['tx_types'].values())

    plt.rcParams['figure.figsize'] = [4,6]
    plt.bar(types, counts)
    plt.xlabel('Transaction Types')
    plt.ylabel('Counts')
    plt.title('XRPL Transaction Types Distribution')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    result = analyze_transactions(TX_FILE)
    print_summary(result)
    plot_tx_types(result["tx_types"])