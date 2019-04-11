var brain = require('brain.js')
var net = new brain.recurrent.LSTM();

var fs = require('fs');
var contents = fs.readFileSync('parliments.json', 'utf8');
var parliments = JSON.parse(contents)

net.train(parliments)

const classifier_output = net.toJSON();

fs.writeFile("classifier_output.json", JSON.stringify(classifier_output), function(err) {
    console.log("Classifier is saved.");
}); 