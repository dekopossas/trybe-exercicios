const trocarNome = (frase, nome) =>{
    let frase2 = '';
    frase2 = frase;
    for (let c = 0; c < frase.length; c += 1){
        if (frase[c] === 'x'){
            frase2[c] = nome;
        }
        return frase2;
    }
}

let f = 'eu e o x estavamos passeando pelo tibia.';
let n = [henrique];
f[7] = n[0];
console.log (f[7]);

console.log (f.replace(/x/g, n));
// console.log(trocarNome(f, n));

for (let c = 0; c < f.length; c += 1){
    console.log (f[c]);
}


let f = 'eu e o x estavamos passeando pelo tibia.';
let n = 'Lazzanha';
const arr = f.split('')
console.log(arr)
arr[7] = n;
console.log (arr.join(''));