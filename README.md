# The Hair Experts

![Am I responvive image](readme-image/amiresponsive.png)

The Hair Experts is the fifth project in the Code Institute Diploma in Full Stack Software Development.
It is a B2C ( Business to Consumer) full stack E-commerce website that offers a range of hair care products and treatments. User’s can create accounts, browse through a selected range of hair care products and items, add them to their basket and purchase them. Users also have the ability to create wishlists and leave comments on products. 

The project was developed using Django, Python, JavaScript, HTML5, CSS and a Postgres relational database to store the site's data. Stripe was used as the payment system

The project was developed using Agile methodologies. This was tracked using Githubs built in boards so I could create Sprints to track the Epics and User Stories.

## Project Goals ##

### Project Goal ###

The goal of the project is to create a full stack website for The Hair Experts built and developed using the Django framework, Bootstrap and CSS. Using Stripe as a payment system and to be deployed on the internet using Heroku and AWS S3 for storing files.

The project was designed to be easy to use and have a simple flow from product searching to product purchasing. 

### User Goals ###

- As a site user I want to shop and browse for hair care products and items.
- As a site user I want to be able to create an account on the website which will track my purchase history and keep track of the wishlist I have created.
- As a site user I want to be able to leave reviews/comments on products I have bought.
- As a site user I want to buy products securely. 

### Site Owner Goals ###

- As a site owner I want to have a platform to sell hair care products to people in Ireland, England and Europe.
- As a site owner I want a site that is known for its reliability.
- As a site owner I want a site that can grow.

## Design ##

### Colour Schemes ###

