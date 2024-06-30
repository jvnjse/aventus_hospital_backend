# aventus_hospital_backend

# Hospital Management Django Project Documentation

## Running the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jvnjse/aventus_hospital_backend.git
   cd aventus_hospital_backend
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

4. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Your Django application will be running at `http://127.0.0.1:8000/`.

## API Endpoints

### Base URL

All endpoints are accessible under the following base URL:

```
http://127.0.0.1:8000/api/
```

### Endpoints

#### 1. **Patients**

- **Add Patient**

  - **Method:** POST
  - **Endpoint:** `/patients/`
  - **Request Body:**

    ```json
    {
      "patient_id": "P001",
      "name": "Patient Name",
      "contact_information": "Patient Contact address",
      "medical_history": "Asthma",
      "date_of_birth": "1999-05-30",
      "gender": "Male"
    }
    ```

- **Get All Patients**

  - **Method:** GET
  - **Endpoint:** `/patients/`
  - **Request Body:** None

- **Get Single Patient**

  - **Method:** GET
  - **Endpoint:** `/patients/P001/`
  - **Request Body:**

    ```json
    {
      "patient_id": "P001",
      "name": "Patient Name",
      "contact_information": "Patient Contact address",
      "medical_history": "Asthma",
      "date_of_birth": "1999-05-30",
      "gender": "Male"
    }
    ```

- **Edit Patient**

  - **Method:** PUT
  - **Endpoint:** `/patients/P001/`
  - **Request Body:**

    ```json
    {
      "patient_id": "P001",
      "name": "Patient Name",
      "contact_information": "Patient Contact address",
      "medical_history": "Asthma",
      "date_of_birth": "1999-05-30",
      "gender": "Male"
    }
    ```

- **Delete Patient**

  - **Method:** DELETE
  - **Endpoint:** `/patients/P001/`
  - **Request Body:** None

#### 2. **Appointments**

- **Add Appointment**

  - **Method:** POST
  - **Endpoint:** `/appointments/`
  - **Request Body:**

    ```json
    {
      "patient_id": "P001",
      "doctor_name": "Dr. Smith",
      "department": "General",
      "appointment_date": "2024-07-15",
      "appointment_time": "14:00",
      "reason_for_visit": "Routine Checkup"
    }
    ```

- **Get All Appointments**

  - **Method:** GET
  - **Endpoint:** `/appointments/`
  - **Request Body:** None

- **Get Single Appointment**

  - **Method:** GET
  - **Endpoint:** `/appointments/A001/`
  - **Request Body:**

    ```json
    {
      "patient_id": "P001",
      "doctor_name": "Dr. Smith",
      "department": "General",
      "appointment_date": "2024-07-15",
      "appointment_time": "14:00",
      "reason_for_visit": "Routine Checkup"
    }
    ```

- **Edit Appointment**

  - **Method:** PUT
  - **Endpoint:** `/appointments/A002/`
  - **Request Body:**

    ```json
    {
      "appointment_id": "A002",
      "patient_id": "P001",
      "doctor_name": "Dr. Cathy edited",
      "department": "Cardiology",
      "appointment_date": "2024-07-17",
      "appointment_time": "16:30",
      "reason_for_visit": "Emergency visit"
    }
    ```

- **Delete Appointment**

  - **Method:** DELETE
  - **Endpoint:** `/appointments/A001/`
  - **Request Body:** None

#### 3. **Upload Excel File**

- **Upload Data from Excel**

  - **Method:** POST
  - **Endpoint:** `/upload/`
  - **Request Body:**

    - **Form Data:**
      - **Key:** `file`
      - **Type:** File
      - **File Path:** `/path/to/your/excel/file.xlsx`

## Postman Collection

The Postman collection file provided can be used to test the API endpoints. You can import the `aventus` collection into Postman using the following steps:

1. **Open Postman** and go to the **Import** option.
2. **Select** the `JSON` file and **Import** the `aventus` collection.
3. **Set the `base_url` Variable**:

   - Click on **Environments** in Postman.
   - Create a new environment or use an existing one.
   - Set the `base_url` variable to `http://127.0.0.1:8000/`.

4. **Run the Requests**:
   - You can now execute the various API requests as defined in the collection.

## Example Postman Requests

Here’s a brief overview of the requests included in the Postman collection:

### Add Patient

- **URL:** `{{base_url}}api/patients/`
- **Method:** POST
- **Body:** JSON with patient details

### Get All Patients

- **URL:** `{{base_url}}api/patients/`
- **Method:** GET

### Get Single Patient

- **URL:** `{{base_url}}api/patients/P001/`
- **Method:** GET

### Edit Patient

- **URL:** `{{base_url}}api/patients/P001/`
- **Method:** PUT
- **Body:** JSON with updated patient details

### Delete Patient

- **URL:** `{{base_url}}api/patients/P001/`
- **Method:** DELETE

### Add Appointment

- **URL:** `{{base_url}}api/appointments/`
- **Method:** POST
- **Body:** JSON with appointment details

### Get All Appointments

- **URL:** `{{base_url}}api/appointments/`
- **Method:** GET

### Get Single Appointment

- **URL:** `{{base_url}}api/appointments/A001/`
- **Method:** GET

### Edit Appointment

- **URL:** `{{base_url}}api/appointments/A002/`
- **Method:** PUT
- **Body:** JSON with updated appointment details

### Delete Appointment

- **URL:** `{{base_url}}api/appointments/A001/`
- **Method:** DELETE

### Upload Excel File

- **URL:** `{{base_url}}api/upload/`
- **Method:** POST
- **Body:** Form-data with a file

## Also check into the postman collection file in the folder structure
