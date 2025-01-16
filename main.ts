radio.setGroup(216)
let Funkgruppe = randint(0, 255)
let Salt = randint(0, 65536) * randint(0, 65536)
radio.sendValue(convertToText(Funkgruppe), Salt)
radio.setGroup(Funkgruppe)
DHT11.setPin(DigitalPin.P0)
basic.showLeds(`
    . . # # .
    . # . . .
    . . # . .
    . . . # .
    . # # . .
    `)
basic.forever(function () {
    radio.sendNumber(DHT11.temperature() * Salt)
    basic.setLedColor(0x00ffff)
    basic.pause(100)
    basic.setLedColor(0x000000)
})
