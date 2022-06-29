from flask import Flask, render_template, url_for
from flask import request as req

import json
import requests

app = Flask(__name__ )


@app.route('/', methods=['GET', 'POST'])
def Index():
       
    return render_template('index.html')

@app.route('/Summary', methods=['GET', 'POST'])
def Summary():

    if req.method == 'POST':
        headers = {"Authorization": f"Bearer {'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'}"}
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        data= req.form['data']
        maxL= int(req.form["maxL"])
        minL= maxL//4
        print(maxL)
        def query(payload):
           
            response = requests.post(API_URL, headers=headers, json=payload)
            return json.loads(response.content.decode("utf-8"))
            



        
        output = query(
          {
             "inputs": data,
             "parameters":{"min_length": minL, "max_length": maxL},
          }
        )[0]

        return render_template('index.html', result=output['summary_text'])

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)