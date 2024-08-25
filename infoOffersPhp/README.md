# Microservice for View Offers

<p>
This microservice performs the action of bringing the information of the offers and taking it to a cinema platform. It has an interface where it calls this microservice through a defined URL. The microservice performs this action through an endpoint and connects to a Postgres database hosted in the cloud. 
</p>


#### How to install and run the project? :wrench:
The project requires php installed on your system. To install and run the project, follow these steps:

###### Clone the repository:

- `git clone <URL_OF_REPOSITORY>`
- `cd <URL_OF_REPOSITORY> `

###### Install dependencies:

- `composer install`

###### Execute the server:
- `php -S localhost:8080`

#### How to use the project :computer:
<p>
To use the microservice, follow the steps above to install and run the project. Once the program is running you can make use of the frontend of the cinema platform which should also run on your local machine or you can make use of the Swagger documentation available, with which it would no longer be necessary to have the frontend of the cinema platform to test this microservice.
</p>


`Frontend Cinema Platform` : <https://github.com/JaviQuilumba/CinemaPlatform.git>

#### Technologies used for this microservice
- **Php** for the backend server.
- **PostgreSQL** for the database.
- **Swagger** for API documentation.
- **Docker** for optional containerization.


###  License
This project is licensed under the (AFL-3.0) License - see the [LICENSE](https://opensource.org/license/afl-3-0-php) file for details.
