

The application is built with flask and takes in json objects through postman. 
It stores the details of the user in the user_details dictionary and user commnets in the user_comments list 

launching the app:
			Press CTRL+B to run the app on the commandline (or go to tools > Build)
			When the app runs, take the url (http://127.0.0.1:5055/) and run it on postman.
			Change the route methods (GET, POST, DELETE, etc.) to match the defined route methods. Provide the required credentials on send the request.
			Do this for all the endpoits defined on the app 
Postman:
		To register a user on the postman, a user is required to provide a firstname, lastname, email, username and password credentials in Json format.
		To login a registered user provides username and password in Json format. An access token is generated.

Registered user should:
               		login
               		post a comment
               		view comments
               		delete comments
	

