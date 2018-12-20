# Template of RLE file

## First Part (Optional)

---

The first part is composed only by non functional params.
Each line are optional and begining by:

- #C
  - Indicates that a line of comment follows.
    - exemples:
      >`#C Useless comment`

      >`#C Usefull comment`

- #N
  - The name of the pattern.
    - exemple:
      >`#N The Goat`

- #O
  - Says when and by whom the file was created.
    - exemple:
      >`#O jonh.smith@gmail.com 2018/12/06`

---
---
---

## Second Part (Optional)

---

The second part is composed only by functional params.
Each line are optional:

- #P
  - Gives the coordinates of the top-left corner of the pattern.
    - exemple:
      >`#P 10 5`
    - default value:
      >`#P 0 0`

- x = \*, y = \*, rule = B\*/S\* -- don't worry about `rule = B*/S*` for now.
  - Same as #P for `x` and `y`
    - exemple:
      >`x = 10, y = 5`
    - default value:
      >`x = 0, y = 0`
    - note:
      - if `#P` and `x = m, y = n` is defined, only the last line readed is taken.

- #r
  - Gives the rules for the pattern in the form survival_counts/birth_counts.
    - exemple:
      >`#r 23/36`
    - default value:
      >`#r 23/3`

- x = \*, y = \*, rule = B\*/S\* -- worry only about `rule = S*/B*` now.
  - Same as #r for `rule`
    - exemple:
      >`rule = S23/B36`
    - default value:
      >`rule = S23/B3`
    - note:
      - Letter S and B can upper or lower
      - If no letter in rule:
        - left member will be `S` and rigth will be `B`
      - Number can only be between 0 <= 8
      - Number can be once only
    - note:
      - if `#r` and `rule = S*/B*` is defined, only the last line readed is taken.

---
---
---

## Third Part (Required)

---

The third part is the pattern, the only required part.

- Pattern composition:
  - `b` for a dead cell
    - note:
      - You can write `bbbbb` to specify more than one dead cell or `5b`
  - `o` for an alive cell
    - note:
      - You can write `ooo` to specify more than one alive cell or `3o`
  - `$` for the end of line
  - `!` for the end of file
    - note:
      - `!` is optional
- exemple:
  >`3b5o$!`

---
---
---

## Exemple complete

---

```
#C this is a comment
#C this is an other comment
#N This is the name
#O john.smith@gmail.com 2018/12/06

#P 1 2
#r 23/3
x = 2, y = 5, rule = 23/36

5o$bo!
```

# To know the rules

http://www.conwaylife.com/wiki/Run_Length_Encoded

# Author

@Julien TOUZEAU