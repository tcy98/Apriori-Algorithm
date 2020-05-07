
#generate all possible itemsets then calculate support value
#if n items is given, 2^n itemsets are created
import csv
from itertools import islice
from tabulate import tabulate

def gen_datasets(filename = None,num_lines = 10):
    if filename == None: return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    else:
        with open(filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            
            return data[:num_lines]
        
    

def gen_itemsets(datasets):
    itemlist = [] #contain every item
    for transactions in datasets:
        for item in transactions:
            if item not in itemlist:
                itemlist.append(item)

    itemsets = []  #contain every possible itemset
    
    from itertools import combinations
    for i in range(1,len(itemlist)+1):    
        comb = combinations(itemlist,i)
        itemsets.extend(list(comb))
    
    #print(itemsets)
    return itemsets

#find how many times itemset exist in each transaction
def calculate_support(itemset,datasets):
    counter = 0
    for tran in datasets:    
        result = all(elem in tran for elem in itemset)
        if(result): counter += 1
    return counter/len(datasets)

#return a dictionary with itemset as keys and support as value
def gen_sup_list(itemsets,datasets,minSupport = 0.5):
    itemSupDic = {}
    sup_val = 0
    for itemset in itemsets:
        sup_val = calculate_support(itemset, datasets)
        if sup_val != 0:
            itemSupDic.update({itemset : sup_val})
    #print(itemSupDic)
    d = dict((k,v) for k,v in itemSupDic.items() if v >= minSupport)
    return d
  
#complete procedure to get most frequent association
def brute_force(num_lines = 10, filename = None):
    datasets = gen_datasets(filename,num_lines = num_lines)
    itemsets = gen_itemsets(datasets)
    return gen_sup_list(itemsets, datasets)




def printTable(dic):
    print('Brute Force Result:')
    #sort dic in descending order
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1],reverse = True)}
    headers = ['ItemSet','Support']
    sets = list(dic.items())
    sets = [[list(x[0]),x[1]] for x in sets]
    #print(sets)
    print(tabulate(sets,headers = headers,tablefmt = 'github'))
    print('\n')
    
def main(num_lines = 10, filename = None,SHOW = False):
    L = brute_force(num_lines = num_lines, filename = filename)
    if(SHOW):   printTable(L)
    
