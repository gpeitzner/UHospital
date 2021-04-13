import objects
from flask import Flask, request, jsonify
app = Flask(__name__)

users = []
medicines = []


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    date = data["date"]
    gender = data["gender"]
    nickname = data["nickname"]
    password = data["password"]
    phone = data["phone"]
    valid_user = True
    for user in users:
        if user.nickname == nickname:
            valid_user = False
    if valid_user:
        users.append(objects.User(first_name, last_name,
                                  date, gender, nickname, password, phone))
        return jsonify(request.get_json()), 200
    else:
        return jsonify({"message": "nickname repeated"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for user in users:
        if user.nickname == nickname:
            if user.password == password:
                return jsonify({
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date": user.date,
                    "gender": user.gender,
                    "nickname": user.nickname,
                    "password": user.password,
                    "phone": user.password
                }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    return jsonify({"message": "bad credentials"}), 400


@app.route("/medicine", methods=["GET", "POST", "PUT", "DELETE"])
def medicine():
    if request.method == "GET":
        tmp = []
        for medicine in medicines:
            tmp.append({"name": medicine.name, "price": medicine.price,
                       "description": medicine.description, "quantity": medicine.quantity})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        quantity = data["quantity"]
        valid_medicine = True
        for medicine in medicines:
            if medicine.name == name:
                valid_medicine = False
        if valid_medicine:
            medicines.append(objects.Medicine(
                name, price, description, quantity))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "medicine repeated"}), 400
    elif request.method == "PUT":
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        quantity = data["quantity"]
        for medicine in medicines:
            if medicine.name == name:
                medicine.price = price
                medicine.description = description
                medicine.quantity = quantity
        return jsonify({"message": "medicine edited"}), 200
    elif request.method == "DELETE":
        name = request.args.get("name")
        for medicine in medicines:
            if medicine.name == name:
                medicines.remove(medicine)
        return jsonify({"message": "medicine deleted"}), 200
