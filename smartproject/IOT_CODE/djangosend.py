



import RPi.GPIO as GPIO
import requests
import time

# Set the GPIO pin for the switch
SWITCH_PIN = 17  # Change this to your GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

def get_contact_details(device_id):
    print("enterd function");
    # Replace with your Django server URL
    url = f'http://192.160.100.200:8000/api/get_contact_details/{device_id}/'
    
    print(url)
    try:
        print("entered try..")
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            print("entered 1st if..")
            print("Contact details:", response.json())
        else:
            print("entered 1st else")
            print("Failed to retrieve contact details:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

try:
    while True:
       # time.sl#eep() 
        print("entered whlie..")
        input_state = GPIO.input(SWITCH_PIN)
        if input_state == GPIO.LOW:  # Button is pressed
            print("Switch pressed!")
            device_id = 3  # Example device ID, replace with actual device ID
            get_contact_details(device_id)
            time.sleep(1)  # Delay to debounce the button press
        time.sleep(5)  # Small delay to prevent high CPU usage
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit






(iotenv) C:\Users\akula\OneDrive\Desktop\projects\smart_Device_project\smartproject>python manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 19, 2025 - 06:27:18
Django version 3.1.8, using settings 'smartproject.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
Email sent to: projectindia251268@gmail.com
[19/Mar/2025 06:27:34] "GET /api/get_contact_details/3/ HTTP/1.1" 200 21
Email sent to: projectindia251268@gmail.com
[19/Mar/2025 06:28:43] "GET /api/get_contact_details/3/ HTTP/1.1" 200 21
C:\Users\akula\OneDrive\Desktop\projects\smart_Device_project\smartproject\smartapp\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 19, 2025 - 06:29:17
Django version 3.1.8, using settings 'smartproject.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.
Email sent to: projectindia251268@gmail.com
Error sending SMS: 
HTTP Error Your request was:

POST /Accounts/AC87c2a7f0187439b6c1e08ee06c74025f/Messages.json

Twilio returned the following information:

Unable to create record: Mismatch between the 'From' number +13218004216 and the account AC87c2a7f0187439b6c1e08ee06c74025f

More information may be available here:

https://www.twilio.com/docs/errors/21660


[19/Mar/2025 06:29:36] "GET /api/get_contact_details/3/ HTTP/1.1" 200 21







import RPi.GPIO as GPIO
import time
import requests

# GPIO Pin Assignments
BUTTON_PIN =  22  # Button connected to GPIO 17
BLUE_LED =  27   # Operation In Progress
GREEN_LED = 17   # Operation Success
RED_LED =  10  # Error / Failure

# Django API Endpoint
API_URL = "http://192.168.35.245:8000/api/get_contact_details/18/"

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable Pull-Up Resistor
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Initial LED State
GPIO.output(BLUE_LED, GPIO.LOW)
GPIO.output(GREEN_LED, GPIO.LOW)
GPIO.output(RED_LED, GPIO.LOW)

# Function to Call API and Process Response
def call_api():
    print("Button Pressed ? Blue LED ON (Calling API...)")
    GPIO.output(BLUE_LED, GPIO.HIGH)  # Turn ON Blue LED while waiting for API response

    try:
        response = requests.get(API_URL, timeout=10)  # Call API with a 10-second timeout
        if response.status_code == 200:
            print("API Response: SUCCESS")
            GPIO.output(GREEN_LED, GPIO.HIGH)  # Turn ON Green LED for success
            time.sleep(2)
            GPIO.output(GREEN_LED, GPIO.LOW)  # Turn OFF Green LED
        else:
            print("API Response: FAILURE")
            GPIO.output(RED_LED, GPIO.HIGH)  # Turn ON Red LED for failure
            time.sleep(2)
            GPIO.output(RED_LED, GPIO.LOW)  # Turn OFF Red LED
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        GPIO.output(RED_LED, GPIO.HIGH)  # Turn ON Red LED for failure
        time.sleep(2)
        GPIO.output(RED_LED, GPIO.LOW)  # Turn OFF Red LED
    finally:
        GPIO.output(BLUE_LED, GPIO.LOW)  # Turn OFF Blue LED when response is received

# Button Press Event Listener
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=lambda channel: call_api(), bouncetime=300)

# Keep Script Running
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()




ip address find in django appication --->>ipconfig

ip address find in raspberry  --->>hostname -I





