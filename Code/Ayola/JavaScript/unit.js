
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });



function v1(){
    rl.question("What is the distance in feet? ", function (answer) {
        var dist = parseFloat(answer)
        var meter = dist*0.3048
        console.log(dist,"feet is",meter,"m")
        
      });



}

function v2(conv) {
    
    
    var unit = ""
    rl.question("What is the distance ? ", function (answer) {
        var dist = parseFloat(answer)
        rl.question("What is the unit ?", function(ans){
            unit = ans
            var multiplier = parseFloat(conv[unit])
            var converted = dist*multiplier
            console.log(dist,unit,"is",converted,"m")

        })

        
        
      });
  }

function v3(){

    var conv = {
        "ft":0.3048,
        "mi":1609.34,
        "m":1,
        "km":1000,
        "yard":0.9144,
        "inch":0.0254
        }
    v2(conv)

}

function v4(conv){
    var unit1 = ""
    var unit2 = ""

    rl.question("What is the distance ? ", function (answer) {
        var dist = parseFloat(answer)
        rl.question("What is the input unit ?", function(ans){
            unit1 = ans
            rl.question("What is the output unit ?",function(an){
                unit2 = an
                var inp_list = conv[unit1]
                var meter = parseFloat(inp_list['m'])*dist
                var converted = parseFloat(conv['m'][unit2])*meter
                console.log(dist,unit1,"is",converted,unit2)
                
            })

        })

        
        
      });

}









conv2 = {
    "ft":0.3048,
    "mi":1609.34,
    "m":1,
    "km":1000
    }

conv4 = {
    "ft":{
        "ft":1,
        "m":0.3048
    },
    "mi":{
        "mi":1,
        "m":1609.34
    },
    "m":{
        "m":1,
        "ft":1/0.3048,
        "mi":0.000621,
        "km":0.001
    },
    "km":{
        "m":1000,
        "km":1
    }

}



//v1()
//v2(conv2)
//v3()
v4(conv4)