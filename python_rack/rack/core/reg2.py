import re
import csv
file = open("4192.csv")

print(type(file))
csvreader = csv.reader(file)
list1=[]
count1=0
cont=""
header = ["ID", 'title','code', 'method name', 'function name',"title_token"]


with open('data_mapping2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    for row in csvreader:
        content1=row[2]
        list1=[]
        string1=""
        if count1 !=0:

            cont = content1
            code = cont

            # Define the regex pattern to extract method names
            pattern = r"\w+\("

            method_names = re.findall(pattern, code)

            # Print the extracted method names

            for name in method_names:
                if name[0:-1] not in list1:
                    if name[0:-1] != "print":
                        list1.append(name[0:-1])
                        string1+=name[0:-1]
                        string1+=" "

            code = cont
            print(list1)
            pattern2 = r"import\s+(\w+)"
            method_names2 = re.findall(pattern2, code)
            list2 = []
            string2=""
            for name2 in method_names2:
                if name2 not in list2:
                    list2.append(name2)
                    string2+=name2
                    string2+=" "

            print(list2)
            data1 = [row[5],row[0], row[2],list1, list2,row[6]]
            print(data1)
            writer.writerow(data1)

        count1+=1


