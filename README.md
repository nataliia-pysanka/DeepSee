The requirements of the app are:

0. OOP and Python
1. Application with REST API that allows to
   - create a Product with properties "Name" and "Amount in stock"
       - if product with given name already exists then the "Amount in stock" 
       should be increased
   - list all Products in store
   - order a product  

2. To create the product and to order a product I should send a request with 
JSON object

3. The application should keep the state after restart. So it requires some 
kind of data storage. It does not matter if it will be a database ( sqlite, 
postgres, ...) or a file, but we would prefer a database

4. Please write me an instruction how I can check/test if the application works