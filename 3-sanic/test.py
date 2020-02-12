from sanic import Sanic
from sanic.response import html,text,json

app = Sanic()

@app.route("/")
def test(request):
    return text("hello world")

if __name__=="__main__":
    app.run(port=80)
