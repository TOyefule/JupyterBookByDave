# Lesson 27 - Deploying Your Application to AWS with an in-memory database


## Learning Objectives 

* Compile an executable .jar file 
* Create a Java application server with Elastic Beanstalk 
* Upload your code to AWS 
* Configure the server to run your application 

## The Walkthrough 

1.  Start with any application with an H2 database from any previous lesson 
	Make sure the server port is set to 5000

2. Compile your application into .jar file: 

	* Open up the main project folder in the terminal. 
	
	* Type: 
	```ShellSession 
		mvnw package 
	```
	Your executable .jar file will be created in the target folder.

If you are having trouble running the mvnw command, these links  should help: 

Install maven

```
https://www.mkyong.com/maven/how-to-install-maven-in-windows/
https://www.mkyong.com/maven/install-maven-on-mac-osx/
https://www.mkyong.com/maven/how-to-install-maven-in-ubuntu/
** Do not forget to add it to your PATH variables! **

```

2. Create an AWS account 
   If you don't already have one, create an AWS account.

3. Log in to the AWS console 

4. Create an Elastic Beanstalk application - search for Elastic Beanstalk and select that product

You should see a screen welcoming you to the Elastic Beanstalk application. 
Click the Get Started Button. 

5. Enter the name of your application 

6. Choose the 'Java' platform from the drop down 

7. Select the 'Upload your application' option 

8. Choose the local file as a source 

9. Select your .jar file from the target folder and upload it. 

10. You will see a red exclamation mark indicating your application is not healthy. 
Change this immediately bu updating the application's configuration settings. 

To do this: 
* Select Configuration from the side menu. 
* Choose the 'Software' option 
* Include a SERVER_PORT variable, and set the value to 5000
* Apply your changes 

11. Go back to the main page for your Elastic Beanstalk application, and click on the URL. This should display your application. 

## What's Going On 

Youur application is being deployed to a cloud-based server on Amazon Web Services. The steps you are going through are: 

1. Packaging your application into an executable .jar that can be run directly on a pre-configured server (with a port set to 5000)

2. Creating a pre-configured server that can run Java 8 applications on Amazon Web Services (using Elastic Beanstalk)

3. Uploading the .jar file to your AWS server 

4. Changing the default port setting in the configuration to 5000 

5. Running your application on AWS using the provided URL. 

Enjoy your uploaded application! 
