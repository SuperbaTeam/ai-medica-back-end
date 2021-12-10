## Vision

* What is the vision of this product?

Our project aims to provide the users an online checkup service for a selection of diseases such as Hepatitis and Heart Stroke.


* What pain point does this project solve?

Make it easier for users to checkup on their health anywhere, anytime without paying a visit to doctors.

* Why should we care about your product?

Our product is going to save time and money for users by providing an initial medical test using a well trained machine learning model that depends on a global scientific data set.

## Scope

### IN

* Users can create their own profiles that will contain their information and results history.

* Users are able to choose one of the diseases, answer few questions and get their checkup result.

* Users can help us in collecting data for a special disease by submiting their personal data if they chooose so.

* Users are going to be presented with awareness information when they visit the web app.


### OUT

* This web app is never going to be paid.

## Minimum Viable Product 

- We expect to provide a useful experince for users with multiple things to do in our application as the following:

* First: the user can select one of the diseases and a rendered form will appear to collect the data from the user and predict the status of the user's disease.

* Second: the user can help us in collecting data for a specific disease using a special API.

* Third: the user can see an enhnancment user control panel showing their medical tests with their results and some features such as deleting and priting the test results.

## Stretch

* Making this web app also a mobile app.

## Functional Requirements

* A user can create their own profile.
* A user can manage their results in the results page.
* A user can print a test result.
* A user can contribute to disease research by providing some information.


## Data Flow

### Disease Discovery Service.

When the user logs in, home page appears and the discover page button will appear in the header, then the user can visit the discover page and choose a disease then submit the related information regarding that disease and then the data is going to be sent to the backend API in order for it to be analyzed with a well trained machine learning model, and after that the data will be processed and stored in the database, including the disease discovery state.

At this point, we can fetch the data from the database and render it in the frontend results page so that the user can view it.

### Help Others Service.

A service that can be accessed without the need of logging-in, the user can enter help others page and fill the form regarding the specific disease, and when the user submits the data, the data is going to be directly sent to an non-authorized API.

## Non-functional requirements 

### **Security**

The data is secure and only the registered user who can see their results.

### **Extendablilty**

Our web app is easily extendable as it can add more diseases to be discovered.