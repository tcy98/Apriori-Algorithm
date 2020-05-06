import apriori,brute_force

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
        print('Brute Force Time Test for {} lines'.format(num_lines))
        
        t_start = time.perf_counter()
        
        #loop 10 times
        for i in range(loop):
            brute_force.main(filename = filename, num_lines = num_lines)
        
        #end test
        tol_time = time.perf_counter() - t_start
        timeBF.append(tol_time/loop)
        
        
        #similarly..
        print('Apriori Time Test for {} lines'.format(num_lines))
        t_start = time.perf_counter()
        for i in range(loop):
            apriori.main(filename = filename,num_lines = num_lines)
        tol_time = time.perf_counter() - t_start
        timeApr.append(tol_time/loop)
    return timeBF, timeApr
    
def plotTime():
    lines = 20
    timeBF,timeApr = timeTest(lines,'data/increase_items.csv')
    plt.plot(range(1,lines+1),timeBF, label = 'BruteForce')
    plt.plot(range(1,lines+1),timeApr, label = 'Apriori')
    plt.legend(loc = 'best')
    
    plt.title('Incrase Items in Dataset')
    plt.xlabel('Num of Items')
    plt.ylabel('Process Time')
    plt.savefig('items.png')
    plt.show()
    
    lines = 100
    timeBF,timeApr = timeTest(lines,'data/increase_transactions.csv')
    plt.plot(range(1,lines+1),timeBF, label = 'BruteForce')
    plt.plot(range(1,lines+1),timeApr, label = 'Apriori')
    plt.legend(loc = 'best')
    
    plt.title('Incrase Transactions in Dataset')
    plt.xlabel('Num of Transactions')
    plt.ylabel('Process Time')
    plt.savefig('Transaction.png')
    plt.show()
    
        
    

def printResult():
    brute_force.main(SHOW = True)
    apriori.main(SHOW = True)
    

if __name__ == '__main__':
    plotTime()
    printResult()
    
    
    

