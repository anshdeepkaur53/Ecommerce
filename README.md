# Ecommerce-
TEAM WEB-ALPHA CLAN

ABOUT US :

The theme of our project is : AIDING SMALL BUSINESSES

Since, COVID-19 has become a full-blown pandemic, unemployment rates have skyrocketed and businesses are being forced to shutter their doors for the sake of public health. It is certainly a stressful time, especially for small business owners who have much smaller coffers to sustain them. So , we the team 'WEB-ALPHA CLAN' have come up with a platform that is , a website which involves the vast variety of gifts and trinkets thus, the site named "Gifts and Trinkets" .

We provide :

Vast variety of handmade gifts from artissans of across India

Fresh flowers from the florists nearby for gifting to our near and dear ones as memorabilia.

A delicious range of gourmet products online – birthday cakes, cheese cakes, chocolate cakes, macarons, vegan cakes, individual desserts, gluten free cakes, pies, pastries and more – all baked fresh daily and delivered free.

With this initiative of ours we have managed to employ not just one but a 'group of professionals' involving the home-bakers, florists, the artists who make hand-gifts for an earning and the delivery people. In this pandemic, everyone is incurring losses and losing livelihood, and our website also supports the ones who are not in in the limelight and are trying to survive in these times.

Components:

Main page (header, product overview, categorical navigator,home page navigator, shopping cart)
Product display page (detailed info, add to cart)
Category page (product overview under a specific category)
Admin panel (add/edit/delete products and manage transactions)
Login and register panel (sign up as customer, signup as seller/sign-in)
Idea of Our Product:

We are giving the 'user friendly' approach in the most convinient way.The site opens up on the store page with all the products without any issues.

Here, a user can 'Add the items' to cart without signing in. This is the part where we have introduced a feature of Guest Login, an ease factor, through which they can order their products to the desired locations, but even if later they change their mind that they want to create an account on our website,they can still sign up and see and track their orders.

For the checkout page, we have given the option of online payment as well as credit/Debit card payment for the ease of the user.

Now, as for the seller's part, they need to sign up to our website as a seller, so as to upload the products alongwith the prices.Once something is ordered, the payment is made directly to their business account.

The future deployment that is under testing yet is that we will be deploying a covid tracker on our page using an alert by Javascript. If the user clicks 'OK' on it, the page will re direct to another page where the covid tracker is setup with the current info across the world.

Also , there is a feature of geolocation using the Google Map API which will provide us with the near-by stores/sellers at the required delivery locations for quicker services.

WORK FLOW:

We have used Django for the implementing our ideas. When the user opens our website,he will be viewing the 'Our Store' page, where he would be able to order the desired items. When the user clicks on a particular item's 'Add to Cart ' button, a GET request is sent to the cart function which in turn increases the product quantity and also displays the product in the cart section alongwith its value and quantity.

If the user wants to open his account on our website ,they can access the Login button which reverses the flow and takes us to the login panel. Similarly, whenever a customer wants to signup , they will be redirected to a different page and a seller will be redirected to a different one. This way the database of the user and the ustomers in the django admin panel are not mixed up.

Now , about the guest login idea, we have used cookies to store the data in the cart until the user checks out and does the payment. If a user orders something from our website , he will be added as a customer in the 'customers' section in our django admin panel. Now if the user wants to signup after sometime, using the same email id, he can signup and still find the order that was placed in his order history as the cookies and the customer are connected.

A unique csrf token is generated for each and every user of our website, be it a logged in user or a guest user.

If the user wants to checkout, he can click the button on the cart page which will redirect to the checkout page with a GET request.Now the user can fill the details in and then when he clicks on paypal buttons , they will open up asandbox paypal port where the user may login and sign up to their paypal account. The payment of the products will through Paypal's gateway directly to the seller's account.Once the payment is completed a javascript alert is displayed with the message of 'Transaction completed', which will then redirect them to the store page with the cart emptied after checkout.

The work flow diagram of our pages is provided in the following link : https://drive.google.com/file/d/141qbNvSwod55y-MPv9dFREo5WCikXpzU/view?usp=sharing

The product add to cart flow ad page transfer flow is in the following link : https://drive.google.com/file/d/140vUgVB2ocHcrz9KBxq37L-RZ9KrKsTR/view?usp=sharing

The Model and workflow of our models.py file with all the main involved functions and their linking is provided in the following link : https://drive.google.com/file/d/1S6S2026l479RrEMNKPay0vAXrnIyg44U/view?usp=drivesdk

The copyright links used are :

Google Api for the location : https://developers.google.com/maps/documentation/javascript/geolocation

The Sandbox Paypal section : https://developer.paypal.com/developer/accounts/

SECURITY :

The security part is assured by the backend part so that the user cannot change the prices from the frontend and even if in case a user tries to do a security break, they would receive an unautorized csrf undefined token issue due to which they would not be able to proceed.

Also,the credentials generated from the paypal payment would directly pay the amount to the seller's bussiness account so the payment to them is safe.

INSTALLATION INSTRUCTIONS:

In the command prompt
-- Pip install Django

cd to the folder and then
-- python manage.py startapp store

INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',

'store.apps.StoreConfig', ]

In your command promt run "python manage.py runnserver" and open up port 127.0.0.1:8000.

KNOWN BUGS :

The login and signup page doesn't seem to be displaying the data after submission to the django administration.

Currently there is no cash on delivery method.

TROUBLESHOOTING:

For any kind of support and help please contact via mail given below.

Support mail: anshdeep.kaur2000@gmail.com
