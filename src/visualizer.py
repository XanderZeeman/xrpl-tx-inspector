import matplotlib.pyplot as plt

def plot_tx_types(tx_types):
    types = list(tx_types.keys())
    counts = list(tx_types.values())

    plt.rcParams['figure.figsize'] = [4,6]
    plt.bar(types, counts)
    plt.xlabel('Transaction Types')
    plt.ylabel('Counts')
    plt.title('XRPL Transaction Types Distribution')
    plt.tight_layout()
    plt.show()
