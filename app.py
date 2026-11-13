from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from predictor import run_prediction
import pdfkit

app = Flask(__name__)
app.secret_key = "secret123"

# ================= MongoDB Connection =================
client = MongoClient("mongodb://localhost:27017/")
db = client["healthanlyserdb"]
users_collection = db["users"]


# ================= HOME =================
@app.route('/')
def index():
    return render_template('index.html')


# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():

    if "user_email" not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')


# ================= SIGNUP =================
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for('signup'))

        if users_collection.find_one({"email": email}):
            flash("Email already registered", "error")
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)

        users_collection.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "password": hashed_password
        })

        flash("Signup successful", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')


# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = users_collection.find_one({"email": email})

        if user and check_password_hash(user['password'], password):

            session["user_email"] = email
            flash("Login successful", "success")
            return redirect(url_for('dashboard'))

        else:
            flash("Invalid credentials", "error")
            return redirect(url_for('login'))

    return render_template('login.html')


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ================= PROFILE =================
@app.route("/profile")
def profile():

    if "user_email" not in session:
        return redirect("/login")

    user = users_collection.find_one(
        {"email": session["user_email"]}
    )

    return render_template("profile.html", user=user)


# ================= EDIT PROFILE =================
@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():

    if "user_email" not in session:
        return redirect("/login")

    user = users_collection.find_one(
        {"email": session["user_email"]}
    )

    if request.method == "POST":

        phone = request.form.get("phone")
        age = request.form.get("age")
        gender = request.form.get("gender")
        height = request.form.get("height")
        weight = request.form.get("weight")
        bmi = request.form.get("bmi")

        users_collection.update_one(
            {"email": session["user_email"]},
            {
                "$set": {
                    "phone": phone,
                    "age": age,
                    "gender": gender,
                    "height": height,
                    "weight": weight,
                    "bmi": bmi
                }
            }
        )

        flash("Profile Updated Successfully", "success")
        return redirect("/profile")

    return render_template("edit_profile.html", user=user)


# ================= PREDICT STEPS =================
@app.route("/predict")
def step1():
    return render_template("predict_step1.html")


@app.route("/predict/step2")
def step2():
    return render_template("predict_step2.html")


@app.route("/predict/step3")
def step3():
    return render_template("predict_step3.html")


@app.route("/predict/step4")
def step4():
    return render_template("predict_step4.html")


# ================= SAVE PERSONAL INFO =================
@app.route("/save_personal_info", methods=["POST"])
def save_personal_info():

    if "user_email" not in session:
        return redirect("/login")

    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    height = request.form.get("height")
    weight = request.form.get("weight")
    bmi = request.form.get("bmi")

    session["personal_info"] = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "bmi": bmi
    }

    users_collection.update_one(
        {"email": session["user_email"]},
        {
            "$set": {
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "bmi": bmi
            }
        }
    )

    return redirect("/predict/step2")


# ================= SAVE LIFESTYLE INFO =================
@app.route("/save_lifestyle_info", methods=["POST"])
def save_lifestyle_info():

    session["lifestyle_info"] = {
        "smoking": request.form.get("smoking"),
        "alcohol": request.form.get("alcohol"),
        "activity": request.form.get("activity"),
        "activity_type": request.form.get("activity_type"),
        "sleep": request.form.get("sleep"),
        "stress": request.form.get("stress")
    }

    return redirect("/predict/step3")


# ================= SAVE MEDICAL HISTORY =================
@app.route("/save_medical_history", methods=["POST"])
def save_medical_history():

    session["medical_history"] = {
        "family_history": request.form.get("family_history"),
        "diabetes": request.form.get("diabetes"),
        "sugar_level": request.form.get("sugar_level"),
        "bp": request.form.get("bp"),
        "systolic": request.form.get("systolic"),
        "diastolic": request.form.get("diastolic"),
        "heart": request.form.get("heart"),
        "heart_type": request.form.get("heart_type"),
        "heart_rate": request.form.get("heart_rate"),
        "cholesterol": request.form.get("cholesterol"),
        "breath": request.form.get("breath"),
        "surgery": request.form.get("surgery"),
        "medication": request.form.get("medication"),
        "allergy": request.form.get("allergy")
    }

    return redirect("/predict/step4")


