from extract import get_input, remove_duplicates, remove_empty_lines, capitalise_names, validate_answer_3
import csv


def main():
    filename = 'results.csv'
    results = get_input(filename)
    print("Original file:")
    print(results)
    print("\n")
    results_new = remove_duplicates(results)
    
    print("Without Duplicates:")
    print(results_new)
    print("\n")

    results_noempty = remove_empty_lines(results_new)
    print("Without Empty lines:")
    print(results_noempty)
    
    results_capitalised = capitalise_names(results_noempty)
    print("After names capitalised:")
    print(results_capitalised)

    results_validated = validate_answer_3(results_capitalised)
    print("After answer 3 validated:")
    print(results_validated)

    with open('clean_results.csv', 'wb', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(results_validated)

    

if __name__ == '__main__':
    main()