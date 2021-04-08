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

