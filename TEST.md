# Testing

This is the Testing section of the [README.md](README.md) file.  
It contains all the testing information for the project The hair experts.


## Responsiveness

Tested on mobile, tablet, laptop and desktop. 
And all devices works as expected.

## Browser Test

Google Chrome  - Pass  
Microsoft Edge  - Pass   
Firefox - Pass    
Brave - Pass  

## Stripe Test

All the payments and webhooks has been successfully tested.

![Stripe payment webhook test](testing-image/stripe/stripetest.png)

## Validation

### HTML Validation

HTML validation all passed.

**Home page**

![HTML validation home page](testing-image/html/hom-validation.png)


**Product page**

![HTML validation product page](testing-image/html/product-page-validation.png)

**Product detail page**

![HTML validation product detail page](testing-image/html/product-detail-validation.png)

**Shopping bag page**

![HTML validation shopping bag page](testing-image/html/shopping-bag-validation.png)

**Check out page**

There is no error present.

However, one warning for h1 tag using for spinner.
As this is a warning, I decided to leave as is.

![HTML validation checkout page](testing-image/html/checkout-page-validation.png)

**Check out Success Page**

![HTML validation checkout success page](testing-image/html/chekout-success-validation.png)

**News page**

![HTML validation news page](testing-image/html/news-page-validation.png)

**Sign Up page**

![HTML validation sign up page](testing-image/html/sign-up-page-validation.png)

**Login page**

![HTML validation login page](testing-image/html/login-page-validation.png)

**Logout page**

![HTML validation logout page](testing-image/html/logout-page-validation.png)

**My Profile Page**

![HTML validation My profile Page](testing-image/html/my-profile-page-validation.png)

**Stock Management Page**

![HTML validation Stock Management Page](testing-image/html/stock-mg-page-validation.png)

**Edit Product Page**

![HTML validation Edit Product Page](testing-image/html/edit-product-page-validation.png)


**News Letter**

![HTML validation News Letter Page](testing-image/html/newsletter.png)
**News Letter Success Message Page**

![HTML validation Success Meessage Page](testing-image/html/success.png)


**News Letter Fail Message Page**

![HTML validation Fail Meessage Page](testing-image/html/fail.png)


## Lighthouse testing

All the lighthouse testing scores are high. Only the Best Practices score is below 80 this is because of cookie related issue with version 3 of stripe.

**Home Page**

![Lighthouse test home page](testing-image/lighthouse/home.png)

**Product Page**

![Lighthouse test product page](testing-image/lighthouse/product.png)


**Detail Page**

![Lighthouse test detail page](testing-image/lighthouse/detail.png)

**Shopping bag Page**

![Lighthouse test shopping bag page](testing-image/lighthouse/shopping-bag.png)

**Checkout Page**

![Lighthouse test checkout page](testing-image/lighthouse/checkout.png)

**Checkout Success Page**

![Lighthouse test checkout success page](testing-image/lighthouse/checkout-success.png)

**News Page**

![Lighthouse test news page](testing-image/lighthouse/news.png)

**Sign Up Page**

![Lighthouse test signup page](testing-image/lighthouse/signup.png)

**Login Page**

![Lighthouse test login page](testing-image/lighthouse/login.png)

**My Profile Page**

![Lighthouse test profile page](testing-image/lighthouse/profile.png)

**Logout Page**

![Lighthouse test logout page](testing-image/lighthouse/logout.png)

**Stock Management Page**

![Lighthouse test stock management page](testing-image/lighthouse/stockmanagement.png)

**Edit Product Page**

![Lighthouse test logout page](testing-image/lighthouse/edit-product.png)

**News Letter Page**

![Lighthouse test news letter page](testing-image/lighthouse/newsletter.png)

**News Letter Success Message**

![Lighthouse test success message page](testing-image/lighthouse/success.png)

**News Letter Fail Message**

![Lighthouse test success message page](testing-image/lighthouse/fail.png)

**404 Page**

![404 Page test](testing-image/lighthouse/404.png)

## CSS Validator Test

All the css files have passed.

**base.css**

![CSS validator test base.css](testing-image/css/css-test.png)

**product.css**

![CSS validator test product.css](testing-image/css/product.png)

**shopping_bag.css**

![CSS validator test shopping_bag.css](testing-image/css/shopping_bag.png)


**news.css**

![CSS validator test news.css](testing-image/css/news.png)

**profile.css**

![CSS validator test profile.css](testing-image/css/profile.png)

**checkout.css**

![CSS validator test checkout.css](testing-image/css/checkout.png)

**newsletter.css**

![CSS validator test newsletter.css](testing-image/css/newsletter.png)


## JS Hint

**base.js**

![JSHint base.js](testing-image/js/base.png)

