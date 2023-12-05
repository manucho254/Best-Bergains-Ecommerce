#### Best Bargains Ecommerce

- Ecommerce website that allows different vendors to sell their products on the platform


### setup project locally

###### Create a virtual environment:
    >  python3 -m venv <environment>

###### Install dependencies
    > pip install -r requirements.txt

###### Setup environment variables:

    - The environment are needed to setup the database and add the secret key
    ```
        DB_USER="" DB_PWD="" DB_HOST="" DB_NAME="" DB_PORT="" SECRET_KEY=""
    ```

##### run migrations and update db:

    - flask --app run_app db migrate -m "migration message"

    - flask --app run_app db upgrade

###### Run application:

    ``` flask -e ".env" --app run_app run --debug  ```
    - The .env should be path to your environment variables

##### Tech Stack:

``` Python3, Flask, Bootstrap, Html, Css, Javascript``` 

##### Help scripts:

    - Test the code style of 
