from flask import Flask, request, jsonify

app = Flask(__name__)

# Bộ nhớ tạm để lưu bài tập
assignments = []

@app.route('/create_assignment', methods=['POST'])
def create_assignment():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    deadline = data.get('deadline')

    assignment = {
        'title': title,
        'description': description,
        'deadline': deadline
    }

    assignments.append(assignment)
    return jsonify({'message': 'Assignment created successfully!', 'assignment': assignment})

@app.route('/assignments', methods=['GET'])
def get_assignments():
    return jsonify(assignments)

if __name__ == '__main__':
    app.run(debug=True)
