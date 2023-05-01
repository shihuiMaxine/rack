Rack recommends 10 relevant APIs for each query based on KKC,  KPAC and KAC. KAC refers to the fact that some keywords may appear together with a specific API or may be associated with multiple API in various programming solutions, indicating that there is a potential semantic connection between keywords and API. KKC identifies that candidate API should not only be related to multiple keywords, but also should be mutually consistent pairs, and then based on these pairs, candidate API related to these functional pairs is collected. KPAC computes a co-occurrence score for each keyword pair. Each keyword pair is if two keywords occur frequently in the API in the code snippet. The API is likely to be relevant for queries containing these two keywords.
We extracted the main information including post ID, question title and answer from the Python posts on Stack Overflow and made the database.We used SQL query to find all the Python posts with code answers in the stack exchange, and then downloaded all the data and saved them into a CSV file. Since the number of files is too large, we first use the data of one hundred lines to analyze and work. In datacsv.python file We used standard natural language processing steps to extract the code part of the whole answer. Then we use Beautiful Soup  to extract the title of the question, the answers, the code content contained in those answers and the "pre" content in those codes from these 100 lines of Python posts. In  reg2.py we extracted the function and method name from the code part of answer After we successfully analyzed the 100 lines data, we analyzed all the data. We extracted the API from the function name and method name of the answer's code part and combine with title token. In TokenMapSaver.py we insert all the mathod and function name in codetoken and  insert all the title token to Text token. When  we want to  see the content of data, we can run outputdata python  file.
Examples:
ex1:
CodeTokenProvider.py:
query = "How do you parse HTML?"
output:
all: ['pars', 'html']
0.5045429590543117
rankedAPIs:  ['BeautifulSoup', 'get', 'find', 'find_all', 'strip', 'requests', 'append', 'open', 'select', 're', 'read', 'parse']
BeautifulSoup 1.0 1.0 1.0 0.5175
get 0.8333333333333333 0.9 1.0 0.45999999999999996
find 0.5 0.8 1.0 0.40249999999999997
find_all 0.38888888888888884 0.7 0 0.345
strip 0.16666666666666669 0.6 0 0.2875
requests 0.2777777777777778 0.5 0 0.22999999999999998
append 0.6111111111111112 0.4 1.0 0.17250000000000001
open 0.888888888888889 0.30000000000000004 1.0 0.11499999999999996
select 0 0.19999999999999996 0 0.05749999999999998
re 0.2777777777777778 0 1.0 0.016666666666666663
ex2:
CodeTokenProvider.py:
query = "How to send email?"
output:
all: ['send', 'email']
0.5240003996421584
rankedAPIs:  ['MIMEText', 'sendmail', 'SMTP', 'MIMEMultipart', 'login', 'smtplib', 'as_string', 'open', 'attach', 'read', 'get', 'EmailMessage', 'socket']
MIMEText 0.588235294117647 1.0 0 0.5175
sendmail 0.47058823529411764 0.9 0 0.45999999999999996
SMTP 0.2941176470588235 0.8 0 0.40249999999999997
MIMEMultipart 0.3529411764705882 0.7 0 0.345
login 0.23529411764705882 0.6 0 0.2875
smtplib 0 0.5 0 0.22999999999999998
as_string 0.058823529411764684 0.4 0 0.17250000000000001
open 1.0 0.30000000000000004 1.0 0.11499999999999996
attach 0 0.19999999999999996 0 0.05749999999999998
read 0.5294117647058822 0 1.0 0.03333333333333334
ex3:
CodeTokenProvider.py:
query = "How to create database?"
output:
all: ['creat', 'databas']
0.42394365287097385
rankedAPIs:  ['execute', 'connect', 'cursor', 'create_engine', 'commit', 'close', 'format', 'sqlite3', 'create_all', 'get', 'open']
execute 1.0 1.0 0 0.5175
connect 0.9 0.9 0 0.45999999999999996
cursor 0.8 0.8 0 0.40249999999999997
create_engine 0 0.7 0 0.345
commit 0.7 0.6 0 0.2875
close 0.19999999999999996 0.5 0 0.22999999999999998
format 0 0.4 0 0.17250000000000001
sqlite3 0 0.30000000000000004 0 0.11499999999999996
create_all 0 0.19999999999999996 0 0.05749999999999998
get 0.6 0.09999999999999998 0 0.0# rack