from flask import Flask,jsonify,request
app = Flask(__name__)

contacts=[
    {
        'id':1,
        'contact':u'99999 88888',
        'name':u'Vedant',
        'done':False
    },
    {
        'id':2,
        'contact':u'77777 66666',
        'name':u'Aarush',
        'done':False
    }
]


@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message": "Please provide the data"
        },400)

    contact = {
            'id':contacts[-1]['id']+1,
            'contact':request.json['contact'],
            'name':request.json.get('name',""),
            'done':False
        }

    contacts.append(contact)
    return jsonify({
        "status" : "success",
        "message": "contact number added successfully"
    })

@app.route("/get-data")
def get_contacts():
    return jsonify({
        "data":contacts
    })


if(__name__ == "__main__"):
    app.run(debug=True)