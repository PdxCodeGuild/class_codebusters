const unitsInMeters = {
  ft: 0.3048,
  mi: 1609.34,
  m: 1,
  km: 1000,
  yd: 0.9144,
  in: 0.0254,
}

function checkAmount(amount){
  while(true){
    if(!isNaN(amount)){
      return parseFloat(amount)
    }
    else {
      amount = prompt('Invalid entry. Enter a number with or without decimals: ')
    }
  }
}

function checkMeasurement(measurement){
  while(true){
    if(measurement in unitsInMeters){
      return measurement
    }
    else {
      measurement = prompt(`Invalid entry. Enter ${Object.keys(unitsInMeters)}`)
    }
  }
}

const amount = checkAmount(prompt('Enter an amount:'))

const inputMeasurement = checkMeasurement(prompt(`Enter an input measurement (${Object.keys(unitsInMeters)}):`))

const outputMeasurement = checkMeasurement(prompt(`Enter an output measurement (${Object.keys(unitsInMeters)}):`))

const inMeters = amount * unitsInMeters[inputMeasurement]
let output = inMeters / unitsInMeters[outputMeasurement]

output = Math.round((output + Number.EPSILON) * 1000) / 1000



alert(`${amount} ${inputMeasurement} is ${output} ${outputMeasurement}`)