# ================= SYMPTOMS FLOW =================
# ================= SYMPTOMS FLOW =================

@app.route("/symptoms/general", methods=["GET", "POST"])
def symptoms_general():

    if request.method == "POST":

        session.pop('general', None)
        session.pop('skin', None)
        session.pop('respiratory', None)
        session.pop('neuro', None)
        session.pop('musculo', None)
        session.pop('digestive', None)
        session.pop('heart', None)
        session.pop('urinary', None)

        session['general'] = request.form.getlist("symptoms")
        return redirect("/symptoms/skin")

    return render_template("symptoms/symptoms_general.html")


@app.route("/symptoms/skin", methods=["GET", "POST"])
def symptoms_skin():

    if request.method == "POST":
        session['skin'] = request.form.getlist("symptoms")
        return redirect("/symptoms/respiratory")

    return render_template("symptoms/symptoms_skin.html")


@app.route("/symptoms/respiratory", methods=["GET", "POST"])
def symptoms_respiratory():

    if request.method == "POST":
        session['respiratory'] = request.form.getlist("symptoms")
        return redirect("/symptoms/neuro")

    return render_template("symptoms/symptoms_respiratory.html")


@app.route("/symptoms/neuro", methods=["GET", "POST"])
def symptoms_neuro():

    if request.method == "POST":
        session['neuro'] = request.form.getlist("symptoms")
        return redirect("/symptoms/musculoskeletal")

    return render_template("symptoms/symptoms_neuro.html")


@app.route("/symptoms/musculoskeletal", methods=["GET", "POST"])
def symptoms_musculoskeletal():

    if request.method == "POST":
        session['musculo'] = request.form.getlist("symptoms")
        return redirect("/symptoms/digestive")

    return render_template("symptoms/symptoms_musculoskeletal.html")


@app.route("/symptoms/digestive", methods=["GET", "POST"])
def symptoms_digestive():

    if request.method == "POST":
        session['digestive'] = request.form.getlist("symptoms")
        return redirect("/symptoms/heart")

    return render_template("symptoms/symptoms_digestive.html")


@app.route("/symptoms/heart", methods=["GET", "POST"])
def symptoms_heart():

    if request.method == "POST":
        session['heart'] = request.form.getlist("symptoms")
        return redirect("/symptoms/urinary")

    return render_template("symptoms/symptoms_heart.html")


@app.route("/symptoms/urinary", methods=["GET", "POST"])
def symptoms_urinary():

    if request.method == "POST":
        session['urinary'] = request.form.getlist("symptoms")
        return redirect("/report")

    return render_template("symptoms/symptoms_urinary.html")

# ================= REPORT =================
@app.route("/report")
def report():

    final_symptoms = (
        session.get("general", []) +
        session.get("skin", []) +
        session.get("respiratory", []) +
        session.get("neuro", []) +
        session.get("musculo", []) +
        session.get("digestive", []) +
        session.get("heart", []) +
        session.get("urinary", [])
    )

    final_symptoms = list(set(final_symptoms))

    if len(final_symptoms) == 0:
        flash("Please select symptoms", "error")
        return redirect("/symptoms/general")

    result = run_prediction(final_symptoms)

    session["last_report"] = {
        "disease": result["disease"],
        "confidence": result["confidence"],
        "risk": result["risk"],
        "advice": result["advice"],
        "symptoms": final_symptoms
    }

    session.pop('general', None)
    session.pop('skin', None)
    session.pop('respiratory', None)
    session.pop('neuro', None)
    session.pop('musculo', None)
    session.pop('digestive', None)
    session.pop('heart', None)
    session.pop('urinary', None)

    return render_template(
        "report.html",
        disease=result["disease"],
        confidence=result["confidence"],
        risk=result["risk"],
        advice=result["advice"],
        symptoms=final_symptoms
    )
