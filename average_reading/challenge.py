"""
Let's say we're building a weather-forecasting software. To determine the 
temperature of a city, we take temperature readings from across many 
thermometers across the city, and we calculate the mean average of those
temperatures.
We'd also like to display the temperatures in both Fahrenheit and Celsius, but
our readings are initially only provided to us in Fahrenheit.
To get the average Celsius temperature, our algorithm does two things:
first, it converts all the readings from Fahrenheit to Celsius.
Then, it calculates the mean average of all the Celsius numbers.

Fahrenheit to Celsius: (T°F - 32) * 5/9 = T°C
"""


def average_temperature(temperatures):
    celsius = []
    for temp in temperatures:
        celsius.append((temp - 32) * 5 / 9)
    return sum(celsius) / len(celsius)
