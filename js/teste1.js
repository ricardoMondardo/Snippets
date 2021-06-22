function removeFromString(str, index) {
    let result = '';
    for (let i in str) if (i != index) result += str[i];
    return result;
}


console.log(removeFromString('abcd',1));