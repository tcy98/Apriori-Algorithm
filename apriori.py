import csv

def gen_datasets(filename=None, num_lines=10):
    if filename == None:
        return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
    else:
        with open(filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))

            return data[:num_lines]


# Ck contains Candidate itemsets with length k
# Thus C1 contains all single item
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                # append if item not in C1
                C1.append([item])
    # sort C1 in ascending order
    C1.sort()
    return list(map(frozenset, C1))


# Calculate support of candidate sets and return if minSupport is reached for candidate item
def scanD(D, Ck, minSupport):
    ssCnt = {}  # store frequency each item appears
    for tid in D:
        for can in Ck:
            # s.issubset(t)  test if it has all
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = len(D)  # total number of dataset
    retList = []  #all item which reach minSupport
    supportData = {} # key : support value
    for key in ssCnt:
        # support = key frequency / total number of dataset
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData

# take a list of frequent itemsets Lk and the size of the itemsets k
# produce Ck, candidate itemsets with length k
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[: k - 2]
            L2 = list(Lk[j])[: k - 2]
            # print '-----i=', i, k-2, Lk, Lk[i], list(Lk[i])[: k-2]
            # print '-----j=', j, k-2, Lk, Lk[j], list(Lk[j])[: k-2]
            L1.sort()
            L2.sort()
            # if first k-2 elements are equal (no duplicates)
            if L1 == L2:
                # set union
                # print 'union=', Lk[i] | Lk[j], Lk[i], Lk[j]
                retList.append(Lk[i] | Lk[j])
    return retList

#set default minSupport to 0.5: occur in at least 50% of all transactions
def apriori(dataSet, minSupport=0.5):

    C1 = createC1(dataSet)
    # print 'C1: ', C1

    D = list(map(set, dataSet))
    # print 'D=', D
    # calculate support and return list of item with support higher than minSupport
    L1, supportData = scanD(D, C1, minSupport)
    # print "L1=", L1, "\n", "outcome: ", supportData

    L = [L1] #L contains the list of frequent itemsets that met a minimun support of 0.5
    k = 2

    while (len(L[k-2]) > 0):
        # print 'k=', k, L, L[k-2]
        Ck = aprioriGen(L[k-2], k) #generate condidate list
        # print 'Ck', Ck

        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        if len(Lk) == 0:
            break

        L.append(Lk)
        k += 1
        # print 'k=', k, len(L[k-2])
    return L, supportData

from tabulate import tabulate

def printTable(dic,minSupport = 0.5):
    print('Apriori Result:')
    #sort dic in descending order
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1],reverse = True)}
    headers = ['ItemSet','Support']
    sets = list(dic.items())
    sets = [[list(x[0]),x[1]] for x in sets if x[1] >= minSupport]
    #print(sets)
    print(tabulate(sets,headers = headers,tablefmt = 'github'))
    

def main(filename = None,SHOW = False,num_lines = 10):
    datasets = gen_datasets(filename,num_lines = num_lines)
    L,sd = apriori(datasets)
    if(SHOW):   printTable(sd)


