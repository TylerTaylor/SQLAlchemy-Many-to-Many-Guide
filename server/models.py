from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
# 4a.
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

# Steps 1-3 create the initial "has many" connection
  # You can run: 
    # `doctor.appointments`
    # `patient.appointments`
    # `appointment.doctor`
    # `appointment.patient`

# Step 4 creates the "through" connection
  # You can run:
    # `doctor.patients`
    # `patient.doctors`

# Step 5 - test in flask shell

# 1. Define your relationships

# A doctor has many appointments
# A doctor has many patients, through appointments

# A patient has many appointments
# A patient has many doctors, through appointments

# An appointment belongs to a doctor
# An appointment belongs to a patient

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

# 3a. Establish a relationship with the join table, appointments in this case
    # this allows us to call `doctor.appointments` and see the associated objects
    # back_populates sort of does the inverse, it lets the appointment know about the associated doctor object
    appointments = db.relationship('Appointment', back_populates='doctor')

# 4b. Reach THROUGH the join table
    # then grab the attribute we want to associate with this doctor (patient)
    patients = association_proxy('appointments', 'patient')

    def __repr__(self):
        return f"<Doctor Name: {self.name}>"

class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

# 3b. Establish a relationship with the join table
    # this allows us to call `patient.appointments` to see all the appointments this patient has
    appointments = db.relationship('Appointment', back_populates='patient')

# 4c. Reach THROUGH the join table
    # then grab the attribute we want to associate with this patient (doctor)
    doctors = association_proxy('appointments', 'doctor')

    def __repr__(self):
        return f"<Patient Name: {self.name}>"

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)

# 2. Give foreign keys to your join table, referring to the table(s) this object "belongs to"
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

    doctor = db.relationship('Doctor', back_populates='appointments')
    patient = db.relationship('Patient', back_populates='appointments')

    def __repr__(self):
        return f"<Appointment - Doctor Name: {self.doctor.name}, Patient Name: {self.patient.name}>"

# 5. Testing in flask shell
    # first, seed some data (feel free to add more!)
        # python seed.py
    # run `flask shell`
    # from app import app
    # from models import db, Doctor, Patient, Appointment
    # doctor = Doctor.query.first()
    # then you should be able to run:
        # (has many appointments)
            # doctor.appointments
        # (has many patients, through appointments)
            # doctor.patients
    # then try the reverse for a patient
    # exit()
