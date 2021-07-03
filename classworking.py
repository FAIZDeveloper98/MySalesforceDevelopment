import csv

#def csv_reader(fileobj):

#    records=csv.reader(fileobj)

#    for row in records:

#       print(" ".join(row))

def csv_dict_reader(fileobj):
    record=csv.DictReader(fileobj,delimiter=",")
    for row in record:
        print(row['first_name'],row['last_name'])
                                    
if __name__ == '__main__':

    with(open(r'C:\Users\u1089875\Downloads\uk-500.csv','r')) as infile:

        csv_dict_reader(infile)

        
