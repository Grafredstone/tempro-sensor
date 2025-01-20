def on_button_ab():
    basic.show_string("" + str(Salt) + "|" + ("" + str(Funkgruppe)))
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

Salt = 0
Funkgruppe = 0
radio.set_group(216)
Funkgruppe = randint(0, 255)
Salt = randint(0, 65536) * randint(0, 65536)
radio.send_value(convert_to_text(Funkgruppe), Salt)
radio.set_group(Funkgruppe)
DHT11.set_pin(DigitalPin.P0)
basic.show_string("S")
basic.set_led_color(0xff0000)
basic.pause(100)
basic.set_led_color(0x000000)
basic.set_led_color(0x00ffff)

def on_forever():
    radio.send_number(DHT11.temperature() * Salt)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        # . . . #
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
        . # # # .
        # . . . #
        . . . . .
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . # # # .
        # . . . #
        . . . . .
        . . . . .
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        """)
basic.forever(on_forever)
