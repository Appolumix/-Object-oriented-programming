from flask import Flask, jsonify

app = Flask(__name__)

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут

    def get_info(self):
        return {"username": self.username, "email": self.email}

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            return {"message": "Password changed successfully"}
        return {"error": "Incorrect old password"}

    def greet_user(self):
        return {"message": f"Привет, {self.username}! Добро пожаловать на наш сайт!"}

class Admin(User):
    def __init__(self, username, email, password, privileges):
        super().__init__(username, email, password)
        self.privileges = privileges

    def show_privileges(self):
        return {"username": self.username, "privileges": self.privileges}

    def greet_user(self):
        return {"message": f"Здравствуйте, администратор {self.username}!"}

class Moderator(User):
    def __init__(self, username, email, password, moderation_areas):
        super().__init__(username, email, password)
        self.moderation_areas = moderation_areas

    def show_moderation_areas(self):
        return {"username": self.username, "moderation_areas": self.moderation_areas}

    def greet_user(self):
        return {"message": f"Приветствую, модератор {self.username}!"}

# Создаём несколько пользователей
general_user = User("john_doe", "john@example.com", "12345")
admin = Admin("admin_user", "admin@example.com", "adminpass", ["ban_users", "modify_posts"])
moderator = Moderator("mod_user", "mod@example.com", "modpass", ["forum", "comments"])

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the User Management API!"})

@app.route("/user")
def user_info():
    return jsonify(general_user.get_info())

@app.route("/admin")
def admin_info():
    return jsonify(admin.show_privileges())

@app.route("/moderator")
def moderator_info():
    return jsonify(moderator.show_moderation_areas())

@app.route("/greet/user")
def greet_user():
    return jsonify(general_user.greet_user())

@app.route("/greet/admin")
def greet_admin():
    return jsonify(admin.greet_user())

@app.route("/greet/moderator")
def greet_moderator():
    return jsonify(moderator.greet_user())

if __name__ == "__main__":
    app.run(debug=True)