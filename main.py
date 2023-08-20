from utils import load_file, get_executed, get_sorted_operations


def main():
    list_from_file = load_file("operations.json")
    executed_operation_list = get_executed(list_from_file)
    last_five_operations = get_sorted_operations(executed_operation_list)[-5:]

    for operation in last_five_operations:
        print(f'{operation.get_convert_date()} {operation.get_description()}\n'
              f'{operation.get_from()} -> {operation.get_to()}\n'
              f'{operation.get_amount()}\n')



if __name__ == '__main__':
    main()
