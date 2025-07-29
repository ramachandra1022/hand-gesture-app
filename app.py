from flask import Flask, render_template, Response, jsonify
from video import generate_frames, get_current_gesture, stop_streaming, start_streaming

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    start_streaming()
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/gesture')
def gesture():
    return jsonify({'gesture': get_current_gesture()})

@app.route('/stop')
def stop():
    stop_streaming()
    return jsonify({'status': 'stopped'})


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
