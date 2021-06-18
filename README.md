# Python CRUD Application
**0.1 initial release**

## To run this application the computer must have installed
1. Python 3
2. Pip 3
3. Python Virtual Environment
4. MySQL server
5. Git

## To run this application

### For all users
- MySQL database must have a database name 'product-crud' and a table name 'products'
- Table 'products' must have these fields
    1. id (int, Primary Key, Not Null, Auto Implement)
    2. product_id (varchar(45), Not Null)
    3. product_name (varchar(45), Not Null)
    4. product_price (float, Not Null)
    5. product_qty (int, Not Null)

### For ubuntu/Linux users
1. Go to terminal and navigate to a file where you want to place this code
2. Run `git clone https://github.com/JanayAlam/product-crud.git`
3. Run `cd ./product-crud`
4. Run `virtualenv venv`
5. Run `source ./venv/bin/activate`
6. Run `pip3 install -r requirements.txt`
7. Run `cp default.env .env`
8. Open the folder in your vs code editor or anything you like and edit the .eve file. Fill the blank option with your database username, password, databse name, host (localhost).
9. Back to terminal. And run `python3 main.py`

### For windows users
1. Go to cmd/powershell/gitbash and navigate to a file where you want to place this code
2. Run `git clone https://github.com/JanayAlam/product-crud.git`
3. Run `cd .\product-crud`
4. Run `virtualenv venv`
5. Run `\path\to\env\Scripts\activate.bat`
6. Run `pip install -r requirements.txt`
7. Run `cp default.env .env`
8. Open the folder in your vs code editor or anything you like and edit the .eve file. Fill the blank option with your database username, password, databse name, host (localhost).
9. Back to terminal. And run `python main.py`