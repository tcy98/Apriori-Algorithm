import apriori,brute_force
from tabulate import tabulate
#global varible
minSupport = 0.3
loop = 10

import matplotlib.pyplot as plt
import time
def timeTest(lines,filename):
    timeBF = []
    timeApr = []

    # number of lines to read in data
    for num_lines in range(1,lines+1,1):
        #measure brute force method
        #('Brute Force Time Test for {} lines'.format(num_lines))
        
        t_start = time.perf_counter()
        
        #loop 10 times
        for i in range(loop):
            brute_force.main(filename = filename, num_lines = num_lines)
        
        #end test
        tol_time = time.perf_counter() - t_start
        timeBF.append(tol_time/loop)
        
        
        #similarly..
        #print('Apriori Time Test for {} lines'.format(num_lines))
        t_start = time.perf_counter()
        for i in range(loop):
            apriori.main(filename = filename,num_lines = num_lines)
        tol_time = time.perf_counter() - t_start
        timeApr.append(tol_time/loop)
    return timeBF, timeApr
    
def plotTime():
    print('\n\n-----------Time Test Result-----------\n\n')
    #plots
    lines = 20
    timeBF,timeApr = timeTest(lines,'data/increase_items.csv')
    plt.plot(range(1,lines+1),timeBF, label = 'BruteForce')
    plt.plot(range(1,lines+1),timeApr, label = 'Apriori')
    plt.legend(loc = 'best')
        
    plt.title('Increase Items in Dataset')
    plt.xlabel('Num of Items')
    plt.ylabel('Process Time')
    plt.savefig('items.png')
    plt.show()
    tabledata = [[]]
    #tabledata[:,0] = range(1,lines+1)
    #tabledata[:,1] = timeBF
    
    for i in range(1,lines+1):
        rowdata = []
        rowdata.append(i)
        rowdata.append(timeBF[i-1])
        rowdata.append(timeApr[i-1])
        tabledata.append(rowdata)
    
    headers = ['num of items','timeBF','timeApr']  
    print(tabulate(tabledata,headers = headers,tablefmt = 'github'))
    
    
    
    #testing transactions
    lines = 100
    timeBF,timeApr = timeTest(lines,'data/increase_transactions.csv')
    plt.plot(range(4,lines+1),timeBF[3:], label = 'BruteForce')
    plt.plot(range(4,lines+1),timeApr[3:], label = 'Apriori')
    plt.legend(loc = 'best')
    
    plt.title('Increase Transactions in Dataset')
    plt.xlabel('Num of Transactions')
    plt.ylabel('Process Time')
    plt.savefig('Transaction.png')
    plt.show()
    
    tabledata = [[]]
    for i in range(1,lines+1):
        rowdata = []
        rowdata.append(i)
        rowdata.append(timeBF[i-1])
        rowdata.append(timeApr[i-1])
        tabledata.append(rowdata)
    
    headers = ['num of transactions','timeBF','timeApr']  
    print(tabulate(tabledata,headers = headers,tablefmt = 'github'))
    

def printResult():
    brute_force.main(SHOW = True)
    apriori.main(SHOW = True)
    

if __name__ == '__main__':
    printResult()
    plotTime()
    
    
    
    

