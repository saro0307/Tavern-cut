# Tavern-cut

Tavern Cut is an advanced cybersecurity application that integrates a Turing Test algorithm with artificial intelligence (AI) to enhance password protection and fortify online accounts against unauthorized access. This project aims to provide a robust and adaptive security mechanism by distinguishing between legitimate users and potential intruders through human-like conversational interactions.

## Features

- **AI-Driven Turing Test:** Utilizes AI to engage users in dynamic conversations during login attempts to assess authenticity.
- **Intruder Alert Mechanism:** Sends automated email alerts to notify users of potential unauthorized access attempts.
- **Continuous Learning:** The system evolves over time, improving its ability to distinguish between genuine users and threats through machine learning.
- **User-Friendly Interface:** Provides a seamless and intuitive interface for user registration, login, and response to security alerts.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/tavern-cut.git
   cd tavern-cut
   ```

2. **Install required libraries:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure email settings:**
   Replace the placeholders in the code with your actual email credentials:
   ```python
   email_sender = 'your_email@gmail.com'
   email_password = 'your_password'
   email_receiver = 'receiver_email@gmail.com'
   ```

4. **Run the application:**
   ```sh
   python tavern_cut.py
   ```

## Usage

1. **User Registration:**
   - Enter your email address and set up a secure password.

2. **Login:**
   - Enter your username and password.
   - The system will engage in a human-like conversation to verify authenticity.

3. **Security Alerts:**
   - In case of unauthorized access attempts, an email alert will be sent to the configured email address.

## Code Overview

### Turing Machine States and Transitions

The Turing machine is implemented to verify the password correctness through a series of states and transitions.

```python
states = {
    "q0": {"r": ("q1", "r", "R")},
    "q1": {"u": ("q2", "u", "R")},
    "q2": {"s": ("q3", "s", "R")},
    "q3": {"s": ("accept", "s", "S")},
    "q4": {"i": ("accept", "i", "S")},
    "q5": {"a": ("accept", "a", "S")},
}
```

### Email Alert Configuration

The `send_email_alert` function sends an email notification if an unauthorized login attempt is detected.

```python
def send_email_alert():
    # Email configuration and sending logic
```

### GUI Setup

The application uses Tkinter to create a user-friendly interface for login and registration.

```python
root = tk.Tk()
root.title("Login Page")
# GUI components setup
root.mainloop()
```

## Future Work

Future evaluations will focus on:

- **Scalability:** Assessing system performance under increased user load.
- **Real-World Deployment:** Testing the system in corporate networks and large-scale platforms.
- **Adaptability:** Enhancing resilience against sophisticated AI-driven attacks.
- **User Experience:** Continuously improving the user interface and reducing false positives.
- **Cross-Platform Compatibility:** Ensuring seamless performance across various operating systems, browsers, and devices.
- **Legal Compliance:** Ensuring adherence to privacy regulations and data protection laws.

## Conclusion

Tavern Cut represents a significant advancement in cybersecurity, integrating the Turing Test algorithm with AI to provide a dynamic and adaptive defense mechanism. This project demonstrates the potential of AI in enhancing online security, offering a robust solution against evolving cyber threats.

## Authors

- Sam Priesly Mathuram P
- Saravana Kumar G
- Sudharsun B
- Thiru Vigneswaran babu S

## License

This project is licensed under the Apache-2.0 license. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- SNS College of Engineering, Coimbatore, Tamil Nadu, India
- All contributors and supporters of the project

For more details, refer to the project report available [here](https://ijsart.com/Home/IssueDetail/90871)) (Volume 10 Issue 5 – MAY 2024).
