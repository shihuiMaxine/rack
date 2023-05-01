from core. CodeTokenProvider import CodeTokenProvider
text1 = input ('input: ')
with open(text1, 'r') as file:
    for line in file:
        print(type(line))
        query = line

        provider = CodeTokenProvider(query)


        results = provider.recommendRelevantAPIs("all")
        print(results)