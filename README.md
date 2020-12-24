# dphi-deployment
Problem Statement
The director of SZE bank identified that going through the loan applications to filter the people who can be granted loans or need to be rejected is a tedious and time-consuming process. 
He wants to automate it and increase his bank’s efficiency. 
After talking around a bit, your name pops up as one of the few data scientists who can make this possible within a limited time. Will you help the director out? 

Objective
The idea behind this ML project is to build an ML model and web application that the bank can use to classify if a user can be granted a loan or not.

Requirements
- app.py - Contains the code used for building the backend with flask
- templates - Contains the html file 
- requiremnets.txt - Contains all the neccssary libraries needed to run the application 
- Procfile - This is not important if you wish to run it locally 
- .gitignore contains what must not be commited to git
- gb_model.pickle - Is the pickled model after it was trained 
- map_dict - This was used for feature engineering 
this is the final deployed application [link](https://dhpi-loan-approval.herokuapp.com/predict)

To run the application locally
- fork the repo
- run git clone with the url on your system 
- change your directory to the cloned folder 
- run pip install -r requirements.txt to install all the dependencies 
- run the application with python app.py 

Credit- ali moez [Pycaret creator](https://github.com/pycaret/pycaret-demo-dphi)
