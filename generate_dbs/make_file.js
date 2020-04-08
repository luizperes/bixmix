
const makeid = (length) => {
   var result           = '';
   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
   var charactersLength = characters.length;
   for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}

size = process.argv[2];
strsize = process.argv[3];

for (i = 0; i < size; i++) {
  console.log(i + "," + makeid(strsize));
}

