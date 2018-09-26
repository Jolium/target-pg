# target-pg

### Target Passorwds Generator
### Generates passwords with the target in mind!


## Requirements
* [Python](https://www.python.org/downloads/release/python-2714/)
* [Requests](https://pypi.org/project/requests/)


## Starting point

Through social engineering or otherwise get information about your target. Information such as name, surname, place of birth, place where he is living, name of heroes or idols, etc. Enter these words to create (Passwords_list.txt) a list of possible passwords for this target.


## How it works

1. Choose settings (default/change)
   1. ex: 'd'  (default)
1. Enter word (just one each time)
   1. ex:  'AbcDef' (press enter)
1. target-pg creates a list of passwords (Passwords_list.txt)
   * AbcDef0000
   * AbcDef0001
   * AbcDef0002
   * ......   ....
   * AbcDef000
   * AbcDef001
   * AbcDef002
   * ......   ....
   * AbcDef00
   * AbcDef01
   * AbcDef02
   * ......   ....
   * AbcDef0
   * AbcDef1
   * AbcDef2
   * ......   ....
1. Enter another word
   1. ex:  'aBc' (press enter)
1. target-pg adds this new word to 'Passwords_list.txt'
   * aBc0000
   * aBc0001
   * aBc0002
   * ...   ....
1. Write '//' (press enter) to exit target-pg



## Settings:

* [1] Passwords minimum length ...................................... (from 1 to 12)
* [2] Passwords maximum length ...................................... (from 8 to 18)
* [3] Passwords with numbers before ........ (1234abcd, 567890abcd)
* [4] Passwords with numbers after ............ (abcd1234, abcd567890)
* [5] Passwords with numbers before and after ..... (1234abcd5678)
* [6] Passwords with capital/small letters .... (ABCD1234/abcd1234)
* [7] Length of numbers ................ (abcd1234, abcd12, abcd123456)