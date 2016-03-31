
# Class Definitions
class Stock(object) :

    all_stocks = []

    def __init__(self, ticker_symbol, init_price) :
        self.ticker_symbol = ticker_symbol
        self.INIT_PRICE = init_price
        self.price = init_price # per share
        Stock.all_stocks.append(ticker_symbol)

    def update_price(self, new_price) :
        self.price = new_price

    def to_string(self) :
        s = "Ticker Symbol: %s\nInitial Price: $%s\nCurrent Price: $%s" % (
                self.ticker_symbol, self.INIT_PRICE, self.price)
        return s

# end class Stock

# Main Method
def main() :
    
    stocks = []
    stocks.append(Stock("MSFT", 55.05))
    stocks.append(Stock("AAPL", 109.56))
    stocks.append(Stock("KO", 46.59))

    for stock in stocks :
        print stock.to_string()

    print '-' * 10
    print Stock.all_stocks

if __name__ == "__main__" :
    main()