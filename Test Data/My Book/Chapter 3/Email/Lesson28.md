# Lesson 27 - Deploying Your Application to AWS with a PostgreSQL database


## Learning Objectives 

* Create a PostgreSQL database that will run your application
* Set up the database to be accessible from any IP address
* Connect the database to your Spring Boot application 

## The Walkthrough 

### Creating a PostgreSQL database: 

1. Select RDS from the AWS product list, and select "Create a database"
2. Choose the PostgreSQL option 
3. Create a production instance 
4. Select db.t2.micro from the DB instance class drop down 
5. Enter a name for the DB instance identifier. ame kit something easy to remember. (movieactordbpostgres)
6. Enter a username (movie) 
7. Enter a password movieactor 
8. Confirm the password. 
9. Enter a name to identify the database (moviedb)
10. Create a database


Click on 'View instance details' to see details about your instances.Click on "Instances", to see the instances you have running, and the status of those instances. Once the instance has been created, then you will need to change the environment variables in your Elastic Beanstalk configuration. 

Your database should now be available.

### Configuring your database for public access: 
Edit your inboud connections, so that you can access the database with any database viewer by doing the following: 
1. Open up the details for the instance you are connecting to by clicking on the identifier of the instance
2. Locate the Security Group section and click on the link that has the Type CIDR/IP Inbound 
3. Click on Actions
4. Select the option to Edit Inbound Rules 
5. Change the Source value to Custom 0.0.0.0/0 and save your settings 


### Uploading your code to AWS 

### Creating an application 

* Use an application from any of the previous lessons. 
* Include the dependency below to connect to the AWS cloud: 
<dependency>
    <groupId>postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>9.1-901.jdbc4</version>
</dependency>

### Add the following to your application.properties file: 

```
spring.datasource.url=jdbc:postgresql://aws_database_instance_endpoint:5432/postgres
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.username=your_user_name
spring.datasource.password=your_password
```

*LEAVE OUT* H2 and MySQL dependencies. 

### Package and deploy your code, and upload it to Elastic Beanstalk as indicated in Lesson 27.

Enjoy your uploaded application! 
