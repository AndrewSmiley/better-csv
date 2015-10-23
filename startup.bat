set PATH=%cd%/Python27;%cd%/Python27/Scripts;%cd%/Git/bin;%PATH%
pip install -r requirements.txt
git reset --hard
git pull
python manage.py runserver