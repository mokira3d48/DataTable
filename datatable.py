__author__ = 'Dr Mokira'
__version__ = '0.1.0'


class DataTable(list):
    """
    The data table is the eazy way to manage data as a table

    :arg columns: The list of columns of your table
    :type columns: list of str
    """
    def __init__(self, columns):
        self.columns = columns
        self.max_str_length = -float('inf')

    def preprocess(self, item):
        """
        Method to pre-process each new row behind to insert it into data table
        """
        new_row = [None] * len(self.columns)
        for index, col_name in enumerate(self.columns):
            new_row[index] = item.get(col_name)
            str_len = len(str(new_row[index]))
            if str_len > self.max_str_length:
                self.max_str_length = str_len
        return new_row

    def append(self, item):
        """
        Method to add a new row into data table

        :param item: The dictionary that contents the data of new row foreach
          columns. If a column missing, by default we set NoneType value.
        :type item: typing.Dict[str, object]
        """
        new_row = self.preprocess(item)
        super().append(new_row)

    def insert(self, index, item):
        """
        Method to insert a new row into data table at a specific index

        :param item: The dictionary that contents the data of new row foreach
          columns. If a column missing, by default we set NoneType value.
        :type item: typing.Dict[str, object]
        """
        if not (0 <= index < len(self)):
            raise IndexError("The index given is out of range")
        new_row = self.preprocess(item)
        super().insert(index, new_row)

    def pop(self):
        """
        Method to retrieve the last row from this data table

        :rtype: typing.Dict[str, object]
        """
        row = self.pop()
        item = {col_name:row[i] for i, col_name in enumerate(self.columns)}
        return item

    def __setitem__(self, index, item):
        if not (0 <= index < len(self)):
            raise IndexError("The index given is out of range")
        new_row = self.preprocess(item)
        super().__setitem__(index, new_row)

    def __str__(self):
        string = ' '.join(
            [("{name:>" + str(self.max_str_length) + "s}").format(name=name)
             for name in self.columns])
        string += "\n"
        for row in self:
            string += ' '.join([
                ("{v:>" + str(self.max_str_length) + "s}").format(v=str(col))
                for col in row])
            string += "\n"
        return string
