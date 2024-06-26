# TeamCollab REST API

REST API providing basic functionality for managing user profiles

### Prerequisites

- Python 3.8 or higher
- MySQL(updated version)
- Git

### Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-directory>

```

2.  Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate

```

3.  Install the dependencies:

```bash
pip install -r requirements.txt


```

4.  Set up the environment variables:

```bash

Create a .env file in the root of your project and add the necessary environment variables. Example:

env
Copy code
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306


```

5.  Apply the migrations:

```bash

python manage.py migrate

```

6.  Create a superuser:

```bash
python manage.py createsuperuser


```

7.  Run the development server:

```bash

python manage.py runserver
```
