radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber / Salt)
})
radio.onReceivedValue(function (name, value) {
    basic.showIcon(IconNames.Yes)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . # .
        . # . # .
        . # # . .
        `)
    radio.setGroup(parseFloat(name))
    Salt = value
})
let Salt = 0
while (true) {
    basic.showIcon(IconNames.Diamond)
    basic.pause(200)
    basic.showIcon(IconNames.SmallDiamond)
    basic.pause(200)
}