**countryfield.js**

![JSHint countryfield.js](testing-image/js/countryfield.png)

**strip.js**

There are strip undifined variables. as they are coming from different app I left these as is.
![JSHint strip.js](testing-image/js/strip.png)

## User Stories Test 

### Sprint 1 
**Epic 1 Create the initial project setup**

- [x]  As a Developer, I want to create the project structure so I can develop the Hair Experts website

**Epic: 2 Create home page**

- [x] As a user, I want to be able to open the home page and understand what is this website for.

- [x] As a user, I want to have easy navigation so that I can move through the pages on the site.

- [x] As a user, I want to browse the footer of the webpage so that I can see what's there.

- [x] As a user, I want to see if the website has social media so that I can visit them.

- [x] As a user, I want to be able to access the website on any device so that I can view the content.

**Epic 3: Product setup**

- [x] As a developer I want to create the websites database and add products

- [x] As a user, I want to see the products page clearly so that it is easy to find products.

- [x] As a user I want to click on the product image and have a details page open.

### Sprint 2 

**Epic 4: Create Product Filtering and Sorting**

- [x] As a user, I want to be able to sort products on the products page so that I see sort by different categories.

**Epic 5: Create shopping basket functionality**

- [x] As a user I want to be able to add items to my shopping basket so that I can see what is in the basket.

- [x] As a user I want to be able to modify the items of my shopping basket so that I can change my order.

**Epic 6: Create Notifications**

- [x] As a user, I want to see a notification when I add, update and delete item to the shopping basket so I see what is in the basket

### Sprint 3 

**Epic 7: Create checkout app**

- [x] As a developer, I want to add checkout data to the database so that I can store the users order data in the database.

- [x] As a user, I want to fill out my information so that they can send my order

- [x] As a user, I want to pay securely so that I can complete the payment without any worries

- [x] As a developer, I want to use stripe webhooks so that I can update the database when a payment is confirmed

- [x] As a user, I want to receive a confirmation email when I complete my order so I can see what I've purchased

**Epic 8: Profile App**

- [x] As a user, I want to have a personalized user profile so that I can check my order history, confirmation, and payment information.

### Sprint 4 

**Epic 9: Create Admin Profile**

- [x] As an owner I want to have add, edit and delete functionality for the site items to manage stock.

**Epic 10: Create News Field**

- [x] As a site owner, I want to have a news section so that I can inform customers about upcoming news

- [x] As an Admin I want to Add, Edit and Delete News articles on the sites news page so that I can keep it updated

- [x] As an Admin I want to Add, Edit and Delete News articles on the sites news page so that I can keep it updated

**Epic 11: Additional functionality**

- [x] As a developer I want to check and finalize this website so that I can complete this site

- [x] As a site owner I want to publish the website so that customers can see

**Epic 12: Final Touch**

- [x] As a user I want to be able to subscribe to a news letter so that I can stay up to date with the latest news and offers.

- [x] As a developer I want to check and finalize this website so that I can complete this site

## Python Test 

All the files I have created over the duration of the project I have tested and fixed all errors. I have not made any changes to the env file or the 404 handler as these are unused, which is why they still show as errors.

![python test ](testing-image/python/python-test.png)

## Manual Test 

**Navigation bar**

![Navigation bar test](testing-image/manual-test/navbar.gif)

**Search bar**

![Search bar test](testing-image/manual-test/search.gif)

**Sort**

![Sort test](testing-image/manual-test/sort.gif)

**Home**

![Home page test](testing-image/manual-test/home.gif)

**Detail's page and Adding Products in a basket**

![Detail page and adding product test](testing-image/manual-test/adding-bascket.gif)

**Delivery Fee**

![Delivery fee test](testing-image/manual-test/delivery-fee.gif)

**Payment Form**

![Payment form test](testing-image/manual-test/payment-form.gif)

**Payment**

![Payment test](testing-image/manual-test/payment.gif)


**Recommendation**

![Recommendation test](testing-image/manual-test/recommendation.gif)

**Comment add/delete**

![Comment test](testing-image/manual-test/comment.gif)

**Register / Login / Logout**

![Register login logout test](testing-image/manual-test/register-login-logout.gif)

**Profile**

![Profile test](testing-image/manual-test/profile.gif)

**Product Management - Add/Edit/Delete**

![Product management test](testing-image/manual-test/product-mg.gif)

**News - Add/Edit/Delete**

![News test](testing-image/manual-test/news-crud.gif)

**News Letter**

![News letter test](testing-image/manual-test/news-letter.gif)

**Footer**

![Footer test](testing-image/manual-test/footer.gif)

**404 Page**

![404 page test](testing-image/manual-test/404.gif)

