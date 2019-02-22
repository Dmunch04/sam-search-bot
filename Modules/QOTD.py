class Quote (self, quote, number):
    self.quote = quote
    self.number = number

def getQuote ():
    quotes = []

    data = open('Data/QOTDs.txt', 'r')
    content = data.readlines()
    data.close()

    num = open('Data/QOTDnum.txt', 'r')
    number = num.read()
    num.close()

    for line in content:
        quotes.append(line)

    result = Quote(quotes[0], number)

    return result
