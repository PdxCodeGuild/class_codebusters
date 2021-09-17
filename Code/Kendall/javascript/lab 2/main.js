function LengthConverter(valNum) {
    document.getElementById("outputMiles").innerHTML = valNum * 0.000621371;
    document.getElementById("outputKilometers").innerHTML = valNum * 1000;
    document.getElementById("outputYards").innerHTML = valNum * 1.0936;
    document.getElementById("outputFeet").innerHTML = Math.round(valNum * 3.28084, 4);
    document.getElementById("outputInches").innerHTML = valNum * 39.370;
}