# Recipe App
Django ecommerse application 

## Demo
The live site can be found [here](https://wild-dining.herokuapp.com/)

## UX
When a user lands on the site homepage, they will be greeted by a tiled grid of products that they can purchase. To add to visual appeal, these display a placeholder image. 

My goal in the design of this website was to make it obvious as to the purpose of the application and keep it simple to use. 

## Features:

**Existing Features** 

  * Mobile-first layout
  * Responsive design
  * Full-stack application
  * User input allowed
  * Data persists across user sessions
  * Editing of data allowed in-app

**Features Left to Implement**

## Technologies
* HTML
* CSS
* JavaScript
* Python (Django)
* MongoDB

## Testing

**Introduction**\
The application was tested to ensure it was fit for purpose.\
**In Scope** \
The scope of this testing was the project design and functionality.\
**Performance Testing**
* Design/Layout\
To ensure this project maintained it's desired layout the site was tested across multiple browsers (Chrome, Firefox, Microsoft Edge and Safari). 
Using browser developer tools, multiple device sizes were also tested to ensure responsiveness.

* Functionality\
Functionality of this site was tested across a variety of browsers and mobile devices to ensure essential features worked as intended.\
**Infastructure**\
The application is a full-stack application built on the frontend using using Django. 
## Deployment

This site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch.
A deployed live version of this application is available [here](https://wild-dining.herokuapp.com/)

To run locally, you can clone this repository directly into the editor of your choice by pasting 'git clone https://github.com/SeanLewisIRE/wild_dining.git'  into your terminal. 
Required packages can be installed using the included 'requirements.txt' file by typing '$pip3 install -r requirements.txt' into the terminal. Installing these packages will allow for the application to be run locally by typing 'python3 app.py'. (DB usernames and passwords required)
To cut ties with this GitHub repository, type git remote rm origin into the terminal.

## Credits

**Content**
* README layout and content inpired by Code Institute sample, available [here](https://github.com/Code-Institute-Solutions/StudentExampleProjectGradeFive)
* Django ecommerce store inspired by Code Institute code along turorial.
