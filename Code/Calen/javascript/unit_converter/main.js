const unitsInMeters = {
    feet: 0.3048,
    miles: 1609.34,
    meters: 1,
    kilometer: 1000,
    yards: 0.9144,
    inches: 0.0254,
}

function checkAmount(amount):
    while(true){
        if(!isNaN(amount)){
            return parseFloat(amount)
        }
        else {
            amount = prompt('invalid entry.')
        }

    }

function checkMeasurement(measurement){
    while(true){
        if (measurement in unitsInMeters){
            return measurement
        }
        else {
            measurement = prompt('invalid entry.')
        }
    }
}

const amount = checkAmout(prompt('Enter an amount.'))

const inputMeasurement = checkMeasurement(prompt('Enter an input measurement. '))

const outputMeasurement = checkMeasurement(prompt('Enter a output measurement'))

const inMeters = amount * unitsInMeters[inputMeasurement]

let output = inMeters / unitsInMeters[outputMeasurement]

output = Math.round((output+Number.EPSILON)*1000) / 1000

alert('${amount} ${inputMeasurement} is ${output} ${outputMeasurement.}')