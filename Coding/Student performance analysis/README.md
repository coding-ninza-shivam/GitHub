Student Performance Analysis Portal
A flask based web application for students and educators to analyze academic performance, get AI-driven insights, and manage accounts securely.

🚀 Features
User Authentication: Sign up, sign in (with OTP), password reset, and secure session management.
Personal Dashboard: View your academic profile and access analysis tools.
Performance Analytics: Visualize grades and trends.
AI Prediction: Get smart predictions for future performance.
Support System: Contact support via a built-in form (sends email to admin).
Admin Panel: Manage users and view login logs (admin only).
Responsive Design: Works on desktop and mobile.
Security: Passwords are hashed, sessions are protected, and sensitive info is never exposed.
🛠️ Setup Instructions
1. Clone the repository
git clone https://github.com/Shivam-UX-cyber/Student-Performance-Analysis-Capstone-Project-1
cd student-performance-analysis
2. Create and activate a virtual environment
python -m venv env
env\Scripts\activate   # On Windows
# source env/bin/activate   # On Mac/Linux
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file or set these in your environment:

SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
Or edit app.py to set your email and secret key.

5. Initialize the database
python
>>> from app import db
>>> db.create_all()
>>> exit()
6. Run the app
python app.py
Visit http://127.0.0.1:5000 in your browser.

📄 Main Pages
/ — Home
/about — About the project
/docs — Documentation & FAQ
/support — Contact support (sends email)
/learn_more — Learn more about features & AI
/signup — Create account
/signin — Sign in (with OTP)
/dashboard — User dashboard
/admin — Admin panel (admin only)
✉️ Support
For help, use the Support page or email: support@example.com

⚠️ Security Notes
Never commit your real email password or secret key to public repositories.
Use environment variables or a .env file for sensitive info.
For Gmail, use an App Password if 2FA is enabled.
📚 License
MIT License (add your license file if needed).

👨‍💻 Authors
[Shivam_642 Shivam_637 Shivam_644 Shiv_631]
IITP 2025 Capstone Project Team
