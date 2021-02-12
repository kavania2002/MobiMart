![MobiMart](https://socialify.git.ci/kavania2002/MobiMart/image?description=1&descriptionEditable=MobiMart%20is%20a%20mobile%20shopping%20website.%20Very%20useful%20for%20Django%20beginner.&font=Bitter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)
<br>

## Tech Stack
- **Frontend:** HTML/CSS/Bootstrap
- **Backend:** Django

## Open Source Contests

### Cross Winter of Code (CrossWoC'21)

[![chat on discord](https://img.shields.io/badge/chat-on%20discord-brightgreen)](https://discord.gg/QugF4JAw)

CrossWoC is a six-week long opensource event organised by IEEE DTU & IEEE DTU CS, which gives programmers and innovators an opportunity to bring out their nascent talent and find intriguing solutions to real-world problems. It provides a platform for developers to dig deeper into their gray matter and bring out their latent creativity through open source.

<div>
<img src="https://crosswoc.ieeedtu.in/images/imgcw.png" alt = "CrossWoC'21"/>
</div>

## Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/kavania2002/MobiMart.git
```
- Create virtual environment-
```
python -m venv env
env\Scripts\activate
```
- Install dependencies using-
```
pip install -r requirements.txt
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 -m pip install -r requirements.txt
```

- Headover to Project Directory- 
```
cd bloggitt
```
- Make migrations using-
```
python manage.py makemigrations
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 manage.py makemigrations
```

- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Run server using-
```
python manage.py runserver
```
- Push Changes-
```
git add .
git commit -m "<your commit message>"
git push
```
<br>


# Note:

- Don't make PR directly, make issues first, once you are assigned, start working and then create a PR
- You need to add mobile phones yourself. Go to admin page in browser, add mobile phones in products according to the company.
- Don't add staticfiles, sqlite3 files while commiting.
<br>
<hr>

Have a look of the website which was before any contributions.   
https://mobimartk.herokuapp.com/
