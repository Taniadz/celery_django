from flask import Flask, Response
app = Flask(__name__)

@app.route('/send_data')
def index():
    data = """
            <countries>
            <country>
                <name>Ukraine</name>
                <id>123456</id>
            </country>
            <country>
                <name>Poland</name>
                <id>789012</id>
            </country>
        </countries>
        """

    return Response(data, mimetype='text/xml')



app.run(port = 5000, debug = True)
