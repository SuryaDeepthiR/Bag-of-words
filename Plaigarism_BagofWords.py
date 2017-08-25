import math
import os.path

class Bag_of_words:

    def file(filename):
        ''' open and read a file and join the next lines of it'''
        f = open(filename,'r')
        s = ' '.join([line.rstrip('\n') for line in f])
        return s

    def remove_delimiters(delimiters,y):
        '''prints lowercase and removes delimiters'''
        new_y = y.lower()
        for i in delimiters:
            new_y = new_y.replace(i,' ')
            data = ' '.join(new_y.split())
        return data

    def frequency(f):
        '''finds frequency of each word and stores it in a list(frequency vector)'''
        words = f.split(" ")
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
            return d

    def euclidean(lst):
        '''gives euclidean norm of frequency vector'''
        res=0
        for e in lst:
            res=res+(lst[e]**2)
        return math.sqrt(res)

    def dot_product(s,t):
        '''Calculates the dot product of two frequency vectors of similar words'''
        sum = 0
        for i in s:
            product = 0
            for j in t:
                if i == j:
                    product = s[i]*t[j]
                    sum = sum+product
        return sum

    def cos_func(c,s1,s2):
        cf = c/(s1*s2)
        return cf


    def main(filename1,filename2):
        delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "...",'"',"=","+","<",">","(",")","{","}","[","]"]
        d1 = {}
        d2 = {}
        f1 = Bag_of_words.file(filename1)
        f2 = Bag_of_words.file(filename2)
        f_data1 = Bag_of_words.remove_delimiters(delimiters,f1).split()
        f_data2 = Bag_of_words.remove_delimiters(delimiters,f2).split()
        for i in f_data1:
            d1[i]=f_data1.count(i)
        for j in f_data2:
            d2[j]=f_data2.count(j)
        e1= Bag_of_words.euclidean(d1)
        #print("Euclidean Norm 1 :" + str(e1))
        e2= Bag_of_words.euclidean(d2)
        #print("Euclidean Norm 2 :" + str(e2))
        dp = Bag_of_words.dot_product(d1,d2)
        #print("Dot product :" + str(dp))
        cf = Bag_of_words.cos_func(dp,e1,e2)
        #print(cf*100)
        return cf*100

Plaigarism = Bag_of_words()

path = input("Enter the path of directory")
file_list = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        file_list.append(file)
print(file_list)
result = []
result2 = []
for i in range(len(file_list)):
    result = []
    result.append(file_list[i])
    for j in range(len(file_list)):
        if i == j:
            result.append(None)
        else:
            result.append(Bag_of_words.main(file_list[i],file_list[j]))
    result2.append(result)
    #print(result)

for x in result2:
    for y in x:
        print(y ,"          ",end = '')
    print("")







