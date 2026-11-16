const fs = require('fs');
const path = require('path');

const tmplPath = path.join(__dirname, 'template.html');
const examsPath = path.join(__dirname, 'mendix_advanced_data.json');
const u111Path = path.join(__dirname, 'mendix_advanced_unique_111.json');
const u314Path = path.join(__dirname, 'mendix_advanced_unique_314.json');
const outPath = path.join(__dirname, 'index.html');

console.log('Reading files...');
const template = fs.readFileSync(tmplPath, 'utf-8');
const exams = JSON.parse(fs.readFileSync(examsPath, 'utf-8'));
const u111 = JSON.parse(fs.readFileSync(u111Path, 'utf-8'));
const u314 = JSON.parse(fs.readFileSync(u314Path, 'utf-8'));

console.log('Injecting datasets...');
let output = template
  .replace('/*__DATA_EXAMS__*/', JSON.stringify(exams))
  .replace('/*__DATA_UNIQUE_111__*/', JSON.stringify(u111))
  .replace('/*__DATA_UNIQUE_314__*/', JSON.stringify(u314));

fs.writeFileSync(outPath, output, 'utf-8');
console.log('Successfully generated index.html!');
console.log('File size:', (fs.statSync(outPath).size / 1024).toFixed(1), 'KB');

