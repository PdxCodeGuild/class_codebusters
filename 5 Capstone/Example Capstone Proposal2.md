# Pryced - Capstone Proposal

## What is Pryced?
Pryced is the industry leading budget app for the common folk. Aimed at providing an easy way to track finances and budget for the future.

## Project Overview
Pryced will allow users to upload a csv, then separate individual items into budget categories. The app is attempting to help users budget their finances more easily. I plan to use Django for the backend and Vue on the front end. I may look into a data visualization library for JS.

## Functionality
- Allow the user upload a csv (most banks allow you to download a csv with all of your transactions.)
- Allow the user to sort transactions into budget categories.
- Allow the user to create categories and set a budget on them.
- Display budgets and spending on a dashboard

## Data Model
![Example DB](ExampleDB.png)
- Month (Used mainly for displaying the current month on the dashboard)
    - Month Name
    - Year
    - User (ForeignKey to User)
- Category
    - Name
    - Budget Amount
    - Comments
    - month (ForeignKey to Month)
    - User (ForeignKey to User)
- Transaction
    - Transaction Date
    - Transaction Amount
    - Description
    - category (ForeignKey to Category, nullable)
    - User (ForeignKey to User)
- User
    - Total Earnings


## Schedule
### Week 1
- [ ] Learn Vue CLI
- [ ] Set up Models
    - [x] User
    - [x] Transaction
    - [ ] Category
    - [ ] Month
- [ ] Create a dummy csv for testing
- [ ] Create Management command to load dummy csv into db


### Week 2
- [ ] Create User signup/login pages (With Styling)
- [ ] Get User signup/login functionality working
- [ ] Create a dashboard based on the dummy data
    - [ ] Display each category on its own with amount spent/budget amount ex: $700/$1200 (Maybe even show this as a pie graph)
    - [ ] Add modal to display transactions within a category


### Week 3 (I plan to have a fully functional capstone by the end of week 3)
- [ ] Create functionality for users to input data
    - [ ] Create a new Month
    - [ ] Create a new Category
    - [ ] Create a new Transaction
- [ ] Display unbudgeted transactions in their own list to be sorted
- [ ] Create functionality for csv upload (This may take a while)
- [ ] Styling and bug fixes

### Week 4
- [ ] Look into drag/drop for sorting transactions
- [ ] Look into creating a printable summary page