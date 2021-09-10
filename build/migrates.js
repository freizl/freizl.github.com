const fs = require('fs');
const path = require('path');

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

fs.readdirSync('./posts/')
  .filter(file => file.endsWith('.org'))
  .forEach(file => {
    const mdFileName = file.slice(0, file.length - 4);
    const mdFC = fs.readFileSync(`./posts/${mdFileName}`, 'utf-8')
      .split('\n');
    const tags = mdFC.filter(line => line.startsWith('tags'))[0];

    const fc = fs.readFileSync('./posts/' + file, 'utf-8');

    const date = file.slice(0, 10);
    const fileName = file.slice(11, file.length - 7);
    const title1 = fileName.replace(/-/g, ' ');
    const title2 = title1.split(' ').map(capitalizeFirstLetter).join(' ');

    let newHeader = `#+TITLE: ${title2}\n#+DATE: ${date}\n`;
    if (tags) {
      newHeader += `#+hugo_${tags.replace(/,/g, ' ')}\n`;
    }

    console.log(mdFileName, tags);
    fs.writeFileSync('./new-posts/' + fileName + '.org', newHeader + '\n' + fc);
  });
