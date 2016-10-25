Create a virtualenv with python 3.4

virtualenv -p /usr/bin/python3.4 venv

With this a virtual env gets created. Activate the virtual env

Use pip3

Install django==1.9.

pip3 install django==1.9

python manage.py migrate

python manage.py runserver

Navigate to 'http://127.0.0.1:8000/travel/'

You should see the form being loaded.

For csv uploading of file, create a .txt file with the values :

'''
https://instagram.com/, Instagrma viewer
https://github.com/kns003/, Github
'''
