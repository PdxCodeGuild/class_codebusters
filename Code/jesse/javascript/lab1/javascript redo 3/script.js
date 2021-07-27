
// Unit Converter

const unitsInMeters = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
}

// check if a number amount was correctly entered
function checkAmount(amount) {
    while (true) {
        if (!isNaN(amount)) {
            return parseFloat(amount)
        } else {
            amount = prompt('Invalid entry. Enter a number with or without decimals: ')
        }
    }
}

// check if a correct measurement was entered
function checkMeasurement(measurement) {
    while (true) {
        if (measurement in unitsInMeters) {
            return measurement
        } else {
            measurement = prompt('Invalid entry. Enter "ft", "mi," "m," or "km", "yd", "in": ')
        }
    }
}

// get amount of the measurement from user
const amount = checkAmount(prompt('Enter an amount: '))

// get input measurement from user
const inputMeasurement = checkMeasurement(prompt('Enter an input measurement (ft, mi, m, km, yd, or in): '))

// get output measurement from user
const outputMeasurement = checkMeasurement(prompt('Enter an output measurement (ft, mi, m, km, yd, or in): '))

// convert measurement to meters
let inMeters = amount * unitsInMeters[inputMeasurement]

// convert meters to output measurment
let output = inMeters / unitsInMeters[outputMeasurement]

// round result to 4th decimal place
output = Math.round((output + Number.EPSILON) * 10000) / 10000

alert(`${amount} ${inputMeasurement} is ${output} ${outputMeasurement}`)