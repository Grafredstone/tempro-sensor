Funkgruppe = randint(0, 255)
Salt = randint(0, 65536) * randint(0, 65536)
radio.send_value(convert_to_text(Funkgruppe), Salt)
radio.set_group(Funkgruppe)
DHT11.set_pin(DigitalPin.P0)
basic.show_leds("""
    . . # # .
    . # . . .
    . . # . .
    . . . # .
    . # # . .
    """)

def on_forever():
    radio.send_number(DHT11.temperature() * Salt)
    basic.set_led_color(0x00ffff)
    basic.set_led_color(0x000000)
basic.forever(on_forever)
