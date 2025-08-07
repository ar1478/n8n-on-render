from flask import Flask, jsonify, request
from video_generator import HealingVideoGenerator

app = Flask(__name__)
generator = HealingVideoGenerator()

@app.route('/')
def home():
    return "Healing Video Generator API is running."

@app.route('/generate', methods=['POST'])
def generate_video():
    data = request.json or {}
    theme = data.get('theme', 'chakra')
    frequency = data.get('frequency', '432hz')
    duration = int(data.get('duration', 10))  # short duration for test
    
    try:
        video_path = generator.create_healing_video(theme, frequency, duration)
        return jsonify({"status": "success", "video_path": video_path})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
