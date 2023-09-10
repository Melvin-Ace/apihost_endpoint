from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # UTC time with validation with +/-2 minutes
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # JSON response
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': 'https://github.com/Melvin-Ace/apihost_endpoint/blob/main/app.py',
        'github_repo_url': 'https://github.com/Melvin-Ace/apihost_endpoint',
        'status_code': 200
    }

    return jsonify(response)