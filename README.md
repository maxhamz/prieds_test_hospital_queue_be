# prieds_test_hospital_queue_be

Django backend, MongoDB server with QR generation

Project Inspiration: https://bezkoder.com/django-mongodb-crud-rest-framework/

## Running MongoDB

`sudo service mongodb start`

## Creating Superuser

`python3 manage.py createsuperuser`

## Running Server

`python3 manage.py runserver`

## Available Endpoints

### Admin

`http://localhost:8000/admin`

### Visitors

1. Register New Visitor

-  URL: `http://localhost:8000/visitors/`
-  Methods: `POST`

*  **URL Params**
   None

*  **Body/Form Params**<br>
   **Required**

   -  `strFullName` : string
   -  `dtBirth` : string (`YYYY-MM-DD`)
   -  `eGender`: string (`M`, `F`, or `X`)
   -  `strGovtId`: string (16 digits max)
   -  `strAddress`: text

*  **Success Response:**

   -  **Code:** 201 CREATED<br />
      **Content:**<br>
      `{ "id": 1, "dtRegistered": "2021-01-27T22:29:14.485612+07:00", "strFullName": "John Doe", "eGender": "X", "dtBirth": "1978-11-19", "strGovtIdNo": "311211111", "strAddress": "Gandaria" }`

*  **Error Responses:**

   -  **Code:** 400 BAD REQUEST<br />
      **Content:**<br>
      `{ "eGender": [ "\"XO\" is not a valid choice." ], "dtBirth": [ "Date has wrong format. Use one of these formats instead: YYYY-MM-DD." ], "strGovtIdNo": [ "Ensure this field has no more than 16 characters." ] }`

<hr/>

2. View Visitors

-  URL: `http://localhost:8000/visitors/`
-  Methods: `GET`

*  **URL Params**
   None

*  **Body/Form Params**<br>
   **Required**
   None

*  **Success Response:**

   -  **Code:** 200 OK<br />
      **Content:**<br>
      `[ { "id": 1, "dtRegistered": "2021-01-27T22:29:14.485000+07:00", "strFullName": "John Doe", "eGender": "X", "dtBirth": "1978-11-19", "strGovtIdNo": "311211111", "strAddress": "Gandaria" }, { "id": 2, "dtRegistered": "2021-01-27T22:30:44.166000+07:00", "strFullName": "Jack Jill", "eGender": "X", "dtBirth": "1979-11-19", "strGovtIdNo": "311211112", "strAddress": "Pondok" } ]`

<hr/>

3. Edit New Visitor

-  URL: `http://localhost:8000/visitors/<int:pk>`
-  Methods: `PUT`

*  **URL Params**
   `pk`: integer

*  **Body/Form Params**<br>
   **Required**

   -  `strFullName` : string
   -  `dtBirth` : string (`YYYY-MM-DD`)
   -  `eGender`: string (`M`, `F`, or `X`)
   -  `strGovtId`: string (16 digits max)
   -  `strAddress`: text

*  **Success Response:**

   -  **Code:** 200 OK <br />
      **Content:**<br>
      `{ "id": 1, "dtRegistered": "2021-01-27T22:29:14.485000+07:00", "strFullName": "John Doe", "eGender": "M", "dtBirth": "1978-01-01", "strGovtIdNo": "1111222233334444", "strAddress": "Gandaria" }`

*  **Error Responses:**

   -  **Code:** 400 BAD REQUEST<br />
      **Content:**<br>
      `{ "eGender": [ "\"XO\" is not a valid choice." ], "dtBirth": [ "Date has wrong format. Use one of these formats instead: YYYY-MM-DD." ], "strGovtIdNo": [ "Ensure this field has no more than 16 characters." ] }`
   -  **Code:** 404 NOT FOUND<br />
      **Content:**<br>
      None

<hr/>

4. Drop New Visitor

-  URL: `http://localhost:8000/visitors/<int:pk>`
-  Methods: `DELETE`

*  **URL Params**
   `pk`: integer

*  **Body/Form Params**<br>
   **Required**
   None

*  **Success Response:**

   -  **Code:** 204 NO CONTENT <br />
      **Content:**<br>
      None

*  **Error Responses:**
   -  **Code:** 404 NOT FOUND<br />
      **Content:**<br>
      None

