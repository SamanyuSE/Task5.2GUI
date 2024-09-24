import tkinter as tk
from gpiozero import PWMLED
from time import sleep

# Setup PWM LEDs connected to GPIO pins
led_a = PWMLED(17)
led_b = PWMLED(2)
led_c = PWMLED(3)

# Ensure all LEDs are initially off
def all_off():
    led_a.value = 0
    led_b.value = 0
    led_c.value = 0

# Turn off all LEDs when the script starts
all_off()

# Function to update LED brightness based on slider value
def update_led_brightness():
    led_a.value = slider_a.get() / 100
    led_b.value = slider_b.get() / 100
    led_c.value = slider_c.get() / 100

# Close the application and turn off all LEDs
def exit_program():
    all_off()
    main_window.quit()

# Create main window for the application
main_window = tk.Tk()
main_window.title("LED Brightness Control")

# Display title label
label_heading = tk.Label(main_window, text="Control the Brightness of LEDs", font=("Times New Roman", 18))
label_heading.pack(pady=15)

# Create sliders for each LED brightness control
slider_a = tk.Scale(main_window, from_=0, to=100, orient=tk.HORIZONTAL, label="LED A Brightness", command=lambda x: update_led_brightness())
slider_b = tk.Scale(main_window, from_=0, to=100, orient=tk.HORIZONTAL, label="LED B Brightness", command=lambda x: update_led_brightness())
slider_c = tk.Scale(main_window, from_=0, to=100, orient=tk.HORIZONTAL, label="LED C Brightness", command=lambda x: update_led_brightness())

# Pack the sliders into the window
slider_a.pack(pady=10)
slider_b.pack(pady=10)
slider_c.pack(pady=10)

# Button to turn off all LEDs
button_reset = tk.Button(main_window, text="Turn Off All LEDs", command=all_off)
button_reset.pack(pady=10)

# Button to close the program
button_exit = tk.Button(main_window, text="Close Program", command=exit_program)
button_exit.pack(pady=10)

main_window.mainloop()
