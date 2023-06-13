from stock_manager.stock_item import Stock_Item

class Stock_Management ( ) :

    def __init__ ( self) -> None : 

        self.stock = {}

    def add_item ( self , name:str , quantity:int) -> None :

        if name not in self.stock.keys() :
            item = Stock_Item( name = name , quantity = quantity )
            self.stock[name] = item
        else : 
            self.update_item_quantity(name = name , quantity = quantity )

    def remove_item ( self , name : str) -> None : 

        if name in self.stock.keys(): 
            del self.stock[name]

    def check_item ( self , name : str) -> bool :

        item = self.stock.get(name)

        if item :
            return True
        return False

    def get_item_quantity ( self , name : str , ) -> None :

        if name in self.stock.keys(): 
            return self.stock[name].quantity
        else :
            self.add_item( name = name , quantity = 0)
            return 0

    def update_item_quantity( self , name : str , quantity : int) -> None :

        if name in self.stock.keys() :
            if quantity > 0 :
                self.stock[name].augment_quantity(quantity = quantity)
            else : 
                self.stock[name].reduce_quantity(quantity = quantity)
        else : 
            self.add_item(name = name , quantity = quantity )
