import requests
from xml.etree import ElementTree as ET
from flask import Flask
from flask import jsonify
from flask import Flask, redirect
app = Flask(__name__)

@app.route("/gbp")
def gbp1():
    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    gbprate=subsubchild.attrib['rate']    

    return jsonify (gbprate), 200

@app.route("/cad")
def cad1():
    
    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    cadrate=subsubchild.attrib['rate']        

    return jsonify (cadrate), 200

@app.route("/jpy")
def jpy1():
    
    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    jpyrate=subsubchild.attrib['rate']        

    return jsonify (jpyrate), 200

@app.route("/gbp/<float:usdtogbp>")
def gbp(usdtogbp):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'GBP':
                    gbprate=subsubchild.attrib['rate']  

    gbptousd = float(usdtogbp) * float(gbprate)
    usdoutput = str(round(gbptousd,2))        

    return jsonify (usdoutput), 200

@app.route("/cad/<float:usdtocad>")
def cad(usdtocad):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'CAD':
                    cadrate=subsubchild.attrib['rate']

    cadtousd = float(usdtocad) * float(cadrate)
    cadoutput = str(round(cadtousd,2))        

#    print(cadoutput)
    return jsonify (cadoutput), 200 

@app.route("/jpy/<float:usdtojpy>")
def jpy(usdtojpy):

    r = requests.get('http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml', stream=True)
    tree = ET.parse(r.raw)
    root = tree.getroot()
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                if subsubchild.attrib['currency'] == 'JPY':
                    jpyrate=subsubchild.attrib['rate']  

    jpytousd = float(usdtojpy) * float(jpyrate)
    jpyoutput = str(round(jpytousd,2))        

#    print(jpyoutput)
    return jsonify (jpyoutput), 200 

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

