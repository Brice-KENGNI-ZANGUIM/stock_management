# conversion-units
This package is build for **stock managment.**
It provide a collection of methods and class to mimic approch the problem of stock management.
For exemple dealing with different type of items and stocks.

## 1. Installation

Run the following code in a terminal to install the **stock management** package in you python environnement

```bash
$ pip install stock-management
```

## 2. Availables objects

in this package version, you have the ability to generate class of : 
<ul>
    <li> <strong> Items : </strong> it can be for exemple cars, dors, apple, tomatos, bred, shoes, pen, book . . .etc   </li>
    <li> <strong>Stocks</strong>   </li>
</ul>

## 3. Import

Here is how you can simply create an instance of item or stock after installing the package
```python

from stock_management.stock_item import Stock_Item
from stock_management.stock_management import Stock_Management

```

## 4. Usage

<u> **a- MANAGE ITEMS** </u> 

To create an instance of item you will need to provide two values: the **name** and the **quantity** of the item.
Here is an exemple of how to create an item name **chocolate** with **120** units of the item

```python
from stock_management.stock_item import Stock_Item
chocolate = Stock_Item( name = "chocolate" , quantity = 120)

```
You can make some basic operations like **adding 20 units** of chocolates

```python
chocolate.augment_quantity(quantity = 20)

```
<u> **b- MANAGE STOCKS** </u> 

To deal will stock you first have to create an instance of a stock by like this for exemple

```python
from stock_management.stock_management import Stock_Management

stock = Stock_Management( )

```
After this, you can make many operations like adding some item in you stock.
Here for exemple in my stock i add **15** units of **orange** and **46** units of **cars**

```python

stock.add_item( name = "orange", quantity = 15)
stock.add_item( name = "car" , quantity = 46)
. . .

```

## 5. Author

<ul>
    <li> Full Name : <strong> Brice KENGNI ZANGUIM </strong>  </li>
    <li> Email : <strong> kenzabri2@yahoo.com </strong>   </li>
</ul>

## 6. Contributors


