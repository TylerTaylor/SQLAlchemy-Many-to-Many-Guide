from app import app
from models import db, Doctor, Patient, Appointment

with app.app_context():
    # Set up your seed data here

    Doctor.query.delete()
    Patient.query.delete()
    Appointment.query.delete()
    
    d1 = Doctor(name="Who")
    db.session.add(d1)
    db.session.commit()

    p1 = Patient(name="John")
    db.session.add(p1)
    db.session.commit()

    a1 = Appointment(doctor_id=d1.id, patient_id=p1.id)
    db.session.add(a1)
    db.session.commit()

    print("seeded!")
