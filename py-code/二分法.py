#coding:utf-8

def binary_search(data_source,find_num):

    mid = int(len(data_source)/2)
    if len(data_source) >= 1:
        if data_source[mid] > find_num:
            print "data in left of [%s]"%data_source[mid]
            binary_search(data_source[:mid],find_num)
        elif data_source[mid] < find_num:
            print "data in right of [%s]"%data_source[mid]
            binary_search(data_source[mid:],find_num)
        else:
            print "The find_num is %s"%find_num

    else:
        print "cannot find .....",data_source[mid]

if __name__ == '__main__':
    data = list(range(1,6000000))

    binary_search(data,56789)
