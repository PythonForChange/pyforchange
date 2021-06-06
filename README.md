## FilesFormat

> PythonForChange FilesFormat allows me to easily integrate different functionalities of the Python For Change ecosystem.


### Sofware

[Get the last version of this software here](https://github.com/PythonForChange/FilesFormat/blob/main/pfcf.py).


### Installation
1. Download [PFCF](pfcf.py) into your proyect folder.
2. Import `pfcf` in your python file.
3. Use it.
4. Enjoy!


### Usage

#### How to import pfcf
```python
from pfcf import *
```
or `python import pfcf`.
 
#### Example 1
```python
l=LogFile("log1")
l.row("hello[") #this [ can not be printed
l.row("world\"") #this " can not be printed
l.section() #break
l.row("hello"+l.vip("[")) #this [ can be printed
l.row("world"+l.vip("\"")) #this " can be printed
l.section() #break
l.row("by Eanorambuena"+l.den("this text can not be printed"))
l.read()
```
First, log1_0.pfcf file is made.

```pfcf
hello[,world",|hello\[,world\",|by Eanorambuena~t~h~i~s~ ~t~e~x~t~ ~c~a~n~ ~n~o~t~ ~b~e~ ~p~r~i~n~t~e~d,
```

Then, log1_0.pfcf is read and printed.
```
hello
world

hello[
world"

by Eanorambuena
```
![image](https://user-images.githubusercontent.com/38821970/120838556-ee7c6380-c535-11eb-92c7-32edb9b71843.png)


Finally, `0` is append to log1_hist.pfcf file.
```pfcf
0
```
 
### Example 2
```python
l.reset()
l.p.den=":"
l.row(l.den("this text can not be printed"))
l.read()
```
 
First, log1_1.pfcf file is made.
```pfcf
:t:h:i:s: :t:e:x:t: :c:a:n: :n:o:t: :b:e: :p:r:i:n:t:e:d,
```

Then, log1_1.pfcf is read and printed.
```
```
![image](https://user-images.githubusercontent.com/38821970/120838601-fcca7f80-c535-11eb-92e2-afce35976807.png)


Finally, `1` is append to log1_hist.pfcf file.
```pfcf
0
1
```
 
#### Example 3
```python
data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})
data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})
data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
l2=LogFile("log2")
l2.fromDict(data)
```

First, log2.json file is made.
```json
{
    "clients": [
        {
            "first_name": "Sigrid",
            "last_name": "Mannock",
            "age": 27,
            "amount": 7.17
        },
        {
            "first_name": "Joe",
            "last_name": "Hinners",
            "age": 31,
            "amount": [
                1.9,
                5.5
            ]
        },
        {
            "first_name": "Theodoric",
            "last_name": "Rivers",
            "age": 36,
            "amount": 1.11
        }
    ]
}
```

Then, log2.json is read as a .pfcf file.
Finally, it is printed.
```
    clients: 
        
            first_name: Sigrid

            last_name: Mannock

            age: 27

            amount: 7.17
        

        
            first_name: Joe

            last_name: Hinners

            age: 31


            amount: 
                1.9

                5.5
            
        

        
            first_name: Theodoric

            last_name: Rivers

            age: 36
```
