from datatable import DataTable


def main():
    """
    Main function
    """
    table = DataTable(['col1', 'col2', 'col3'])
    table.append({"col1": 12, 'col3': "Oky"})
    table.append({"col2": "Foreach", 'col3': "Lina"})
    table.append({"col1": 22, 'col3': "Lina"})
    print(table)

    print({"col1": 12} in table)
    print({"col200": "No way"} in table)
    # print(1000 in table) Not supported yet

if __name__ == '__main__':
    main()
