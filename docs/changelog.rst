Change log
==========

v0.1
------

Release date:
  May 02, 2013

- Simple diary app with the following features:

  - An URL per day.
  - Each day in the diary may have several entries.
  - Entries in days will show up listed in its own day page.
  - Shows previous/next links to browse backwards/forwards only on days with actual entries.   
  - Diary management uses django's admin UI.

- Unittests to cover:

  - Setting SAMPLE_APP_REDIRECT_TO_URL_NAME is used as expected. 
  - Model's get_absolute_url
  - The two views

- Documentation about the app.
