from stock_management.stock_item import Stock_Item 
from stock_management.stock_management import Stock_Management

if __name__ == "__main__" :
    item = Stock_Item("Chocolate" , 200)
    print(item.quantity)

    stock = Stock_Management( )
    stock.add_item( "tesla" ,23)
    stock.add_item ( "car" , 63)
    stock.add_item( "pen" , 75)
    stock.add_item( "table" , 523)

    print(stock.get_stock_status())