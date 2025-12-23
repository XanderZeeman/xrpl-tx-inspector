import sys
from analyzer import analyze_transactions
from visualizer import plot_tx_types

if len(sys.argv) < 2:
    print("Usage: python3 src/main.py <path_to_tx_json>")
    sys.exit(1)

TX_FILE = sys.argv[1]

def print_summary(summary):
    print("XRPL Transaction Summary")
    print("------------------------")
    print(f"Total transactions: {summary['total_tx']}")
    print(f"Transaction types: {summary['tx_types']}")
    print(f"Total payments: {summary['total_payments']}")
    print(f"Total fees: {summary['total_fees']}")


if __name__ == "__main__":
    result = analyze_transactions(TX_FILE)
    print_summary(result)
    plot_tx_types(result['tx_types'])