// let iter = 7;
// let arr = [];
// for (let i = 0; i < iter; i++) {
//     console.log(`iter number ${i}`);
//     arr.push(`elem${i}`);
// }
// console.log(arr);
// for (let i = 0; i < arr.length; i++) {
//     //console.log(arr[i]);
//     let html = `<div>${arr[i]}</div>`
//     console.log(html);
// }
// const pass = 'pasadadass';
// if (pass.length > 8 && true) {
//     console.log();
// }

let age = 30;
if (true) {
    let age = 50;
    var x = 'hello';
    if (true) {
        let age = 70;
        console.log('inside super internal block:', age);
    }
    console.log('inside block:', age);
}
console.log('outside block:', x);


let temp = false;
let val = (temp) ? 10 : 20;
console.log(val);
