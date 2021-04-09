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

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
