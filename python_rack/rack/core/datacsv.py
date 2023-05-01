from config import StaticData
import requests, csv
from bs4 import BeautifulSoup as bs
from similarity.MyTokenizer import MyTokenizer
from core. CodeTokenProvider import CodeTokenProvider

file = open("Query.csv")

print(type(file))
csvreader = csv.reader(file)

rows = []
titlelist=[]
answerlist=[]
data=[]

header = ['title','answer', 'code', 'pre',"api","ID","Title_Token"]


with open('4192-2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    i=0
    for row in csvreader:
        # print(row)
        if i !=0:
            soup = bs(row[4], "html.parser")
            pre1 = soup.find_all('pre')
            code1 = soup.find_all('code')
            api1= soup.findAll('code')
            query = row[3]
            provider = CodeTokenProvider(query)
            title_token = provider.decomposeQueryTerms()

            api1 = [api2.text for api2 in api1]
            # for j in code1:
            myTokenizer = MyTokenizer("gs -q -dQUIET -dPARANOIDSAFER -dBATCH -dNOPAUSE -dNOPROMPT \
-dMaxBitmap=500000000 -dLastPage=1 -dAlignToPixels=0 -dGridFitTT=0 \
-sDEVICE=jpeg -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -r72x72 \
-sOutputFile=$OUTPUT -f$INPUT")

            data1 = [row[3], row[4], code1, pre1,api1,row[0],title_token]
            # print(data1)
            writer.writerow(data1)
        i+=1
