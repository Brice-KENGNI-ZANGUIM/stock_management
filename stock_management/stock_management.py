from stock_management.stock_item import Stock_Item

class Stock_Management ( ) :
    """
        DESCRIPTION : 
        ------------
            Provide tools to manage the component of a stock

        USAGES :
        -------
            >>> from stock_management.stock_management import Stock_Management
            >>> stock = Stock_Management()
    """
    def __init__ ( self) -> None : 
        """
            DESCRIPTION :  
            ------------
                Initialise the stock object by providing an empty dictionnary
        """
        self.stock = {}
        self.__status__ = {}

    def add_item ( self , name:str , quantity:int) -> None :
        """
            DESCRIPTION :  
            ------------
                Add an item in the stock

            PARAMETERS :
            -----------
                - name : str
                    the name of the item to add in stock
                - quantity : int
                    the quantity of the  item to add in stock

            USAGE : 
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item( name = "shoes" , quantity = 123)
        """
        # if the item to add doesn't exist already  we just add it in the stock
        if name not in self.stock.keys() :
            item = Stock_Item( name = name , quantity = quantity )
            self.stock[name] = item
        # if it already exist, then we update the quantity related
        else : 
            self.update_item_quantity(name = name , quantity = quantity )

        # update stock status
        self.__status__[name] = quantity

    def remove_item ( self , name : str) -> None : 
        """
            DESCRIPTION :  
            ------------
                Remove an existing item in the stock

            PARAMETERS :
            -----------
                - name : str
                    the name of the  item to remove from stock

            USAGE : 
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.remove_item( name = "shoes" )
        """
        if name in self.stock.keys(): 
            del self.stock[name]

    def check_item ( self , name : str) -> bool :
        """
            DESCRIPTION :  
            ------------
                check for the existence of an item in stocks

            PARAMETERS :
            -----------
                - name : str
                    the name of the item to check

            USAGE : 
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item(name = "shoes" , quantity = 63 )
                >>> stock.check_item( name = "shoes")
        """
        item = self.stock.get(name)

        if item :
            return True
        return False

    def get_item_quantity ( self , name : str , ) -> int :
        """
            DESCRIPTION :  
            ------------
                look for the quantity of the item in stock

            PARAMETERS :
            -----------
                - name : str
                    the name of the item 

            USAGE : 
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item(name = "chocolate" , quantity = 45 )
                >>> stock.get_item_quantity( name = "chocolate")
        """
        if name in self.stock.keys(): 
            return self.stock[name].quantity
        else :
            self.add_item( name = name , quantity = 0)
            return 0

    def augment_stock_item_quantity( self , name : str , quantity : int) -> None :
        """
            DESCRIPTION :
            ------------
                augment the quantity of an item in stock

            PARAMETERS :
            -----------
                - name : str
                    the name of the item to check
                - quantity : int
                    the quantity of item to augment in the stock

            USAGE :
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item( name = "shoes" , quantity = 40 )
                >>> stock.augment_stock_item_quantity( name = "Tesla" , quantity = 10 )
        """
        if name in self.stock.keys() :
            self.stock[name].augment_quantity(quantity = quantity)
        else : 
            self.add_item(name = name , quantity = quantity )

    def reduce_stock_item_quantity( self , name : str , quantity : int) -> None :
        """
            DESCRIPTION :
            ------------
                augment the quantity of an item in stock

            PARAMETERS :
            -----------
                - name : str
                    the name of the item to check
                - quantity : int
                    the quantity of item to remove in the stock

            USAGE :
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item( name = "Tesla" , quantity = 200 )
                >>> stock.reduce_stock_item_quantity( name = "Tesla" , quantity = 2)
        """
        if name in self.stock.keys() :
                self.stock[name].reduce_quantity(quantity = -quantity)
        else : 
            raise KeyError( f"The item {name} is actually not present in stock")
        
    def get_stock_status ( self ) -> dict :
        """
            DESCRIPTION :
            ------------
                return the state of the stock, precisely it return all the items and quantity in stock

            PARAMETERS :
            -----------
                None

            USAGE :
            ------
                >>> from stock_management.stock_management import Stock_Management
                >>> stock = Stock_Management()
                >>> stock.add_item( name = "shoes" , quantity = 200 )
                >>> stock.add_item( name = "pencil" , quantity = 23 )
                >>> stock.add_item( name = "spoon" , quantity = 63 )
                >>> stock.add_item( name = "tomato" , quantity = 150 )
                >>> stock.get_stock_status( )
        """

        return { val.name : val.quantity  for val in self.stock.values() }
