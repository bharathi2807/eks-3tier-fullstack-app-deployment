from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory user storage (just for demo)
users = []

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #0f172a, #020617);
            color: #e5e7eb;
        }
        .card {
            background: #1e293b;
            padding: 30px;
            border-radius: 12px;
            width: 350px;
            text-align: center;
            box-shadow: 0 15px 30px rgba(0,0,0,0.5);
        }
        input[type=text], input[type=password] {
            width: 90%;
            padding: 8px;
            margin: 8px 0;
            border-radius: 6px;
            border: none;
        }
        input[type=submit] {
            padding: 8px 20px;
            margin-top: 10px;
            border-radius: 6px;
            border: none;
            background: #38bdf8;
            color: #020617;
            font-weight: bold;
            cursor: pointer;
        }
        h2 { color: #38bdf8; }
        .user-list {
            margin-top: 15px;
            text-align: left;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Register User</h2>
        <form method="POST" action="/">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Register">
        </form>
        {% if users %}
            <div class="user-list">
                <h4>Registered Users:</h4>
                <ul>
                {% for user in users %}
                    <li>{{ user['username'] }}</li>
                {% endfor %}
                </ul>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.append({"username": username, "password": password})
        return redirect(url_for("register"))
    return render_template_string(HTML_FORM, users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)