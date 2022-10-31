
from flask import Flask,jsonify,request,render_template
from models.utils import OutletSales

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return "WELCOME"
    
@app.route('/test')
def student():

    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get_predict_charges():

    if request.method == 'POST':

        result = request.form
        Item_Weight = result["Item Weight"]
        Item_Fat_Content = result["Item Fat Content"]
        Item_Visibility = result["Item Visibility"]
        Item_Type = result["Item Type"]
        Item_MRP = result["Item MRP"]
        Outlet_Identifier = result["Outlet Identifier"]
        Outlet_Establishment_Year = result["Outlet Establishment Year"]
        Outlet_Size = result["Outlet Size"]
        Outlet_Location_Type = result["Outlet Location Type"]
        Outlet_Type = result["Outlet Type"]


        object = OutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Item_Type,Outlet_Identifier)
        charges = object.get_predict_charges()

        return render_template("output.html", charges = charges)

    
    
if __name__ == "__main__":
    app.run()