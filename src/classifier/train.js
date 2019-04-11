var brain = require('brain.js')
var net = new brain.recurrent.LSTM();

var fs = require('fs');
var contents = fs.readFileSync('parliamentarians.json', 'utf8');
var parliamentarians = JSON.parse(contents)

net.train(parliamentarians)

const classifier_output = net.toJSON();

fs.writeFile("classifier_output.json", JSON.stringify(classifier_output), function(err) {
    console.log("Classifier is saved.");
}); 