# PyHasher
Python script to hash strings with **SHA256**.

## Requirements

* [Python 3+](https://www.python.org)
* [Pandas](https://pandas.pydata.org/)
* [Hashlib](https://docs.python.org/3/library/hashlib.html)

## Installation

1. **Install Python 3+:** Download and Install the lastest version of Python from [here](https://www.python.org/downloads/)
2. **Install Pandas:** open the command line (cmd or Símbolo del sistema) in Windows and write: 

```
pip install pandas
```

3. **Install hashlib:** now write: 

```
pip install hashlib
```

## How to run the script

* Paste all the strings that you want to hash inside the **ANIs.txt** file under the ANI text. **DO NOT erase the first string: ANI.**
* Open the folder where you placed the **hasher.py** file.
* Hold **Shift** and right click inside the folder.
* Select: **Open command window her** or **Abrir la ventana de PowerShell aquí** or **Abrir símbolo del sistema aquí**. 
* Once it's open, write this:

```
python hasher.py
```

* Wait until it shows the path to the folder again as that means that the script completed the hashing process.
* Open the **output.txt** file and all the strings from the **ANIs.txt** file should have a hash next to it.


