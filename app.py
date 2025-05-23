from flask import Flask,render_template,request,redirect,url_for,jsonify
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask</h1></html>"
@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/form',methods=['GET','POST'])
def form():
    return render_template("form.html")
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return f'hello {name}, you are {age} years old'
    return render_template("form.html")
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template("result.html",results=res,scores=score)
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp={'score':score,"res":res}
    return render_template("result1.html",results=exp)
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template("result.html",scores=score)
@app.route('/pass/<int:score>')
def pas(score):
    
    return render_template("result.html",scores=score)
@app.route('/getresult',methods=['GET','POST'])
def get_result():
    return render_template("getresults.html")
@app.route('/submit_marks',methods=['GET','POST'])
def sub_res():
    marks=0
    if request.method=='POST':
        d=float(request.form['ds'])
        c=float(request.form['cn'])
        o=float(request.form['os'])
        db=float(request.form['dbms'])
        s=float(request.form['se'])
        marks=(d+c+o+db+s)/5
    else:
        return render_template("getresults.html")
    return redirect(url_for('successres',score=marks))
items=[
    {"id":1,"name":"item 1","description":"this is item 1"},
    {"id":1,"name":"item 2","description":"this is item 2"},
]
@app.route('/todo')
def todo():
    return render_template('todo.html')
@app.route('/todo/items',methods=['GET'])
def get_items():
    return jsonify(items)
@app.route("/todo/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)
@app.route('/todo/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item={
        "id":items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']

    }
    items.append(new_item)
    return jsonify(new_item)
@app.route('/todo/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)
@app.route('/todo/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id'] != item_id]
    return jsonify({"result": "Item deleted"})
if __name__=="__main__":
    app.run(debug=True)