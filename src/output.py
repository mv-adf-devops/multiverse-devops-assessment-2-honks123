from extract import get_input

def main():
    filename = 'clean_results.csv'
    results = get_input(filename)
    for i in results:
        print(i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3] + ',' + i[4] + ',' + i[5])


if __name__ == '__main__':
    main()