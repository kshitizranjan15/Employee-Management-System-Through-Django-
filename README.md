
<!-- <div align="center">
  <img src="your-project-logo.png" alt="Project Logo">
</div> -->

# Employee Management System

A comprehensive web application developed with Django, offering a robust Employee Management System with features tailored for Employees, Managers, and HR.

## 🌟 Features

### Common Features for all Dashboards:

- **Edit Profile:** Update your information with ease.
- **Ask HR:** Direct communication with HR for queries.
- **Feedback:** Share feedback with managers, HR, or colleagues.
- **Leave Management:**
  - Apply Leave: Request leaves, and get them approved by your manager.
  - Leave Overview: Track the leaves you've taken.

- **eTMS (Transport Services):** Access information about company transport services.
- **Performance:** View your performance report.
- **LinkedIn Learning (LL):** Explore LinkedIn Learning resources.
- **Know Your Company:** Learn more about the company.
- **Logout:** Securely log out.

### Additional Features for Manager Dashboard:

- **Performance Review:** Provide feedback to your team.
- **Employee Status:** Get details on your team members.
- **Assign Department:** Manage departments and projects.
- **View Feedbacks:** See what your team thinks.
- **View Requests:** Review leave requests from your team.

### Additional Features for HR Dashboard:

- **View Feedbacks:** Check feedback from employees.
- **View Requests:** View queries submitted through Ask HR.
- **Assign Manager:** Assign managers to employees.
- **Add Employee:** Add new employees and send initial credentials via email.
- **Delete Employees:** Remove employee details securely.

## 🚀 Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database settings:**
   Adjust settings in `settings.py`.

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## 🌐 Usage

1. Access the application at `http://localhost:8000`.
2. Log in with your credentials.
3. Navigate to the respective dashboard based on your role.

## 🤝 Contribution

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Remember to replace `<repository-url>` with the actual URL of your repository, and include your project logo file in the repository with the correct path in the image tag.