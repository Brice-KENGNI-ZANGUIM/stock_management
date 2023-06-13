from stock_management.stock_item import StockItem

import stock_manager

if __name__ == "__main__" :
    item = StockItem("Chocolate" , 200)
    item.reduce_quantity(120)
    item.reduce_quantity(100)
    print(item.quantity)

    dic = { "a" : 1 , "b" : 2 , "c" : 3}
    del dic["a"]

    print(dic)