# :beer:

## Buy people :beer:

- A fun little cli app to buy each other :beer: or give each other kudos. Credit to @grandtashworth for the original Bash implementation which inspired this.

## Requirements

- See `requirements.txt`

## Example Usage

- Just a :beer:

```bash
$ ./beer.py dky
Thanks! Buying a beer for: dky
Checking to see if we gave dky any Beer
Yes, he's got some Beer, give him another round!
```

- :beer: with a reason

```bash
$ ./beer.py dky "because he's a troll"
Thanks! Buying a beer for dky for because he's a troll
Checking to see if we gave dky any Beer
Yes, he's got some Beer, give him another round!
```

## Summary of :beer: given

- Summary of :beer:s are stored in [SQLite](https://www.sqlite.org/index.html). Get a summary with:

```bash
$ ./table.py
User      Count
------  -------
dky          24
hana          8
petros        8
grandt        8
joe           4
```
