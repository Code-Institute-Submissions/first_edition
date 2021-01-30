# Deployment

### Heroku

I deployed my website to Heroku under the guidance of Code institutes tutorial on how to do so. I will explain this process thoroughly in these steps:

1. First, you must create a new app on [Heroku.com](https://www.heroku.com/). Login/signup for an account and then navigate to the dashboard. From here, Click on her app and give it a name 
(should ideally call it the same name as your website) and pick a region closest to you. Afterwards, click on the resources tab and then under addons type in postgres and click on the result.
You can use the free plan for the purposes of this demostration.

2. In order to use Postgres, you must install dj_database_url and psycopg2, unicorn, boto3 adn django-storeages.. Type into the console on git "pip3 install psycopg2-binary", "pip3 install dj_database_url" and
"pip3 install unicorn" and also "pip3 install boto3" and "pip3 install django-storages" . Make a requirements.txt file by typing "pip3 freeze > requirements.txt". add "storages" to installed apps in settings.py to allow django storages
to function.

3. Go back to Heroku and get your database url. It can be found in the settings tab hidden behind Config vars.
Now on gitpod, in the settings.py file, import dj_database_url. Scroll down and find the database setting (which should be marked by a comment) and comment out the orignal code.  Instead, Type the following:


```python 

DATABASES  = {
    "default": dj_database_url.parse("INSERT_POSTGRES_DATABASE_URL_HERE")

}
```

4. Since you're now connected to Postgres, you're able to Run migrations again to fill out the database. What you want to do is type into the console "Python3 manage.py migrate". Now you're able to import your product data.
Type "python3 manage.py loaddata categories" and then "python3 manage.py loaddata products" (the order is important as products depend on categories). I recommend creating a superuser now while you're still connected to Postgres
by typing "python3 manage.py createsuperuser" and then following the instructions in the console.

5.  Although not a necessary step, I recommend keeping your postgres url out of version control. You can do so by typing the following into settings.py:

```python 

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

    This will also make it so that on your local host of gitpod you also have access to a database. The DATABASE_URL value is the postgres link you applied before.

6. Create a file called "Procfile" and give it the value web: "gunicorn msp4.wsgi:application". Also, type into the console "heroku config:set DISABLE_COLLECTSTATIC=1" which will ensure Heroku wont try and collect static files When
you deploy. Now in settings.py, change the value of ALLOWED_HOSTS this:

```python 

ALLOWED_HOSTS = ["(your_heroku_app_name).herokuapp.com", "localhost"]

```

7. Go to Heroku deploy tab and in the connect to github section, type the name of the application you have saved in github, click connect and enable automatic deploy. This will make sure that every single git push will also deploy to 
heroku.

8. In the settings tab, reveal config variables and add in the values for the following variables:

| STRIPE_PUBLIC_KEY  | 
| STRIPE_SECRET_KEY  | 
| STRIPE_WH_SECRET  | 
| EMAIL_HOST_PASS  | 

To get the stripe Public and Secret key, sign into stripe and in your dashboard you'll find them under get test API keys. You need to create a webhook endpoint to get the WH_SECRET so go to the developers menu on the left hand side
of the stripe dashboard, click add endpoint in the top right, give it the url of your heroku app (you can find it ____ ) , and append "/checkout/wh" (in the case of my website), select recieve all events and then add endpoint.
The signing secret is now hidden behind a button, put this value into the heroku config vars. Email Host pass comes from your email app you created with gmail, enter the 16 digit password as its value.

9. Make sure in settings.py that all of your config variables here match the ones in settings.py. I also recommend sending a test webhook to the new endpoint to see if its functional.

### Amazon Web Services Bucket

Amazon web services is a cloud based storage service which is used to host our static and media files. I will show you how I used it to help with my deployment:

1. Go to [aws.amazon.com](https://aws.amazon.com/) and click on create AWS account in the top right. Fill out the details including your card details, you wont be chaged with a small website like this one. You must confirm your email 
and then your account will be set up.

2. Go back to the website and sign in. Now, under the my account tab, click on AWS management console. Type s3 into the searchbar and then click on s3.

3. Click create bucket, name it, select region close to you, untick block all public access, tick aclknowdge that it will be public and click on create bucket.

3. On the properities tab, click on static website hosting, use bucket to host a website, fill in the default values for index and error documents (that is, index.html and error.html) and click save.

4. On the permissions tab, click CORS configuration and paste in this and click save:

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]

5. Next in the Bucket Policy tab (still inside permissions) select policy generator. In the new tab, select the policy type S3 bucket Policy, type a star (*) into the Principal field (which will allow all principals) and for the actions tab,
scroll down to "GetObject" and tick it. For the ARN field, you want to back to Permissions/Bucket policy on a different tab/window and then copy the arn on page. Afterwards, paste the value into the field. It should have a value of something
like "arn:aws:s3:::BUCKET_NAME_HERE" . With that done, click add statement, generate policy, then copy the policy and paste it into the Buckey Policy tab where you got the ARN value. You want to add a * onto the end of the resource value just After
the forward slash but before the comma. Click save.

6. Go to access control List tab. Under Public access, click everyone and then in the pop up click list objects and then save.

### Amazon Web Services User

Users are required to access the s3 bucket you just created. I will show you how I made my user:

1. On the top navigation bar, click services and look for IAM, it will be under "Security, Identity, & compliance" or type it into the searchbar.

2. A group will be required to house ther user. On the Left hand side under access management, click groups, create new and call it whatever you want. Click next, next and then create group.

3. A policy is require dto access your bucket. So on the left hand side dashboard under Access management, click Policies, then create policy. Click import managed policy and then look for for "AmazonS4FullAccess" and then import.

4. Leave this tab open and on another tab back to S3's bucket policy page and grab the ARN again. Paste it in twice in resource and add a * at the end of the second one, it looked like this in my case:

"Resource": [
        "arn:aws:s3:::first-edition",
        "arn:aws:s3:::first-edition/*"
      ]
5. Click review policy, give it a name and description and create policy.

6. Go to groups, click on the group name you just created and then attach policy. Find the policy you made a minute ago and click attack policy.

7. Now to put a user inside this group. Under Access Management on the left hand side, click add User, give it a name (I called mine First-edition-staticfiles-user), tick programatic access and then next permissions. To add the user 
to the group, just tick the group and then next several times until you create the user.

8. You'll land on a success page saying that the user creation was successful. This page will also have a download .csv button. It's very important that you keep this file as it has the access and secret accss key thats required for
your heroku variables.


### Connecting Django to AWS

1. In settings.py, type the following code and fill in the values applicable to you:


```python 

if 'USE_AWS' in os.environ:

    AWS_STORAGE_BUCKET_NAME = # The name of the bucket you created prior
    AWS_S3_REGION_NAME = # Pick the region you used when creating your bucket, go back to S3 bucket if you forgot its value.
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') # These two are from your csv values that are retrived from your heroku config variables, we will fill them out afterwards
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = "media"

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

2. Although not required, you can add this in the if statement to improve performance by allowing the webbrowser to cache files.

```python 

AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```

3. Create a file called custom storages.py and have it filled out as so:

```python 
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

4. Add the AWS keys to your config vars on heruku under the settings tab. Remember, you get these values from the .csv file you saved earlier! Make sure they match the variable name in your settings.py file, I called them
"AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY". Also, add "USE_AWS" and set it to true! Finally, delete the "DISABLE_COLLECTSTATIC" as you will be uploading your static files through AWS now. You should do a "git add .", a commit and 
a "git push" to check if you performed these steps correctly. Your site should have its css working and next we wil work on Images.

5. Go to S3  and click create folder and call it media. Click upload and then select all your websites images (I suggest having them in one folder first to make this easier), then click next and select grant public 
read access to these objects. Keep clicking next until you get to upload and then click it.