def get_health_plan(disease):

    plans = {

        "Diabetes": {
            "routine": [
                "Wake up early and walk 30 minutes",
                "Monitor blood sugar regularly",
                "Avoid stress and get proper sleep"
            ],
            "diet": [
                "Low sugar foods",
                "Whole grains",
                "Green vegetables",
                "Avoid sweets and junk food"
            ],
            "exercise": [
                "Walking",
                "Yoga",
                "Light cardio"
            ]
        },

        "Heart Disease": {
            "routine": [
                "Daily morning walk",
                "Avoid stress",
                "Regular doctor checkups"
            ],
            "diet": [
                "Low salt diet",
                "Fruits and vegetables",
                "Avoid oily food"
            ],
            "exercise": [
                "Walking",
                "Breathing exercises",
                "Light jogging"
            ]
        },

        "Common Cold": {
            "routine": [
                "Take proper rest",
                "Stay hydrated"
            ],
            "diet": [
                "Warm fluids",
                "Soup",
                "Fruits rich in vitamin C"
            ],
            "exercise": [
                "Light stretching"
            ]
        }

    }

    # Default plan if disease not found
    return plans.get(disease, {
        "routine": ["Maintain healthy daily routine"],
        "diet": ["Balanced diet"],
        "exercise": ["Regular exercise"]
    })
@app.route("/recommendations")
def recommendations():

    if "last_report" not in session:
        flash("No report available", "error")
        return redirect("/dashboard")

    report = session["last_report"]
    plan = get_health_plan(report["disease"])

    return render_template(
        "recommendations.html",
        report=report,
        routine=plan["routine"],
        diet=plan["diet"],
        exercise=plan["exercise"]
    )
@app.route("/routine")
def routine_page():
    if "last_report" not in session:
        return redirect("/dashboard")

    plan = get_health_plan(session["last_report"]["disease"])
    return render_template("routine.html", routine=plan["routine"])


@app.route("/diet")
def diet_page():
    if "last_report" not in session:
        return redirect("/dashboard")

    plan = get_health_plan(session["last_report"]["disease"])
    return render_template("diet.html", diet=plan["diet"])
@app.route('/diet')
def diet():
    return render_template('diet.html')

@app.route('/diet_skin')
def diet_skin():
    return render_template('diet_skin.html')

@app.route('/diet_respiratory')
def diet_respiratory():
    return render_template('diet_respiratory.html')

@app.route('/diet_heart')
def diet_heart():
    return render_template('diet_heart.html')

@app.route('/diet_neuro')
def diet_neuro():
    return render_template('diet_neuro.html')

@app.route('/diet_musculo')
def diet_musculo():
    return render_template('diet_musculo.html')

@app.route('/diet_digestive')
def diet_digestive():
    return render_template('diet_digestive.html')

@app.route('/diet_kidney')
def diet_kidney():
    return render_template('diet_kidney.html')


@app.route("/exercise")
def exercise_page():
    if "last_report" not in session:
        return redirect("/dashboard")

    plan = get_health_plan(session["last_report"]["disease"])
    return render_template("exercise.html", exercise=plan["exercise"])
# ================= DOWNLOAD REPORT =================
@app.route("/download_report")
def download_report():

    if "last_report" not in session:
        flash("No report found", "error")
        return redirect("/dashboard")

    report = session["last_report"]
    personal = session.get("personal_info", {})
    lifestyle = session.get("lifestyle_info", {})
    history = session.get("medical_history", {})

    rendered = render_template(
        "pdf_report.html",
        report=report,
        personal=personal,
        lifestyle=lifestyle,
        history=history
    )

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )

    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=Health_Report.pdf"

    return response


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)