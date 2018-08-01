from flask import Flask, render_template, jsonify, redirect

import numpy as np
import pandas as pd
import json


app = Flask(__name__)


def read_data():
    
    import pandas as pd
    df_university = pd.read_csv("new_College.csv")
    df_university.head()
    columnName1 = list(df_university.columns)
    dictt2 = {}
    for i in columnName1:
        dictt2[i] = list(df_university[i])   
    df_standerd = pd.read_csv("median_level.csv")
    df_standerd = df_standerd.dropna()
    df_standerd.head()

    columnName = list(df_standerd.columns)
    
    dictt = {}
    for i in columnName:
        dictt[i] = list(df_standerd[i])   
    finaldict = { 'standerd' : dictt, 'college': dictt2 }

    return finaldict

def dictTranform(dict_list):
        df = pd.DataFrame(dict_list)
        names = list(df.columns)
        Outerlst = []
        for i in range(len(df)):
            innerList = []
            for j in range(len(names)):
                innerList.append(df.loc[i, names[j]])
            Outerlst.append(dict(zip(names, innerList)))
        return Outerlst



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dropdown")
def names():
    dictt = read_data()
    transformed_list = list(dictt['college'].keys())[1:]
    return jsonify(transformed_list)

@app.route("/line")
def makeline():
    dictt = read_data()
    # transformed_dictt = dictTranform(dictt['standerd'])
    return jsonify(dictt)





if __name__ == "__main__":
    app.run(debug=True)

