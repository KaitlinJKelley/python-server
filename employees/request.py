EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Kendal Crabtree",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Luke Darden",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Mitch Eglin",
      "locationId": 1
    },
    {
      "name": "Lucy",
      "locationId": 2,
      "id": 5
    }
  ]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
            return requested_employee

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
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      EMPLOYEES[index] = new_employee