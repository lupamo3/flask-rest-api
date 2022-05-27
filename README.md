<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
-->





<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Flask Lead Creation and Customer Creation API</h3>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project

An application that allows users to create leads, create customers, view leads, edit leads, edit their customers, view customers.

.

Here are some of the features:
* Create Leads
* Create Customers
* Edit Leads
* View Users
* Edit their profiles
* It has implemented DRY principles  :smile:



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Python](https://www.python.org/)
* [PostgresQl](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
  ```sh
  
  ```

### Installation

1. Access Github [https://github.com](https://github.com)
2. Clone the repo
   ```sh
   git clone https://github.com/lupamo3/flask-rest-api.git
   ```
3. Change directory into the flask-rest-api directory :
   ```sh
   cd flask-rest-api
   ```
4. Create and activate your virtual environment :

   ```sh
   Virtual venv python=[Python-Version]
   Pip install auto-env
   ```
5. Install Project Requirements
```sh
pip install -r requirements.txt
```
6. Run the application
```sh
flask run
```

### Test the application on Postman
## Test The API end-points
 - Run [CertificateTest](https://farifu-flask.herokuapp.com/) on your postman to test the URLs

or use:

| URL                                 | METHOD                 | MESSAGE                                |
| ------------------------------------|:----------------------:| --------------------------------------:|
|/api/users/register                  | POST                   | Create a leads/customer admin.         |
|/api/users/login                     | POST                   | Login to profile.                      |
|/api/users/all                       | GET                    | Get all users                          |
|/api/users/edit                      | PUT                    | Edit Specific User  records            |
|/api/users/logout                    | POST                   | Logout of the platform                 |
|/api/leads/create                    | POST                   | Create a lead record                   |
|/api/leads/all                       | GET                    | View all leads.                        |
|/api/customer/create                 | POST                   | Create a Customer   .                  |
|/api/customer/all                    | GET                    | Get all customers                      |  




<!-- USAGE EXAMPLES -->
## Additional Information

- **Feel free to reach me via email and to fork this project**
    - Any feedback would be appreciated.
    - The Pull requests have bit by bit application documentation


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


<!-- CONTACT -->
## Contact

Your Name - [@nlanjichi](https://twitter.com/nlanjichi)

Project Link: [https://github.com/lupamo3/flask-crud/tree/master](https://github.com/lupamo3/flask-crud/tree/master)


