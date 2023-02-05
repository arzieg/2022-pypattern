from dataclasses import dataclass

@dataclass
class StockInHand:
    apples: int = 40
    orange: int = 50
    mangoes: int = 60

    def total_stock(self) -> int:
        return self.mangoes + self.apples + self.orange

def main() -> None:
    stock = StockInHand ()
    stock.apples = 100
    print (stock.total_stock())

if __name__ == '__main__':
    main()