# CSE-6214: E-Commerece Platform
## Description
A e-commerce web application with the minimum function of allowing three different types of users to log in and out of the platform and perform their user type based actions. Each type of user (Buyer, Seller, or Admin) has different rights to access certain functionalities. Buyers have the ability to search, compare, buy, and return products from different selllers. Selllers have the ability to add, sell, and recieve payments for the products they have avaliable. Admins are able to approve/block new users accounts and products. Additionally, Admins can over see the actions of different users. 


## Objective
To develop a e-commerce platform within four sprints using agile principles. The platform should contain the features below and additional features requested by the customer (TA) nearing the end of the project.
## Features
### 1. General User Control
>#### 1.0 Roles
>> * Buyer- search, compare, return, and buy products
>> * Seller- sell, and recieve payments for avaliable products
>> * Admin- approve/block new user accounts and products, oversee buyer and seller actions
>#### 1.1 New Profile
>> * New users can create a profile with their email
>> * Set their role
>#### 1.2 Authentication
>> * Login/Logout: username and password



### 2. Buyer/Buying Controls
> #### 2.0 Search Products
>> * Products can be searched by:
>>    * Name
>>    * Categories
>> * Products with QTY of 1 or more will appear in search results
>> * Products can be further filtered by:
>>     * Additional categories
>>     * Price
> #### 2.1 Compare Products
>> * Products can be compared by using the "Sort by" tool:
>>     * Lowest to highesest price
>>     * Highest to lowest price
> #### 2.2 Buy Products
>> * Buyer will need to put the following personal information to buy a product:
>>     * Name - Person who item will be shipped to
>>     * Street Address, City, State, Country, and Zipcode
>>     * Contact Email and Phone number
>>     * Payment Information
>> * Only products with QTY 1 or more can be purchased 
> #### 2.3 Return Products
>> * Buyer can request a return by entering the follow information:
>>     * Buyer name
>>     * Product name
>>     * Product QTY
>>     * Reason
>> * Buyer can see updates on return process once the request is submitted
>> * Buyer can ship back the product once the seller approves the refund request
>> * Buyer will recieve a refund once the seller notifies the system the product was returned


### 3. Seller/Selling Controls
> #### 3.0 List Products
>> * To be eligible for a list each product should have the following criteria:
>>     * Name
>>     * Description
>>     * Price
>>     * Quanitiy
>>     * Picture
>>     * At least one category
>> * Product information will be stored in a database
> #### 3.1 Orders and Returns
>> * Seller will be notified when an item is ordered
>> * Seller will be notified if the buyer requests a return
> #### 3.2 Payment and Refunds
>> * Seller will have access to refund requests and can accept the requests
>> * Seller will have access to recieving payments
>> * Seller will have access to refund payments
>> * Payment technology TBD


### 4. Admin Controls
> #### 4.0 Oversee Users
>> * Admins can see when new user accounts are created
>> * Admins approve or decline new account creation
>> * Admins can see the actions of all buyers and sellers
>> * Admins can restrict the actions of buyers and sellers
> #### 4.1 Oversee Products
>> * Admins can see when new products are added
>> * Admins can approve or decline products



## Languages and Techniques
| Development     | Language/Tech.            |
| --------------- | -------------             |
| Front End       | HTML and CSS              |
| Back End        | Django and Python         |
| Database        | PostgreSQL or SQLite (TBD)|
| Version Control | GitHub                    |


## Team Members 
Mariah Tam - mlt605 - tammariah - mariah@rc-flite.com - Full-stack Developer
