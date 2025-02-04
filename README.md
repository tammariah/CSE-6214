# CSE-6214: E-Commerece Platform
## Description
A e-commerce web application with the minimum function of allowing three different types of users to log in and out of the platform and perform their user type based actions. Each type of user (Buyer, Seller, or Admin) has different rights to access certain functionalities. Buyers have the ability to search, compare, buy, and return products from different selllers. Selllers have the ability to add, sell, and recieve payments for the products they have avaliable. Admins are able to approve/block new users accounts and products. Additionally, Admins can over see the actions of different users. 


## Objective
To develop a e-commerce platform within four sprints using agile principles. The platform should contain the features below and additional features requested by the customer at the end of the project.
## Features
### 1. General User Control
#### 1.1 Roles
* Buyer- search, compare, return, and buy products
* Seller- sell, and recieve payments for avaliable products
* Admin- approve/block new user accounts and products, oversee buyer and seller actions
#### 1.2 New Profile
* New users can create a profile
* Set their role
#### 1.3 Authentication
* Login/Logout: username and password
* Email used to setup user name and passeord


### 2. Buyer/Buying Controls
#### 2.1 Search Products
* Products can be searched by:
    * Name
    * Categories
* Products with QTY of 1 or more will appear in search results
* Products can be further filtered by:
     * Additional categories
     * Price
#### 2.2 Compare Products
* Products can be compared by using the "Sort by" tool
      * Lowest to highesest price
      * Highest to lowest price
#### 2.3 Buy Products
* Buyer will need to put the following personal information to buy a product:
    * Name - Person who item will be shipped to
    * Street Address, City, State, Country, and Zipcode
    * Contact Email and Phone number
    * Payment Information
* Only products with QTY 1 or more can be purchased 
#### 2.4 Return Products
* Buyer can request a return by entering the follow information:
     * Buyer name
     * Product name
     * Product QTY
     * Reason
* Buyer can see updates on return process once the request is submitted
* Buyer can ship back the product once the seller approves the refund request
* Buyer will recieve a refund once the seller notifies the system the product was returned


### 3. Seller/Selling Controls
#### 3.1 List Products
* To be eligible for a list each product should have the following criteria:
     * Name
     * Description
     * Price
     * Quanitiy
     * Picture
     * At least one category
* Product information will be stored in a database
#### 3.2 Orders
* Seller will be notified when an item is ordered
* Seller will be notified if an item wants to be returned
#### 3.3 Payment and Refunds 
* Seller will have access to recieving payments
* Seller will have access to refund payments
* Seller will have access to refund requests and can accept the requests
* Payment technology TBD


### 4. Admin Controls
#### 4.1 Oversee Users
* Admins can see when new user accounts are created
* Admins approve or decline new account creation
* Admins can the actions of all buyers and sellers
* Admins can restrict the actions of buyers and sellers
#### 4.2 Oversee Products
* Admins can see when new products are added
* Admins can approve or decline products



## Languages and Techniques
| Development     | Language/Tech.            |
| --------------- | -------------             |
| Front End       | HTML, CSS, and JavaScript |
| Back End        | Django and Python         |
| Database        | PostgreSQL                |
| Version Control | GitHub                    |


## Team Members 
Mariah Tam - mlt605 - tammariah - mariah@rc-flite.com - role
