const code = `
while (true) console.log('kablewy');
postMessage('L');while (true) console.log('kablewy');
postMessage('I');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('C');while (true) console.log('kablewy');
postMessage('T');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('{');while (true) console.log('kablewy');
postMessage('k');while (true) console.log('kablewy');
postMessage('3');while (true) console.log('kablewy');
postMessage('F');while (true) console.log('kablewy');
postMessage('7');while (true) console.log('kablewy');
postMessage('z');while (true) console.log('kablewy');
postMessage('H');while (true) console.log('kablewy');
postMessage('}');`;

const regex = /postMessage\('([A-Za-z0-9{}])'\)/g;

let match;
let extractedLetters = '';

while ((match = regex.exec(code)) !== null) {
  extractedLetters += match[1];
}

console.log('Extracted letters:', extractedLetters);
