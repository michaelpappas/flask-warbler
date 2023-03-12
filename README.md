
# RESTful API Flask

A RESTful twitter clone API using Flask and Postgresql

## Manual Installation

Clone the repo:

```bash
git clone https://github.com/michaelpappas/flask-warbler
cd flask-warbler
```

Set the environment variables:
```bash
touch .env
# open .env and modify the environment variables
```
or
```bash
cp .env.example .env
# open .env and modify the environment variables
```


## Table of Contents

- [Dev Environment](#dev-environment)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)

Development Environment Setup
## Dev-environment

You'll need Python3 and PostgreSQL

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
```

Create warbler database in psql with:
```sql
CREATE DATABASE warbler
```

To run the backend run:
```bash
flask run -p 5000
```

## Project Structure

```
\                           # Root folder
 |--app.py                  # main routes scripts
 |--forms.py                # WTForms classes
 |--models.py               # database models and methods
 |--seed.py                 # scripts for seeding db with generator data
 |--readme.md               # project readme
 |--requirements.txt        # dependencies
 |--test_messages_model.py  # messages model tests
 |--test_messages_views.py  # messages views tests
 |--test_user_model.py      # user model tests
 |--test_user_views.py      # user views tests

 \generator                 # Generator folder to seed db
 |--create_csvs.py          # generates random user profiles
 |--follows.csv             # follows csv file
 |--helpers.py              # helper functions for seed data creation
 |--messages.csv            # messages csv file
 |--users.csv               # users csv file

 \static                    # static files folder
 |--/images                 # images folder
 |--/stylesheets            # stylesheets folder
 |--/templates              # jinja templates folder
 |--favicon.ico             # warbler favicon
 |--warbler_ftnality.js     # likes icon toggling logic
```

### API Endpoints

List of available routes:

**Auth/Signup routes**:\
`GET /signup` - renders user signup form\
`POST /signup` - posts user signup form\
`GET /login` - renders user login form\
`POST /login` - posts user login form\
`POST /logout` - user logout request\

**Home routes**:\
`GET /` - renders homepage w/ messages if logged in or anon homepage if not\


**User routes**:\
`GET /users` - gets all users with optional username filter(login required)\
`GET /users/:user_id` - gets user with user_id URL param(login required)\
`GET /users/:user_id/following` - gets user followers(login required)\
`POST /users/follow/:follow_id` - sets current user to follow follow_id(login required)\
`POST /users/stop-following/:follow_id` - removes current user following follow_id(login required)\
`GET /users/profile` - renders edit profile form(login required)\
`POST /users/profile` - posts edit profile form(login required)\
`GET /users/changepwd` - renders edit password form(login required)\
`POST /users/changepwd` - posts edit password form(login required)\
`GET /users/:user_id/likes` - gets users liked messages(login required)\
`POST /users/delete` - delets user account(login required)\

**Message routes**:\
`GET /messages/new` - renders new message form(login required)\
`POST /messages/new` - posts new message form(login required)\
`GET /messages/:message_id` - gets a single message(login required)\
`POST /messages/:message_id/delete` - deletes message(login required)\
`POST /messages/:message_id/like` - likes message(login required)\





