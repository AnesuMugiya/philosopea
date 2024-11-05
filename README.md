# Philosopea

Philosopea is a web application designed as a platform for philosophical discussions and ideas. It combines the features of a blog and an interactive learning community. Users can read, like, and comment on blog posts, and explore featured articles on various philosophical topics. The app is built using Django, Bootstrap, jQuery, AJAX, and a MySQL database for data storage.


![Screenshot 2024-11-02 001902](https://github.com/user-attachments/assets/f3aaa453-a5d9-43c2-abfa-c0b6cdb4568b)


## Features

- **Blog Posts:** Users can write, post, and share insights on philosophical topics.
- **Commenting:** Engage in thoughtful discussions by commenting on posts.
- **Likes:** Show appreciation for articles by liking them.
- **Featured Articles:** Highlighted posts on trending philosophical themes and thinkers.
- **Search:** Quickly find posts, authors, or topics with a search feature.
- **Tags:** Use tags to categorize posts and improve searchability.

## Technology Stack

- **Backend:** Django, MySQL
- **Frontend:** Bootstrap, jQuery, AJAX

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/AnesuMugiya/Philosopea.git
    cd Philosopea
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the MySQL database:**

    Set up a MySQL database and configure database settings in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'philosopea_db',
            'USER': 'your_mysql_user',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Blog Posts

- Create posts on philosophical topics, or read and engage with existing ones.
- Tag posts for easier discovery and categorization.
- Like posts to support authors and popularize content.

### Comments

- Leave thoughtful comments on blog posts to add to discussions.
- Interact with other readers' comments, creating a community of philosophical inquiry.

### Featured Articles

- Explore highlighted posts that showcase popular or trending philosophical discussions and themes.

### Search

- Use the search feature to find specific topics, authors, or discussions.
- Utilize tags to narrow down results and explore content by themes.

## Contributing

1. **Fork the repository:**

    ```sh
    git fork https://github.com/AnesuMugiya/Philosopea.git
    ```

2. **Create a new branch:**

    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m "Add your feature"
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/your-feature-name
    ```

5. **Create a Pull Request:**

    Go to the repository on GitHub and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me!

---

Thank you for exploring Philosopea!