[Color Hunt](https://colorhunt.co/palette/2228312d4059ff5722eeeeee)

When developing the site I wanted to keep the colours simple. Keeping colours simple would make the pictures stand out and not overpower the images for the products with lots of colour.

![Colour scheme](readme-image/colour-schemes.png)

There was a low accessibility score due to the button contrast ratio.  I changed the buttons background lightness colour to  #AD6200 so that users can see the button more clearly. 

![button colour](readme-image/button-colour.png)

### Fonts ###

Logo: font-family: "Playfair Display", serif;

### Favicon ###

Used [Canva](https://www.canva.com/) to create
![favicon](readme-image/favicon.png)

## E-Commerce Business Model ##

**Business model: B2C** 

### Target Audience ###

From 20 to 60 year old women who live in Ireland that are also interested in hair products. 

![Target Market Example](readme-image/d-marketing/target-market.png)

### Vision ###

To provide customers with top-of-the-range hair solutions and the products that help their hair health reach its full potential.

### Objectives ### 

The Main objective is to increase profit streams from the online store and expand the market to other demographics and businesses. 

### Strategy ###

**To achieve this we need to:**

- Increase the website’s SEO
- Increase Facebook followers
- Increase news letter subscribers

### Digital Marketing ### 

#### Facebook ####

The hair experts will mainly use facebook to advertise our business.
This is the best place to focus on because 75.6% of the population in Ireland are using it. We will plan to upload to our Facebook at least twice a day, one for around lunch time and one for before bed time when our target audience who are busy during the day might have a better chance to see our page. We will research facebook insights to monitor clicks and engagement rates to see how effectively our facebook page and posts are working. We will also take advantage of Facebook advertising to reach as many people as possible. This can be run cheaply by setting a target audience for specific people to advertise. As this e-commerce site grows, running YouTube and google ads would be the next step to increase the company’s online presence which will help to increase our profit.

**Facebook Business Page**

![Facebook page](readme-image/d-marketing/facebook.png)

**Example post**

![Example post](readme-image/d-marketing/example-post.png)

#### Increase the Website’s SEO ####

We have a news section that can be updated often. 
We will use keywords that are related to hair products and update on a weekly basis. Topics are something related to hair like how to keep your hair healthy and tips to keep your hair shiny.
This will increase the site’s activity and improve engagement with our customers.

**News Page :**

Upload the contents that are associated mainly with hair and beauty and also sometimes topics that are using current trending keywords to increase the traffic a few times a week. Google Keyword Planner and Google trends are useful tools to find suitable keywords.

### Keyword research ###

Searched keywords with [Wordtracker](https://www.wordtracker.com/search?query=professional%20hair%20products%20for%20women) and [Keyserch](https://www.keysearch.co/)

**Meta tag**

Used long tail keyword

 ![Keyword in meta tag](readme-image/d-marketing/keyword-meta.png)

### Email Marketing ### 

Website has a newsletter section where customers can subscribe and get our news and special offers. We use mailchimp to send our campaigns so that we can track 
Open rates, click through rates and bounce rates.
This is good because we can test our emails to see what works or does not work.
Sending email to our customers also increases our website’s traffic and leads to calls to action.
We will use facebook posts to increase subscribers.

## User Experience (UX) ##

### Navigation bar ###
Navigation bar contains the links to the different website sections. The main page is the product page which also has a dropdown feature where you can select categories. You also have the search bar where you can search specific products by typing keywords in the box. The logo can be used to navigate to the home page. A user can easily access the other pages on the site to view Hair Products, Electrical Items and News. The layout will allow users to see everything the website has to offer at a glance.

The navigation bar features a news tab so that users can stay up to date with the website's latest news as well as a search bar that lets user’s search for an item directly.


![Navigation bar](readme-image/ux/navigation.png)

**dropdown**

The Navigation bar allows users to refine their search. They can browse all the site products. They can choose to select just hair products that will show the user what they offer. 

![Navigatrion dropdown](readme-image/ux/navigation1.png)

**Filter** 

When the user selects the electric section and selects only the hair dryer then this will be all that is displayed. This offers the user the ability to refine their search to find whatever it is they are looking for.

![Filter](readme-image/ux/filter.png)

### Home page ###

The website's home page showcases the main image or Hero image it is intended to grab the users attention.The shop now button goes directly to the product page that renders all the products this shop sells.

**Deliverly charge**

When a user reaches 50 euro free delivery will be applied to their shipping. The amount displayed will change depending on what is inside the basket. Once the limit has been reached it will be set to free shipping. This benefits the user so they can decide if they want to spend more.

![Home](readme-image/ux/home.png)

On the home page, the products have been categorised into three sections. This will make it easy to find products.

Memo:
Clicking on the shampoo and conditioner section will display the set products because the set includes both shampoo and conditioner

![Category](readme-image/ux/category.png)

### Footer ###

The foot sections mark the bottom of the page. It contains links to the hair experts social media sites which users can use to visit our social sites to learn more about us and keep updated on our latest news.

![Footer](readme-image/ux/footer.png)

#### Help Center ####

The help centre section gives the user the option to reach out to a member of the team for help if they need it. This lets the user know we will listen to their problems if they have one and try and help them solve it

![Help Center](readme-image/ux/help-center.png)

### Product Page ###

Product page shows product pictures,product name and price. Clicking on the picture can take the user directly to the product’s detail page. When the admin user is logged in it will display an edit and delete button that shows that the admin can control their stock from the product page. This is beneficial for users as the site 

![Product Page](readme-image/ux/produc.png)

#### Sorting feature ####

Sorting functionality on the products. Users can sort based on the sorting options below to help them find what they are looking for quicker.

![Sorting](readme-image/ux/sorting.png)

### Detail page ###

Displays details of product. Users can view the product's details and see if it is the right fit for their needs.

On the detail page when the admin user is logged in they can see the edit and delete button next to rating. This allows the admin control over the shop's stocks and users will always be kept informed on what products we have available.

![Dtail](readme-image/ux/detail.png)

#### Review ####

All users can view comments that have been left on product’s.
But the delete button is only visible to the user that wrote the comment.
Also when the user is logged in they can see the add comment for a product button. Once you click it, a comment form will be displayed that the user can leave a comment on this product. This is only visible for users that have logged in.

![Review](readme-image/ux/review.png)

### Shopping Bag ###

As the user shops on the site they can add products to their basket. When a product is added to the basket it will display the quantity of the product they have added as well as the price. This will let users know how much they are spending and how many items they are buying. 
User can also remove items from their basket this will decrease the price and the quantity.
This makes it easy for users to make changes inside the shopping bag. 

![Shopping bag](readme-image/ux/shopping-bag.png)

#### Recommendations ####

In the shoppoing bag they will see a recommendation for products at the bottom of the page. This will display recomendded products that might interest the user.

![Recommendation](readme-image/ux/recommendation.png)

When the Read Me button on the recommendation section is clicked a modal opens and displays details of the recommendation product. Clicking the picture of the product brings the user to the product detail page.

![Click the recommendation button](readme-image/ux/click-recommendation.png)

### Checkout page ###

Once the user has added the products to the basket. The user will see a form where they fill out their personal details including their address. This section also includes the secure payment form where users can input their card details to pay for their purchase.

This will benefit users as they can enter their personal details so they can ensure their products will be sent to the correct address and person. The secure payment allows users to safely enter card details and make payments. 

![Checkout](readme-image/ux/checkout.png)

#### After complete order button is pressed ####

When the user confirms their order they will see a spinning wheel this lets the user know their order is being processed. 

![Spinner](readme-image/ux/spinner.png)

#### Confirmation message after the shopping ####

When the purchase has been successful the user will see the confirmation pop up. This contains all the information the users need to know about their order.  This information benefits the user if they have any issue or need to find out anything about the order. 

![Confirmation](readme-image/ux/confirmation.png)

### Sign Up ###

Users can sign up and create an account for the website. Once a user has created their account they can access other features like adding and deleting comments. 

![Signup](readme-image/ux/signup.png)

When creating their account the user will be asked to confirm their email address, this lets the user know they have entered the correct email address.  

![Verify email](readme-image/ux/verify-email.png)

![Confirmation email](readme-image/ux/confirmation.png)

![alt text](readme-image/ux/confirm-email.png)

After confirm your email, you can login.

## Log In ##

Once a user has successfully created an account they can then login to their account through the login section of the website. 

![Login page](readme-image/ux/login-page.png)
![Login](readme-image/ux/login.png)

The website uses role based access for its users. When you login as an admin, product management will show up which controls the shop's stock items. 