from flask import Flask, render_template, request
app = Flask(__name__)

class VirtualAssistant:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def greet(self):
        return f"Hello! I am {self.name}, your AI-powered virtual assistant from {self.company}."

    def assist(self, task):
        if task.lower() == "scheduling appointments":
            return self.schedule_appointment()
        elif task.lower() == "financial advice":
            return self.financial_advice()
        elif task.lower() == "investment options":
            return self.investment_options()
        elif task.lower() == "account management":
            return self.account_management()
        else:
            return f"I can help you with {task}. How can I assist you today?"

    def schedule_appointment(self):
        return "To schedule an appointment, please provide your preferred date and time."

    def financial_advice(self):
        return "For financial advice, please provide some details about your current financial situation and goals."

    def investment_options(self):
        return "We offer a range of investment options including stocks, bonds, mutual funds, and real estate. Which are you interested in?"

    def account_management(self):
        return "For account management, please provide your account number and the type of assistance you need."

# Create an instance of the Virtual Assistant
assistant = VirtualAssistant("Ekaita Assistant", "Ekaita Financial Consultancy")

@app.route('/')
def index():
    greeting = assistant.greet()
    return render_template('index.html', greeting=greeting)

@app.route('/assist', methods=['POST'])
def assist():
    task = request.form['task']
    response = assistant.assist(task)
    return render_template('index.html', response=response, greeting=assistant.greet())

if __name__ == '__main__':
    app.run(debug=True)
