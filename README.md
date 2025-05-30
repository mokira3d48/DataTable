# DATA TABLE
![](https://img.shields.io/badge/Python-3-blue)
![](https://img.shields.io/badge/lastest-2025--05--29-green)
![](https://img.shields.io/badge/contact-dr.mokira%40gmail.com-blueviolet)

Cloneable referential to get an implementation of DataTable with the best practice.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#uage)
- [Features](#features)
- [To contribute](#to-contribute)
- [Licence](#licence)
- [Contact](#contact)


## Description

Implementation of a basic DataTable for sevaral usage in your programs or application.

## Installation

To install the project, make sure you have Python 3.x version.


```bash
git clone git@gitlab.com:mokira3d48/DataTable.git datatable
cd datatable
```

---

## Usage

Here is an example how to add a new object row:

```python
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


if __name__ == '__main__':
    main()

```

```
   col1    col2    col3
     12    None     Oky
   None Foreach    Lina
     22    None    Lina

```

## Features

- Add new row.
- Remove a indexed row like a python list.
- Insert and replace a row using its index.
- Retrieve the last row using `pop` method exactly like a python list.


---

## To contribute

Contributions are welcome! Please follow these steps:

1. Create a new branch for your feature (`git checkout -b feature/my-feature`);
2. Commit your changes (`git commit -m 'Adding a new feature'`);
3. Push toward the branch (`git push origin --set-upstream feature/my-feature`);
4. Create a new *Pull Request* or *Merge Request*.

## Licence

This project is licensed under the MIT License. See the file [LICENSE](LICENSE)
for more details, contact me please.

## Contact

For your question or suggestion, contact me please :

- **Name** : Dr Mokira
- **Email** : dr.mokira@gmail.com
- **GitHub** : [mokira3d48](https://github.com/mokira3d48)
- **GitLab** : [mokira3d48](https://github.com/mokira3d48)
