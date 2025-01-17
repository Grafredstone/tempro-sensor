input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    basic.showString("" + Salt + "|" + Funkgruppe)
})
let Salt = 0
let Funkgruppe = 0
radio.setGroup(216)
Funkgruppe = randint(0, 255)
Salt = randint(0, 65536) * randint(0, 65536)
radio.sendValue(convertToText(Funkgruppe), Salt)
radio.setGroup(Funkgruppe)
DHT11.setPin(DigitalPin.P0)
basic.showString("S")
basic.setLedColor(0xff0000)
basic.pause(100)
basic.setLedColor(0x000000)
basic.forever(function () {
    radio.sendNumber(DHT11.temperature() * Salt)
    basic.setLedColor(0x00ffff)
    basic.setLedColor(0x000000)
})
