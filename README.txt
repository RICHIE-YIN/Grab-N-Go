Grab-N-Go is a website similar to OfferUp and Facebook Marketplace. It allows users to list their items and inquire about 
items from other users.

This application was built using Python, MySQL, and Bootstrap. My main challenges in creating this application were building
the MySQL database itself (figuring out ManyToMany and OneToMany relationships), implementing SQL code into Python, and 
creating chat features using MySQL.

Breakdown of how the app functions:

- On the landing page, it automatically populates all available listings.
- When you create a new listing, you can include the title, description, price, condition, category, images, location, 
  zip code, city, and state.
- You can also create your own profile. If this is your first time registering on this app, you will be prompted to create 
  a profile. After creating a profile, you can then edit it if desired.
- Users also have the ability to check their own listings and perform actions such as viewing, editing, and deleting 
  listings if needed.
- When a user is interested in another user's item, they can send a message to that user regarding the product. This 
  initiates a new conversation between BOTH users.