class Stock_Item ( ): 
    """
        DESCRIPTION :  
        ------------
            A class representing a unique item in stock. Every item is represent by its name and quantity

        USAGE : 
        -------
            >>> from stock_manager import StockItem
            >>> item = StockItem ( name = "wood" , quantity = 10)
    """
    def __init__ (self , name : str , quantity : int) -> None :
        """
            DESCRIPTION :  
            ------------
                instantiation of a nex item

            PARAMETERS :
            -----------
                - name : str
                    the name of the new item
                - quantity : int
                    the quantity of the new item
        """
        self.name = name
        self.quantity = quantity

    def augment_quantity ( self , quantity : int) -> None :
        """
            DESCRIPTION :  
            ------------
                add somme quantity of the item

            PARAMETERS :
            -----------
                - quantity : int
                    the quantity of item to add from the one available
        """
        self.quantity += abs(quantity)

    def reduce_quantity ( self , quantity : int) -> None :
        """
            DESCRIPTION :  
            ------------
                remove somme quntity of the item

            PARAMETERS :
            -----------
                - quantity : int
                    the quantity of item to remove from the one available
        """

        if self.quantity >= abs(quantity) : 
            self.quantity -= abs(quantity)
        else : 
            raise ValueError( f"you want to remove {quantity} {self.name} but you can't remove more than {self.quantity} {self.name}" )

    def __quantity_status__ ( self ) -> bool :

        return self.quantity > 0 
