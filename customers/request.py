CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "email": "hannah@gmail.com"
    },
    {
      "id": 2,
      "name": "Ian Inglewood",
      "address": "7002 Chestnut Ct",
      "email": "ian@gmail.com"
    },
    {
      "id": 3,
      "name": "Janet Jackson",
      "address": "7002 Chestnut Ct",
      "email": "janet@gmail.com"
    },
    {
      "id": 4,
      "name": "Kaitlin Kelley",
      "address": "7002 Chestnut Ct",
      "email": "kaitlin@gmail.com"
    },
    {
      "email": "first@gmail.com",
      "name": "first last",
      "id": 5
    }
  ]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            return requested_customer
