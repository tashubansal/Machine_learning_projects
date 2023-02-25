from flask import Flask ,render_template,request

import project as pj

app=Flask(__name__)

@app.route('/')
def hello_world():
    # if (request.method=="POST"):
    #     sepallen=request.form["sepal"]
    #     sepalwid=request.form["sepal2"]
    #     petallen=request.form["petal"]
    #     petalwid=request.form["petal2"]
        # flower_pred=pj.flower_prediction([sepalln,sepalwid,petallen,petalwid])
        # print(flower_pred)
    return render_template('index.html')

@app.route('/sub',methods=['POST'])
def submit():
    #HTML --> .py file
    if request.method=="POST":
        sepallen=request.form["sepal"]
        sepalwid=request.form["sepal2"]
        petallen=request.form["petal"]
        petalwid=request.form["petal2"]
        flower_pred=pj.flower_prediction([sepallen,sepalwid,petallen,petalwid])

    #.py to HTML file
    return render_template('sub.html' ,len1=sepallen,wid1=sepalwid,len2=petallen,wid2=petalwid,result=flower_pred)
if __name__=="__main__":
    app.run(debug=True)    