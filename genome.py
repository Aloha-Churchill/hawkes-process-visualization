import matplotlib.pyplot as plt
import numpy as np


file = open('covidgenome.txt')
genome = file.read().replace('\n', '')
file.close()

def frequencyPerLength(length, nucleotides):
    start = 0
    end = start+length
    frequency = []
    count = 0
    while end < len(genome):
        for i in range(start, end):
            if genome[i:i+len(nucleotides)] == nucleotides:
                count += 1
        start = end
        end = end+length
        frequency.append(count)
        count = 0
    
    plt.hist(frequency, bins = 100)
    plt.xlabel('Number of ' + nucleotides + ' per 100 Bases in Sequence')
    plt.ylabel('Frequency')
    plt.show()

def pointProcessCount(nucleotides):
    tracker = []
    for i in range(len(genome)-len(nucleotides)):
        if genome[i:i+len(nucleotides)] == nucleotides:
            tracker.append(i)
    
    plt.scatter(tracker, np.zeros_like(tracker))
    plt.yticks([])
    plt.show()

def getFrequency(nucleotides):
    count = 0
    for n in genome:
        if n == nucleotide:
            count += 1
    return count

def main():

    #sequence = 'ACT'
    sequence = 'A'
    frequencyPerLength(100, sequence)

    #ATG
    #sequence = 'ATGGAC'
    #pointProcessCount(sequence)

    



main()