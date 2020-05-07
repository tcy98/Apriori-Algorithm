# pa04-Spring2020
 Python implementation of Association Rule Mining: a trivial (brute force) solution and Apriori Algorithm to find frequent itemsets 

## Association Rule Mining
• developed to analyze market basket data 

• identified groups of market items that customers tended to buy in association with each other 

• People who buy soap and shampoo have an increased probability of buying hairspray 

## Code
[brute_force.py](brute_force.py): a brute_force implementation 

[apriori.py](apriori.py): use Apriori algorithm


## Test:
[test.py](test.py): compare and analyze performances of two solutions 

Measure time for both solutions with data that has increase numbers of items/numbers of transactions.

Taking the average of 10 times to reduce error

## Results

 ![With increase items in datasets](Transaction.png) 

 ![With incrase transactions in datasets](items.png)
