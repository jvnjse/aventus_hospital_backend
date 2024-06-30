from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, Appointment
from .serializers import PatientSerializer, AppointmentSerializer
import pandas as pd
from datetime import datetime


@api_view(["GET", "POST"])
def patients_list(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def appointments_list(request):
    if request.method == "GET":
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def upload_excel(request):
    if request.method == "POST":
        file = request.FILES["file"]

        try:
            if file.name.endswith(".xlsx"):
                excel_data = pd.read_excel(file, sheet_name=None)
            elif file.name.endswith(".csv"):
                excel_data = {
                    "Patients": pd.read_csv(file, sheet_name="Patients"),
                    "Appointments": pd.read_csv(file, sheet_name="Appointments"),
                }
            else:
                return Response(
                    {"error": "Invalid file format"}, status=status.HTTP_400_BAD_REQUEST
                )

            patients_data = excel_data.get("Patients")
            appointments_data = excel_data.get("Appointments")

            if patients_data is not None:
                patient_objects = []
                for _, row in patients_data.iterrows():
                    patient_objects.append(
                        Patient(
                            patient_id=row["Patient ID"],
                            name=row["Patient Name"],
                            contact_information=row["Contact Information"],
                            medical_history=row["Medical History"],
                            date_of_birth=row["Date of Birth"],
                            gender=row["Gender"],
                        )
                    )
                Patient.objects.bulk_create(patient_objects, ignore_conflicts=True)

            if appointments_data is not None:
                appointment_objects = []
                for _, row in appointments_data.iterrows():
                    try:
                        patient = Patient.objects.get(patient_id=row["Patient ID"])

                        appointment_time = None
                        time_formats = ["%I:%M %p", "%H:%M"]
                        for time_format in time_formats:
                            try:
                                appointment_time = datetime.strptime(
                                    row["Appointment Time"], time_format
                                ).time()
                                break
                            except ValueError:
                                continue

                        if appointment_time is None:
                            raise ValueError(
                                f"Invalid time format for {row['Appointment Time']}"
                            )

                        appointment_objects.append(
                            Appointment(
                                appointment_id=row["Appointment ID"],
                                patient=patient,
                                doctor_name=row["Doctor Name"],
                                department=row["Department"],
                                appointment_date=row["Appointment Date"],
                                appointment_time=appointment_time,
                                reason_for_visit=row["Reason for Visit"],
                            )
                        )
                    except Exception as e:
                        print(f"Error processing appointment row {row}: {str(e)}")

                Appointment.objects.bulk_create(
                    appointment_objects, ignore_conflicts=True
                )

            return Response(
                {"success": "Data uploaded successfully"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
