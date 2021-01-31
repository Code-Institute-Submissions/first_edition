# Testing

**As a user, I want to create an account and then sign into my profile:**

1. If you're logged in, log out by clicking my account in top left, logout and then sign out. Otherwise skip this step.
2. Click Login in the top right, then register.
3. Try and break the form by entering mismatched passwords, emails, passwords that don't fit the criteria.
4. Enter a valid email address, username, password.
5. Go to the homepage and append /admin and press Enter
6. Now login as uername admin password 12345.
7. Click email addresses, then the email you registered and click verify.
8. Go back to the main website, logout, then login by entering the same credentials you used for signing up.


*Results:* Pass, the new account was created after being verified by the admin. The django allauth form didn't break with my attempts either.

**As a user, I want to be able to search for a product:**

1. On any page, click on the searchbar.
2. Type in a book name, part of a string of the book name or part of the description.
3. Press the enter key.
4. Repeat this step for other descriptions and book names.

*Results:* Fail. Although it worked at the start of my project, I had updated it with a new searchbar from freefrontend.com. I realized that I didn't set the input name to ="q" which is what my products view was searching for. I changed my input tag to be this:

```html

    <input id="search" class="search-input" type="search" name="q" placeholder="Search all Products" autofocus required />
```

After doing this, it worked exactly as intended.


**As a user, I want to buy a product:**

1. Navigate to the products page by whatever means you please, such as clicking on the products nav-link and then a category in the dropdown.
2. Click on any product image or name to get to the product detail page.
3. Click add to bag.
4. Click either on the toast navigate to checkout button or the shopping trolley/dollar amount in the nav.
5. Click checkout now
6. Enter incorrect details first to check to see if the criteria is being applied correctly from the Order Model and click complete order.
7. After fiddling around with that, enter satisfactory criteria and a card number repeating the number "42" and then complete order.
8. If you made it to checkout success, go to your stripe dashboard, developers on the right hand side and check if your payment has succeeded.

*Results:* Pass, I make it to checkout success, the webhook goes through on stripe and my forms account for any errors in its input (for example, not having an integer in the phone number input or putting an incorrect card number for payment.)

**As a user, I want to save a product for later and potentially add it to bag:** 

1. Navigate to the products page by whatever means you please, such as clicking on the products nav-link and then a category in the dropdown.
2. Click on any product image or name to get to the product detail page.
3. Click Save for later
4. Click on the trolley/ dollar amount in the navigation.
5. Scroll down to see if it has correctly been added.

*Results:* Pass, I see the product in the bag template under saved for later items.