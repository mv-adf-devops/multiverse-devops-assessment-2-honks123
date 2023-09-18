from extract import get_input, remove_duplicates, remove_empty_lines

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

    

if __name__ == '__main__':
    main()