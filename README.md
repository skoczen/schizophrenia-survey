This is the repository for the Schizophrenia Survey contract work between Steven Skoczen and Informatics Experts.

![Build status](https://circleci.com/gh/skoczen/schizophrenia-survey.png?circle-token=:circle-token)

Information on how to bootstrap and deploy the project below.


Boostrapping
============

1. Clone this repo
	
	```bash
	git clone git@github.com:skoczen/schizophrenia-survey.git
	```

2. Set up the virtualenv, and `pip install fabric`

3. Bootstrap the requirements and setup a dev db.
	
	```bash
    fab refreeze
    fab setup_db
	```

4. You're set. 
	
	```bash
    ./manage.py test
	./manage.py runserver
	```


Running tests
=============

Tests are run continuously [at CircleCI](https://circleci.com/gh/skoczen/schizophrenia-survey/tree/master).  For local development, you can use the following fabric helpers.

- `fab unit` will run all unit tests
- `fab e2e` will run all browser (end-to-end) tests
- `fab wip` will run all tests marked with `@wip` (works in progress)


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

3. Add the addons

	```bash
heroku addons:add zerigo_dns:basic --app qi-schizophrenia-live
heroku addons:add memcachier --app qi-schizophrenia-live
heroku addons:add redistogo:nano --app qi-schizophrenia-live
heroku addons:add heroku-postgresql
heroku addons:add pgbackups:auto-month
heroku labs:enable user-env-compile 
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

The project is continuously deployed.

* `master` is deployed to the `qi-schizophrenia-staging` app,
* `production` is deployed to the `qi-schizophrenia-live` app, 

If you need to manually deploy, run `fab deploy`  or `fab deploy target:staging`

Note: If you haven't created the AWS bucket, simply running `./manage.py sync_static` will do it for you.


Backups
=======

Backups are done nightly via heroku's pgbackups.  Backup archives are stored in the `qi-schizophrenia-data` s3 bucket on AWS.


Documentation on manual backups and restores are found [in the pgbackups documentation](https://devcenter.heroku.com/articles/pgbackups#import-export).
