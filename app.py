# Main Application File
# username: admin
# password: adminisgood

import face_recognition.browse_video as video

from flask import Flask, render_template, request, redirect, url_for, session, Response
from auth.auth_utils import verify_admin
from database.db_utils import get_all_attendance

app = Flask(__name__)
app.secret_key = "super_secret_key_change_later"

# Login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if verify_admin(username, password):
            session["admin"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template(
                "login.html",
                error="Invalid username or password"
            )

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect(url_for("login"))

    records = get_all_attendance()

    return render_template(
        "dashboard.html",
        records=records,
    )

# Camera Control
@app.route("/start_attendance")
def start_attendance():
    if "admin" not in session:
        return redirect(url_for("login"))

    video.camera_active = True
    video.current_mode = "attendance"

    return redirect(url_for("dashboard"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if "admin" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        person_name = request.form["name"]
        return redirect(url_for("start_register", name=person_name))

    return render_template("register.html")


@app.route("/start_register/<name>")
def start_register(name):
    if "admin" not in session:
        return redirect(url_for("login"))

    video.camera_active = True
    video.current_mode = "registration"
    video.person_name = name
    video.img_count = 0
    video.frame_count = 0

    return redirect(url_for("register"))

@app.route("/stop_camera")
def stop_camera():
    video.camera_active = False
    video.current_mode = None
    video.person_name = None

    return redirect(url_for("dashboard"))

# Video Stream
@app.route("/video_feed")
def video_feed():
    if "admin" not in session:
        return redirect(url_for("login"))

    return Response(
        video.generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)