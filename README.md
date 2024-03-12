# DjangoBlogApp 

### To run the backend:

1. Clone the repository. 
	`git clone https://github.com/Lawkay1/DockerBlogApp`

2. cd into the simple_blog directory 
	`cd DockerBlogApp/simple_blog`
3. Using the sample template named envsample.txt and db_envsample.txt 
	- Create a file named .env and populate the values of your desired database credentials (based on the ensample.txt file).
	- Create another file named db.env and populate the values of your desired database credentials (based on the db_envsample.txt file). 
	**(Keep the keys consistent with what is on the sample)**

4. Build the web and database service using the docker-compose command below 
	`sudo docker-compose up --build`

5. Your services is expected to be running now and you can test the APIs based on the Postman Documentation Below

	https://documenter.getpostman.com/view/30792613/2sA2xjyAZm

6. Easy to test in the following order:
	- register 
	- login
	- get_all_blogposts
	- get_one_blogpost
	- update_blogpost
	- delete_blogposts
