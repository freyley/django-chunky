django-chunky
=================

Editable content chunks for Django

Steps to install:

* add 'chunky' to INSTALLED_APPS
* run syncdb or migrate to get the database table
* include the urls: 
  url(r'^chunky/', include('chunky.urls')),

* include the template in the page somewhere:
   {% include "chunky_js_import.html" %}
* Load the templatetags:
   {% load chunk %}
* Use the templatetag wherever you want a chunk.
   {% chunk "editable_chunk" %}

The slug of a chunk is unique, so you can include it on multiple pages. Chunks start out with an default message, and then superusers can edit the chunks so that it says what you want it to say.

