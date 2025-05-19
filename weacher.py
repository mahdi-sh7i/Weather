from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5 import uic
import sys
import requests

class UI(QMainWindow):
    def __init__(self):  # Corrected the initialization method
        super(UI, self).__init__()
        self.setObjectName("Form")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        uic.loadUi("weather.ui", self)

        self.label_city = self.findChild(QLabel, "label_city")
        self.label_humidity = self.findChild(QLabel, "label_humidity")
        self.label_temperature = self.findChild(QLabel, "label_temperature")
        self.label_weather = self.findChild(QLabel, "label_weather") 
        self.label_description = self.findChild(QLabel, "label_description")
        self.label_wind = self.findChild(QLabel, "label_wind")

        self.text_get = self.findChild(QLineEdit, "text_get")
        self.btn_search = self.findChild(QPushButton, "btn_search")
        self.label_pic = self.findChild(QLabel, "label_pic")
        self.label_picb = self.findChild(QLabel, "label_picb")
        
        # Clear fields on startup
        self.clearer()
        
        # Connect button click to function
        self.btn_search.clicked.connect(self.clicker)
        
        # Show The App
        self.center()  # Center the window        
        self.show()

    def center(self):
        # Center the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()  # Use QDesktopWidget here
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearer(self):
        self.text_get.setText("")  # Changed to setText for QLineEdit
        self.label_city.setText("")
        self.label_humidity.setText("")
        self.label_temperature.setText("")
        self.label_weather.setText("")
        self.label_description.setText("")
        self.label_wind.setText("")

    def clicker(self):
        city_name = self.text_get.text()  # Use text() for QLineEdit
        if city_name:
            weather_data = self.get_weather_data(city_name)
            if weather_data:
                weather_condition = weather_data['weather']
                self.label_city.setText(weather_data['city'])
                self.label_humidity.setText(f"{weather_data['humidity']}%")
                self.label_temperature.setText(f"{weather_data['temperature']} °C")
                self.label_weather.setText(f"{weather_data['weather']}")
                self.label_description.setText(f"{weather_data['description']}")
                self.label_wind.setText(f"{weather_data['wind_speed']} m/s")


                self.label_weather.setText(f"{weather_condition}")
                pixmap = QPixmap(f'/home/mahdi/all_pro/weather/small-image/{weather_condition}.jpg')  
                pixmab = QPixmap(f'/home/mahdi/all_pro/weather/big-image/{weather_condition}.jpg')
                self.label_pic.setPixmap(pixmap)  # Change to label_pic
                self.label_picb.setPixmap(pixmab)  # Change to label_picb
            else:
                self.clearer()  # Reset labels if no data found
                self.label_weather.setText("City not found or error fetching data.")
        else:
            self.clearer()

    def get_weather_data(self, city):
        api_key = "d27ca866dc15f3c9c1dd1df47a8d4cc2"  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                'city': data["name"],
                'humidity': data["main"]["humidity"],
                'temperature': data["main"]["temp"],
                'weather': data["weather"][0]["main"],
                'description': data["weather"][0]["description"],
                'wind_speed': data["wind"]["speed"]
            }
        except requests.exceptions.RequestException as e:
            print("Error fetching weather data:", e)
            return None

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
