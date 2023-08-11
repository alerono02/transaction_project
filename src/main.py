from funcs import get_transaction, load_data
import transaction as t


def main():
    last_executed_transactions = get_transaction(load_data('operations.json'))
    for trans in last_executed_transactions:
        t.Transactions(trans)
        print(t.Transactions(trans), '\n')


if __name__ == '__main__':
    main()
