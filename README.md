This is the repository for the Schizophrenia Survey contract work between Steven Skoczen and Informatics Experts.

Information on how to bootstrap and deploy the project below.


Boostrapping
============

1. Clone this repo
	
	```bash
	git clone git@github.com:skoczen/schizophrenia-survey.git
	```

2. Set up the your virtualenv, and `pip install fabric`

3. Set up your remotes manually, or by use the fab helper command.
	
	```bash
	fab initial_setup
	```

4. You're set. 
	
	```bash
	cd project
	./manage.py runserver
	```



Deploying to Heroku, with AWS for static media
==============================================

Preparing
---------


1. Install the gem, if you don't already have it

	```gem install heroku```

2. Authenticate

	```heroku login```

3. Create the app
	
	```bash
	heroku create --stack cedar mynewproject
	```

3. I use this set of addons in almost every project

	```bash
heroku addons:add zerigo_dns:basic --app qi-schizophrenia-live
heroku addons:add memcachier --app qi-schizophrenia-live
heroku addons:add redistogo:nano --app qi-schizophrenia-live
heroku addons:add heroku-postgresql
	```

4. Set up your domains

	```bash
	heroku domains:add www.mydomain.com
	heroku domains:add mydomain.com
	```

5. Set your keys

	* If you have a private repo, you can set the keys directly in `keys_and_passwords.py`.
	* If you have a public repo:
		* You're best off setting them as environment variables in your deployment environment.  
			```bash
			heroku config:add AWS_ACCESS_KEY_ID=foo-bar-1
			```
		* For local usage, set the keys in `keys_and_passwords_private.py`

	Keys you're likely want to set:
		```bash
		heroku config:add AWS_ACCESS_KEY_ID=foo`
		heroku config:add AWS_SECRET_ACCESS_KEY=bar
		heroku config:add AWS_STORAGE_BUCKET_NAME=myproject
		heroku config:add DB_PASSWORD=pass1234
		# analytics settings.
		```
	

Deploying
---------

* `fab deploy`

Note: If you haven't created the AWS bucket, simply running `./manage.py sync_static` will do it for you.