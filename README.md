# News Aggregator (local dev)

This is a local development copy of the News Aggregator project.

How to run (PowerShell):

1. Activate the virtualenv:

   . .\mmm\Scripts\Activate.ps1

2. Run migrations (only if needed):

   python manage.py migrate

3. Start the dev server:

   python manage.py runserver

4. Open the admin interface in your browser:

   http://127.0.0.1:8000/admin/

Create a superuser (if you don't have one):

   python manage.py createsuperuser

Notes:
- The admin uses the `Article.sources` ManyToMany to show which sources an article is associated with.
- This README is minimal; expand as needed for deployment or tests.
