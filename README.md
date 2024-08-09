# HardWear

This is my e-commerce site which sells clothes and homeware, such as bed and bath items and kitchen silverware. The name of this site is a play of word with the hardware, but spelt hardwear. Django is what I mainly use to build this site along with a Python back-end development to handle the code that is used to make the site work properly. To make colorful site without having a lot of code in the CSS file, I used the Bootstrap front-end (CSS) framework, along as font awesome to make icons for the checkout and login pages. To be able to allow a credit/debit card transaction via the checkout, Stripe will be connectted to the site with webhooks. 
![Responsive website image](static/screenshots/amiresponsive.png)
Visit the live site - [HardWare](https://hardwear-1e19c988931d.herokuapp.com/)

---

---

## **Design**

  - This site will have two main colors, grey and white, with the display banner being yellow. 
  - The navigation and footage sections will be white while the center would be either grey execept for the index page as it have image of smiling woman in front of a yellow wall to match the display banner. 
  - The two main google fonts that I used for this site are Overlock and Nunito as I researched and find out that both fonts work together for a store that sells clothing, which this site partly does. 

<details>
<summary>Google Fonts:</summary>

![Google Fonts](static/screenshots/google-fonts.png)
</details>
<br>

- __Wireframe__

  -  This is the home page of the site.
<br>

  <details>
  <summary>Home Page:</summary>

  ![Home Page](static/screenshots/home-page.png)
  </details>

  -  This page will contain all the products on the site.

  <details>
  <summary>Products Page:</summary>

  ![Products Page](static/screenshots/product-page.png)
  </details> 
  
  - This page will have information each product where the user can select a size (if available) and the quanity before adding to bag on the top right of the page.

  <details>
  <summary>Product Info Page:</summary>

  ![Product Info Page](static/screenshots/product-info-page.png)
  </details> 

  - This page will contain the item the user has put in their bag and ready to purchase.

  <details>
  <summary>Bag Page:</summary>

  ![Bag Page](static/screenshots/bag-page.png)
  </details> 

  - This page is where the user can checkout their items by filing in the form and enter their payment detail.

  <details>
  <summary>Checkout Page:</summary>

  ![Checkout Page](static/screenshots/product-checkout-page.png)
  </details> 

  - This is where the user can sign in. 

  <details>
  <summary>Signin page:</summary>

  ![Signin Page](static/screenshots/sigin-page.png)
  </details> 

  - This is where user can sign up. 

  <details>
  <summary>Signup Page:</summary>

  ![Signup Page](static/screenshots/signup-page.png)
  </details> 

### **Database Design**

This site has six database model and the checkout app has two. One is Order and the other is OrderLineItem models

- Order Model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|order_number|order_number|CharField|max_length=32, null=False, editable=False| 
|user_profile|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'|
|full_name |full_name |CharField|max_length=50, null=False, blank=False|
|email_address |email_address|EmailField|max_length=254, null=False, blank=False|
|phone_number|phone_number|CharField|max_length=20, null=False, blank=False|
|country|country|CountryField|blank_label='Country *', null=False, blank=False|
|postcode|postcode|CharField|max_length=20, null=True, blank=True|
|city_or_town|city_or_town|CharField|max_length=40, null=False, blank=False|
|street_address1|street_address1|CharField|max_length=80, null=False, blank=False|
|street_address2|street_address2|CharField|max_length=80, null=True, blank=True|
|county|county|CharField|max_length=80, null=True, blank=True|
|date|date|DateTimeField|auto_now_add=True|
|delivery_cost|delivery_cost|DecimalField|max_digits=6, decimal_places=2, null=False, default=0|
|order_total|order_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|grand_total|grand_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|original_bag|original_bag|TextField|null=False, blank=False, default=''|
|stripe_pid|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''|

- OrderLineItem Model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|order|order|ForeignKey|Orders, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
|product|product|ForeignKey|Product, null=False, blank=False, on_delete=models.CASCADE|
|product_size|product_size|CharField|max_length=2, null=True, blank=True|
|quantity|quantity|IntegerField|null=False, blank=False, default=0|
|lineitem_total|lineitem_total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False|

- Category Model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|name|name|CharField|max_length=254|
|friendly_name|friendly_name|CharField|max_length=254, null=True, blank=True|

- Product Model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|category|category|ForeignKey|'Category', null=True, blank=True, on_delete=models.SET_NULL|
|sku|sku|CharField|max_length=254, null=True, blank=True|
|name|name|CharField|max_length=254|
|description|description|TextField|   |
|sizes|sizes|BooleanField|default=False, null=True, blank=True|
|price|price|DecimalField|max_digits=6, decimal_places=2|
|rating|rating|rating|DecimalField|max_digits=6, decimal_places=2, null=True, blank=True|
|image_url|image_url|URLField|max_length=1024, null=True, blank=True|
|image|image|ImageField|null=True, blank=True|

- UserProfile Model:

|Name|Database Key|Field Type|Validation|
|---|---|---|---|
|user|user|OneToOneField|User, on_delete=models.CASCADE|
|default_phone_number|default_phone_number|CharField|max_length=20, null=True, blank=True|
|default_street_address1|default_street_address1|CharField| max_length=80, null=True, blank=True|
|default_street_address2|default_street_address2|CharField|max_length=80, null=True, blank=True|
|default_city_or_town|default_city_or_town|CharField|max_length=40, null=True, blank=True|
|default_county|default_county|CharField|max_length=80, null=True, blank=True|
|default_postcode|default_postcode|CharField|max_length=20, null=True, blank=True|
|default_country|default_country|CountryField| blank_label='Country', null=True, blank=True|

## **User Stories**

These user stories were developed for the project using Agile development methodology.
To see the full list, click [here.](https://github.com/users/krandon1986/projects/7/views/1 "Link to HardWear Project" ) to User Story Project. 

#### **Shopper**
* [User Story # 1](https://github.com/krandon1986/project-5-e-commerce-application/issues/1) 
    
  <details>
  <summary>View Product</summary>

    ![User Story 1](static/screenshots/User-Story-1.png)
    </details> 
    <br>

* [User Story # 2](https://github.com/krandon1986/project-5-e-commerce-application/issues/2)
    
    <details>
    <summary>Special Deals or Offer</summary>

    ![User Story 2](static/screenshots/user-story-2.png)
    </details>
    <br>

* [User Story #3](https://github.com/krandon1986/project-5-e-commerce-application/issues/3)

    <details>
    <summary>View Purchase Total</summary>

    ![User Story 3](static/screenshots/user-story-3.png)
    </details>
    <br>
  
* [User Story #9](https://github.com/krandon1986/project-5-e-commerce-application/issues/9)
    
    <details>
    <summary>Sorting List of Products</summary>

    ![User Story 9](static/screenshots/user-story-9.png)
    </details>
    <br>

* [User Story # 10](https://github.com/krandon1986/project-5-e-commerce-application/issues/10)
    
    <details>
    <summary>Sorting a Specific Category</summary>

    ![User Story 10](static/screenshots/user-story-10.png)
    </details>
    <br>

* [User Story # 11](https://github.com/krandon1986/project-5-e-commerce-application/issues/11)
    
    <details>
    <summary>Sorting Multiple Product Categories</summary>

    ![User Story 11](static/screenshots/user-story-11.png)
    </details>
    <br>

* [User Story # 12](https://github.com/krandon1986/project-5-e-commerce-application/issues/12)
    
    <details>
    <summary>Product by Name and Description</summary>

    ![User Story 12.1](static/screenshots/user-story-12.1.png)
    ![User Story 12.2](static/screenshots/user-story-12.2.png)
    </details>
    <br>

* [User Story # 13](https://github.com/krandon1986/project-5-e-commerce-application/issues/13)
    
    <details>
    <summary>Previous Search Result</summary>

    ![User Story 13](static/screenshots/user-story-13.png)
    </details>
    <br>

* [User Story # 14](https://github.com/krandon1986/project-5-e-commerce-application/issues/14)
    
    <details>
    <summary>Product's Size and Quantity</summary>

    ![User Story 14](static/screenshots/user-story-14.png)
    </details>
    <br>

* [User Story # 15](https://github.com/krandon1986/project-5-e-commerce-application/issues/15)
    
    <details>
    <summary>Viewing Items</summary>

    ![User Story 15](static/screenshots/user-story-15.png)
    </details>
    <br>

* [User Story # 16](https://github.com/krandon1986/project-5-e-commerce-application/issues/16)
    
    <details>
    <summary>Product Quantity Adjustment</summary>

    ![User Story 16](static/screenshots/user-story-16.png)
    </details>
    <br>

* [User Story # 17](https://github.com/krandon1986/project-5-e-commerce-application/issues/17)
    
    <details>
    <summary>User Payment Information</summary>

    ![User Story 17](static/screenshots/user-story-17.png)
    </details>
    <br>

* [User Story # 18](https://github.com/krandon1986/project-5-e-commerce-application/issues/18)
    
    <details>
    <summary>User Personal and Payment Confidentiality</summary>

    ![User Story 18](static/screenshots/user-story-18.png)
    </details>
    <br>

* [User Story # 19](https://github.com/krandon1986/project-5-e-commerce-application/issues/19)
    
    <details>
    <summary>Order Confirmation</summary>

    ![User Story 19.1](static/screenshots/user-story-19.1.png)
    ![User Story 19.2](static/screenshots/user-story-19.2.png)
    </details>
    <br>


#### **Site User**
* [User Story # 4](https://github.com/krandon1986/project-5-e-commerce-application/issues/4) 
    
  <details>
  <summary>Account Registration</summary>

    ![User Story 4.1](static/screenshots/user-story-4.1.png)
    ![User Story 4.2](static/screenshots/user-story-4.2.png)
    ![User Story 4.3](static/screenshots/user-story-4.3.png)
    ![User Story 4.4](static/screenshots/user-story-4.4.png)
    ![User Story 4.5](static/screenshots/user-story-4.5.png)
    </details> 
    <br>

* [User Story # 5](https://github.com/krandon1986/project-5-e-commerce-application/issues/5)
    
    <details>
    <summary>Login/Logout</summary>

    ![User Story 5.1](static/screenshots/user-story-5.1.png)
    ![User Story 5.2](static/screenshots/user-story-5.2.png)
    </details>
    <br>

* [User Story # 6](https://github.com/krandon1986/project-5-e-commerce-application/issues/6)
    
    <details>
    <summary>Password Recovery</summary>

    ![User Story 6.1](static/screenshots/user-story-6.1.png)
    ![User Story 6.2](static/screenshots/user-story-6.2.png)
    </details>
    <br>

    

#### **Admin/Store Owner**
* [User Story # 20](https://github.com/krandon1986/project-5-e-commerce-application/issues/20) 
    
    <details>
    <summary>Add a Product</summary>

    ![User Story 20.1](static/screenshots/user-story-20.1.png)
    </details>
    <br>

    <details>
    <summary>Edit a Product</summary>

    ![User Story 20.2](static/screenshots/user-story-20.2.png)
    ![User Story 20.3](static/screenshots/user-story-20.3.png)
    ![User Story 20.4](static/screenshots/user-story-20.4.png)
    </details>
    <br>

    <details>
    <summary>Delete a Product</summary>

    ![User Story 20.5](static/screenshots/user-story-20.5.png)
    ![User Story 20.6](static/screenshots/user-story-20.6.png)
    </details>
    <br>

  



To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

