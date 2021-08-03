
# Capstone Proposal

## Calorie Tracker
I want to build a simple calorie tracker app. Most calorie trackers include more than you need, so I plan to make a simplified version that fits my needs.

## Project Overview
This will be a simple calorie tracking app that will take in a users weight, goal weight, daily calorie needs and calorie consumption. I want to show a scale visualizing calories in vs calories out. There will also be a weekly/monthly view for tracking calories or weight overtime. It is important to view weight loss as a trend rather than by individual day. I will use django for the backend and possible a CSS framework for the styling (not yet decided).

## Functionality
- Allow the user to create a profile
  - Profile will contain goal weight, current weight, daily calorie needs, and daily calorie intake.
- Allow the user to see data as either daily, weekly, or monthly
- Daily data will be shown on a scale of calories consumed vs calories allowed for that day.
- Weekly and monthly will show as a line graph to better track weight over time.

## Data Model

#### Profile
- Users name
- Current weight
- Goal weight
- Daily allowed calorie intake

#### SingleDay
- User (Foreign key to profile)
- Calories consumed


## Schedule
#### Week 1
- Implement database
  - Create profile model
  - create single day model
- Connect routes to views for accessing data
  - create profile
  - update profile
  - delete profile
  - create single day
  - update single day
  - delete single day

#### Week 2
- Work on html templates, establish rough framework
- Begin work on styling
  - Look into using a CSS Framework

#### Week 3
- Start working on JavaScript in interact between frontend and backend
- Have a "complete" product by end of week 3

#### Week 4
- Last minute bug fixes or style changes
- Do no try to add new features