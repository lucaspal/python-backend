def append_name(file_name, param):
    with open(file_name, 'a') as file:
        file.write('\n\n' + param)


def main():
    signature = input('Insert name: \n')
    print('Starting...')
    file_name = 'from_zero_one.txt'
    create_file(file_name)
    print('Done creating file.')
    append_name(file_name, signature)
    print('Done appending name')


def create_file(file_name):
    with open(file_name, 'wt') as new_file:
        new_file.write('My first document')


if __name__ == '__main__':
    main()
