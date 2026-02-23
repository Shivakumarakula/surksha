
import RPi.GPIO as GPIO
import time
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

# GPIO Setup
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Twilio credentials
account_sid = 'AC87c2a7f0187439b6c1e08ee06c74025f'
auth_token = 'a771922a4ceff468d85871853f052242'

# Email credentials
email_address = 'octatanglecare3s@gmail.com'
email_password = 'nvxz bzjd ypqa crkk'

# Static receiver information
receiver_email = 'akulashivaakulashiva@gmail.com'
receiver_phone = '+919390370155'

# Function to send email
def send_email():
    subject = "Emergency Alert"
    body = "This is an emergency alert. Please check in with the sender as soon as possible."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = receiver_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_address, email_password)
        server.sendmail(email_address, receiver_email, msg.as_string())
    print(f"Email sent to {receiver_email}")

# Function to send SMS using Twilio API
#def send_sms():
 #   client = Client(account_sid, auth_token)
  ###print(f"SMS sent to {receiver_phone}")

# Function to handle button press
def on_button_press():
    print("Button pressed!")
    #send_sms()
    send_email()

# Main loop
try:
    while True:
        input_state = GPIO.input(BUTTON_PIN)
        if input_state == False:
            on_button_press()
            time.sleep(5)  # Debounce
finally:
    GPIO.cleanup()








import RPi.GPIO as GPIO
import requests
import time

# Set the GPIO pin for the switch
SWITCH_PIN = 17  # Change this to your GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

def get_contact_details(device_id):
    #print("enterd function");
    # Replace with your Django server URL
    url = f'http://192.168.105.245:8000/api/get_contact_details/{device_id}/'
    
    print(url)
    try:
#        print("entered try..")
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
 #           print("entered 1st if..")
            print("Contact details:", response.json())
        else:
  #          print("entered 1st else")
            print("Failed to retrieve contact details:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

try:
    while True:
        print("Device is started.....")
       # time.sl#eep() 
   #     print("entered whlie..")
        input_state = GPIO.input(SWITCH_PIN)
        if input_state == GPIO.LOW:  # Button is pressed
            print("Switch pressed!")
            print("alert message is send to your contacts....!!!1")
            device_id = 3  # Example device ID, replace with actual device ID
            get_contact_details(device_id)
            time.sleep(1)  # Delay to debounce the button press
        time.sleep(2)  # Small delay to prevent high CPU usage
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit
