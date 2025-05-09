from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/calendar/today', methods=['GET'])
def get_today_calendar():
    today = datetime.now().strftime('%Y-%m-%d')
    simulated_response = [
        {
            "time": "13:30",
            "event": "Non-Farm Payrolls (NFP)",
            "importance": "High",
            "currency": "USD",
            "forecast": "250K",
            "previous": "300K"
        },
        {
            "time": "15:00",
            "event": "ISM Services PMI",
            "importance": "Medium",
            "currency": "USD",
            "forecast": "54.2",
            "previous": "55.1"
        }
    ]
    return jsonify({
        "date": today,
        "events": simulated_response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
)))
