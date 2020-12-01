const fs = require('fs');
const buffer = fs.readFileSync('01.txt');
const s = buffer.toString().split('\n');
let data = s.map((elem) => parseInt(elem));


function part1(data) {
    let seen = new Set();
    for (let i=0; i<data.length; i++) {
        if (seen.has(2020-data[i])) {
            return data[i] * (2020-data[i]);
        }
        seen.add(data[i]);
    }
}


function part2(data) {
    data.sort();
    let n = data.length;
    for (let i=0; i<n-2; i++) {
        let l = i+1;
        let r = n-1;
        while (l < r) {
            let a = data[i];
            let b = data[l];
            let c = data[r];
            let cur = a+b+c;
            if (cur===2020) {
                return a*b*c;
            }
            if (cur-2020 > 0) {
                r -= 1;
            } else {
                l += 1;
            }
        }
    }
}


console.log(part1(data));
console.log(part2(data));