from funcs import get_transaction
import transaction as t


def main():
    last_executed_transactions = get_transaction()
    for trans in last_executed_transactions:
        t.Transactions(trans)
        print(t.Transactions(trans), '\n')


if __name__ == '__main__':
    main()
