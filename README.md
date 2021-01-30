Table of Contents
=================

   * [Title](#The-First-Edition)
   


# ***The First Edition***

The First Edition is an ecommerce website which serves the purpose of providing books for sale on an online platform. It is extremely comphehensive, allowing the user to add products to a shopping bag,
then actually buying the products using stripe payments. If the user makes a profile, they can actually track their orders in the order history page. Users also have the ability to save the items for later and add them to a bag, which
will stick with them as long as the site cookies arent deleted.

The admin account has the username of "admin" and password of "12345". They have access to CRUD operations with products directly on the website and even more functionality through Django administration such as checking the sites userbase and orders that are 
made throughout the website. It can be accessed by appending "/admin" onto the homepage. 




# UX 

**As a user, I want to create an account:** The user can create an account oy clicking register on the top right hand side of any webpage. From there, they must enter their email address, insuring that it follows the correct syntax, renter their email. Provide a username unique to the 
website, a password that matches the criteria, repeat said password and finally click on sign up. They'll be notified on a new page that a confirmation email has been sent to the email they entered. Now they can check their email and click on the link. The user has successfully signed up
with a new account. If they user is already logged in with an account, they can click on my account in the top right, from the drop down click log out and then the sign out button on the new webpage.

**As a user, I want to sign into my profile:** You must have made a profile as some stage before attempting this step. A guide on how to do so is above. To sign in, simply click on the login nav link and then entered your username and password. From there, 
click on the sign in link and you will be redirected to the homepage. If you have forgotten your password, you can click on the Forgot password link below the form. From there, you enter your registered email address and click on the reset password button. Check your
email and then click on the link. You now have the option to create a new password. Upon doing so, you will now be logged in to your profile.

**As a user, I want to update my profile details:** First off, make sure you are signed in. Next, click on the register 

**As a user, I want to buy a product:** The user can select a product from either the highly rated products (4+ stars) from the home page, clicking on the buttons next to the highly rated products, or clicking on the products nav link and selecting the category they want. From there, they
can click on the product image or name and will be able to add the prouduct to their bag. On the same page, They can adjust the quantity by typing the amount or using the up/down buttons. From here, they can click on the toast button "Go to Checkout" on the right hand side or the nav link 
in the top right with the bag and newly updated price tag. They should click on secure checkout again and give their delivery details. The card details must either be real  or one of stripes test payment details, such as repeating the number 42 over the entire card (Dont worry, stripe
is set to test mode, you wont be charged). Click on checkout order and a new webpage will appear called checkout_success saying that your order was successful and it will show you your order details.

**As a user, I want to save a product for later and potentially add it to bag:** This is similiar to the above steps. Basically, you nagivate to the product detail page by clicking on the product image or name. From there, you click on the save for later
button. By clicking on the bag nav link in the very top right hand side, you'll see at the bottom a saved for later heading. Underneath, your product will be stored in a table. You can either move this product to your bag or remove it entirely from the 
saved for later table.

**As a user, I want to check my order history:** If you dont have an account, you can check this by filtering your email to ____ and then you'll see any confirmation emails you have. This is also available to users with an account but they have the option 
to check all their orders on one webpage. Assuming they're logged in, they can click on my account nav link and select the order history dropdown link. From here, they'll see every single order they've ever made on ________

**As an admin, I want to be able to create a new product:** First, you must log in as an admin, I've created an admin account which you can login as the username "admin" and password "12345". After that, you can use the django administration by appending 
"/admin" onto the homepage (alternatively you can login from this screen) and then clicking on products, then add new product in the top right. The entry criteria for the fields can be seen in products/models.py. There is an even easier way to do this.
Clicking on the add a product nav link will bring up a similiar form except its through the website itself.

**As an admin, I want to be able to edit a product:** On the Djagno administration, its possible to edit a product by clicking products and then clicking the books ISBN number on the list of books. The form will be filled out already, its a matter of
twaking the pre existing entries in the fields that you want changed. It's also possible through the website too. Go to the products or product details page and then click on the edit button, the form will also be filled in like before.

**As an admin, I want to delete a product:** In the django administration, click on products and then the product ISBN you wish to delete. The form to edit the product will open up but you need only go down to the bottom left and click the red delete button.
On the Website, The delete button will always be next to the edit button. Click on the button and confirm the deletion of the product.


# Features

### On the Base Template 

**Navbar:** The navbar is fumdamental to by website and will stick to the top of the page if the user scrolls down. The navigation links will depend if the user is logged in or not and what type of user they are, but it will always contain a home button
(which is the sites name, The first Edition) on the top left, the products dropdown menu and a bag that stores all the users saved and bagged products.

**Search bar:** The searchbar is also present on the navbar, the user can search by ____

**Footer:** In the sites footer, there are workable links to different product categories and non functional links to our social media pages, privacy Policy, contact us and about us.

### On the Index Template 

**Hero Image:** A user can get a first impression of your website within the first half a second, so I made an effort to make its hero image as appealing as possible. I also have__________

**Highly rated books:** Underneath, I have books that are rated above 4 stars out of 5 in 3 different book categories and also bestsellers, which is a boolean. The user can click on the book image to go straight to the product details page or click on
the coral coloured button to see the rest of that specific category/bestsellers. This can be manipulated by ____________

### On the products template

**All products shown in a given category:** Either through the dropdown on products in the nav link, the footer or the index page, the user can select a category to filter the books that they can search for. You can see basic information of the products
here such as the name, the author, its price, category and rating.

**Search all Products:** In the navigation dropdown, they can also search all products and display it on one webpage.

**Sorting Products:** Regardless of its all products or a category, the user can sort the displayed products by clicking on the sort by link in the top right and then filter by price, rating or name. They can sort by either low or high in the first two
cases and alplabetically/reverse alplabetical order in the later example.

### On the Product Detail Template

**Renders all of the products information:** More information will be displayed on this page, including its Format, its ISBN, Description, length, publisher and an optional professional endoresment will be rendered if there is one.

**Customers reviews:** If there is a customer review (I have reviewed the book "Dune", the rest of the products have no reviews) then it will be displayed at the bottom of the page. If you're logged in and ordered the book yourself, you can also
review the product.

**Has the means to buy the product:** There is a button to add the product to your shopping bag, which is the first step to actually purchasing it. The quantity can also be picked between 1-99 just above this button. If you're interested in the product but unsure if you'll buy it, you can click save for later and it'll
be on the same page as the shopping bag, just underneath.

### On the Bag Template

**The Bag Items:** All the items you've added to the bag are displayed here. You have the option of adjusting the quantity or removing specific products. The product grand total will be printed at the bottom and a free shipping threshhold of 20 Dolalrs
will be taken into account. Either, there will be red text stating the amount you're short of free shipping or there wont and the delivery field will be free and calculated at 0.00. If there are no bag items, it'll say that the bag is empty and a link
to the all products page will be shown as "_____"

**Saved for later items:** Saved for later items will be displayed underneath the bag items. The user has the ability to either remove the item from this table or move it to the basket. Moving it to the basket will set the quantity to 1 and remove its
entry in the saved for later item.

### On the Checkout Template

**Order Summary:** The items from your bag will be displayed on the right hand side of the screen with its name, image, quantity and price. The total costs of the items and delivery will be added to the grand total below.

**Checkout Form:** The user must supply their delivery details to the form alongside their full name and email account (which is important as it'll be linked to send them the order confirmation). The user must also give their card details, repeating the
number "42" will be sufficient for testing purposes.


### On the My accounts templates

**Profile Details:** ______


**Order History:** Under the my account dropdown in the navigation link, the user can open a seperate tempalte to view their order history. all their ordered products will appear here ____

### Allauth templates

I downloaded a package called called alluath which is a massive assistance for speeding up the process for user authentication. This would include the registration process with the singup page, confirmation email confirm page, the login page, logout page, resetting
password page and some other pages that share a similiar function. Their purpose is straightforward and simple.

### Toasts


## Features left to Implement

**Stock Counter:** I wanted to add a stock counter in the product models as a simple integer that would decrease by the quantity in the checkout_success tempalate. However, my mentor informed me that this was way more work than I thought as making it so 
if two users bought something at the same time, it would create a problem.

**Different formats for certain books:** I also wanted to make it so that some books would have multiple formats, such as a paperback and hardhack. They would require a different price image and ISBN to its counterpart. When I asked my mentor, I was 
told due to time constraints it probably wouldn't be worth adding this feature.

**Having a visually appealing star rating system:** I actually made an attempt at making this as you can see in my commits. However the data needed to be posted through javascripts AJAX. This had proven to be problematic as I couldn't find a way
to post the products id through AJAX, so I had to scrap the system due to time constrains for a visually less appealing rating system. I later realised near the end of my project that I could have used javascripts template literals to pass through the 
product id, but by then it was too late to implement fully. Otherwise, the functionality is very similiar.



# Technologies Used

Html 5: This language is used to present content on my website.

Css: Css is used for styling the web page, thus making it more attractive to the user if used correctly.

[Google Fonts:](https://fonts.google.com/) I have imported the fonts of Roboto and Ruda and have used it throughout my website.

[Heroku:](https://www.heroku.com/) A cloud based program that is used to deploy my website.It supports the Python Programming Language.

[Hover.css:](https://ianlunn.github.io/Hover/) This is used to add animations to by buttons such as float in the air and leave a shadow or grow in size in the case of some of my book images.

[Django:](https://docs.djangoproject.com/en/3.1/) The Full stack framework that I have used to develop my website.

[Allauth:](https://django-allauth.readthedocs.io/en/latest/) This is a django package designed to help with the user authentication and account management. It also allows me to use Social media authentication.

[Bootstrap:](https://getbootstrap.com/) Bootstrap is extremely useful and time saving with its responsive grid system and its pre built components, such as the sticky Nav I took from bootstrap. It also has custom classes for centering text, adding margins, setting
colours etc.

[Font Awesome:](https://fontawesome.com/) Many of the Icons used in my website are from font Awesome, like the quill you see next to the author name or the shopping bag card in the top right corner.



# Testing 

See the TESTING.md file.


# Deployment

See the DEPLOYMENT.md file.


# Credits


## Content

* I got the footer from [Mockplus.com](https://www.mockplus.com/blog/post/bootstrap-4-footer-template), specificially the first footer on the list.

* I found my searchbar on [freefrontend.com](https://freefrontend.com/css-search-boxes/).


## Media 

* I got the hero image from [Pixels.com](https://pixels.com/featured/the-lady-and-her-shelfs-marco-tagliarino.html?product=canvas-print), the artists name is Marco Tagliarino.


# Acknowledgements

* I got the idea for a simplistic black and whtie colour scheme from [this](https://youtu.be/mq8LYj6kRyE) youtube video. He says that having black, white and one strong colour (Coral in my case) is a fantastic basis for a colour scheme. I went 
with the same charcoal colour in my footer to be used on my navbar and then I balanced it out with some variations of greys.

* [Fontpair.co](https://fontpair.co/) has dozens of great font pairings and I used one of them for the basis for my websites typography.