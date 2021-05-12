# prettytitle

This program prettifies commented titles for copying into python scripts.

## Set Up

1. Clone the project using:

```bash
git clone https://github.com/kevinbennet/prettytitle.git
```
## Usage
To run:
```python
python prettytitle.py "<title here>" [options]

positional arguments:
  title                 title name to prettify

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        set length of title box (default: 119)
  -c, --caps            capitalize title
```
## Sample Output
```python
$ python prettytitle.py "capitalized title" -l 79 -c

###############################################################################
############################## CAPITALIZED TITLE ##############################
###############################################################################
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
