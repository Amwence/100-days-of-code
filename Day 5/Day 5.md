# Day 5 Loops

## For Loop

''for'' loops iterate over lists,tuples, sets, dictionaries, strings and ``range()``; until either something happens to make them stop(``break``), or they get to the end of their list/range. <br>

Example:
```
for item in list_of_items:
    #Do something to each item
```

The range function is used as a way to do things within a certain range. Suprising I know. it is used range(start, stop but not included,index jump/step). So range(0,10,2) would print 0, 2, 4, 6, 8, because 10 is not included, and it goes up by 2. 