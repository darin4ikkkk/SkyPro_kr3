from utils import load_file, sort_executed, sorted_by_date, data_sort, format_date, card_num_mask, print_data

loaded_file = load_file('operations.json')

sorted_executed_oper = sort_executed(loaded_file)

sorted_operations = data_sort(sorted_executed_oper)
sorted_operations = sorted_operations[:5]

print(print_data(sorted_operations))


