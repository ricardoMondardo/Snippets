







function findFrequence(arr) {
    let result = {};
    for (c in arr)
    {
        if (result[arr[c]] == null) {
            result[arr[c]] = 1
        } else {
            result[arr[c]] += 1
        }
    }
    return result
}

let strPhase = "acckasjdsffsadsaccca";
let strInterval = "aafc";

let arrPhase = strPhase.split("");
let arrInterval = strInterval.split("");

let frequenceInterval = findFrequence(arrInterval);

console.log(frequenceInterval);


