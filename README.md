## This application with REST API is allow to:
   - create a Product with properties "Name" and "Amount in stock"
       - if product with given name already exists then the "Amount in stock" 
         increased
   - list all Products in store
   - order a product  
____

## How  to test application works:
1. Clone repository: `git clone git@github.com:nataliia-pysanka/DeepSee.git`
2. Change dir: `cd rest_api`
3. Install virtual enviroment: `python -m venv venv`
4. Activate virtual env: `source venv/bin/activate`
5. Update: `pip python -m pip install --upgrade pip`
6. Install dependencies for the project in the virtual environment python:
   `-m pip install --no-cache-dir -r requirements.txt`
7. Make migrations for creating DB:
   `python manage.py makemigrations && python manage.py migrate`
8. Launch local server: `python manage.py runserver`
____
http://localhost:8000/ - main page with product list

http://localhost:8000/api/products/ - API for GET request

http://localhost:8000/api/create/ - API for POST request

http://localhost:8000/api/store/ - API for PUT request

You can put JSON in field and make POST or PUT request. 
Also you can use  curl command in terminal:
* for list all products in store (./list.sh):
```curl "http://localhost:8000/api/products/"```
* for create (or update) some products (./create.sh):
```curl -d "@products.json" -H "Content-Type: application/json" -X POST http://localhost:8000/api/create/```
* for order one(!) product (./order.sh):
```curl -d '{"name":"Brown eggs","amount_in_stock":8}' -H "Content-Type: application/json" -X PUT http://localhost:8000/api/store/```