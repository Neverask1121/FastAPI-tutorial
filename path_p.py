from fastapi import FastAPI


app = FastAPI()


customer_name_gross_item = [
    101: {"name": "Aditya Bhandari", "gross": 100, "item": "biscuit"},
    102: {"name": "Adit Bhandari", "gross": 100, "item": "biscuit"},
    103: {"name": "Bhandari", "gross": 100, "item": "biscuit"},
]


@app.get("/customer/{customer_id}")
def Customer_id_funciton(customer_id: int):

    if customer_id not in customer_name_gross_item:
        return {
            "status": "not found"
        }

    profile = customer_name_gross_item[customer_id]

    return {
        "customer_id": customer_id,
        "customer_name": profile["name"],
        "customer_gross": profile["gross"],
        "customer_item": profile["item"]
    }