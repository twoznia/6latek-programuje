const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/robot2.html');await p.pdf({path:__dirname+'/robot2.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await p.setViewportSize({width:794,height:1123});
const els=await p.$$('section');
for(let i=0;i<els.length;i++){await els[i].screenshot({path:__dirname+`/q${i+1}.png`});}
await b.close();console.log(els.length)})();
