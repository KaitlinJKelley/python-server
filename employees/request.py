from models.location import Location
import sqlite3
import json
from models import Employee

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
          e.id,
          e.name,
          e.address,
          e.location_id,
          l.name location_name,
          l.address location_address
      FROM employee e
      JOIN location l
      ON l.id = e.location_id
      """)

      employees = []

      dataset = db_cursor.fetchall()

      for row in dataset:
        # new variable
        employee = Employee(row["id"], row["name"], row["address"], row["location_id"])

        location = Location(row["id"], row["location_name"], ["location_address"])

        employee.location = location.__dict__

        employees.append(employee.__dict__)

      return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
          e.id,
          e.name,
          e.address,
          e.location_id
      FROM employee e
      WHERE e.id = ?
      """, (id,))

      data = db_cursor.fetchone()

      employee = Employee(data["id"], data["name"], data["address"], data["location_id"])

      return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):
    with sqlite3.connect("kennel.db") as conn:

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute(""" 
      SELECT
          e.id,
          e.name,
          e.address,
          e.location_id
      FROM employee e
      WHERE e.location_id = ?
      """, (location_id,))

      employees = []

      dataset = db_cursor.fetchall()

      for row in dataset:
        employee = Employee(row["id"], row["name"], row["address"], row["location_id"])

        employees.append(employee.__dict__)

    return json.dumps(employees)

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      EMPLOYEES.pop(index)

def update_employee(id, new_employee):
  with sqlite3.connect("./kennel.db") as conn:

    db_cursor = conn.cursor()

    db_cursor.execute(""" 
    UPDATE Employee
    SET
      name = ?,
      address = ?,
      location_id = ?
    WHERE id = ?
    """, (new_employee["name"], new_employee["address"], new_employee["locationId"], id,))

    rows_effected = db_cursor.rowcount

    if rows_effected == 0:
      return False
    else:
      return True