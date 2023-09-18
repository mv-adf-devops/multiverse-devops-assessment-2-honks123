from extract import get_input, remove_duplicates

def main():
    filename = 'results.csv'
    results = get_input(filename)
    print(results)
    
    results_new = remove_duplicates(results)
    
    print(results_new)

    

if __name__ == '__main__':
    main()