trends_cloud
============

This trends cloud demo contains a sample django web server that is setup to use Twitter's bootstrap for html layout and jquery for fetching and rendering the trends cloud.

Install Django: 
The easiest way to get started is to get a built distribution at
https://docs.djangoproject.com/en/1.5/misc/distributions/

Setup Apache:
Some of the Django distributions come with an apache server and many operating systems come with Apache pre-installed.  If not, go to http://httpd.apache.org/download.cgi to download a copy.

Configure Apache:
In your Apache's httpd.conf, set up the port to listen to (we use 8010 for this example) and set up the proxy for your django server and for your trends backend server:

    Listen 8010
    ProxyPass /api http://localhost:8080/api/model.json
    ProxyPass / http://localhost:8000/

Restart Apache with the new configs

Once installed, run the server:
    python manage.py runserver

Visit the server through the Apache proxy:
    http://localhost:8010

