function removeFromString(str, v) {
    let arrStr = str.split('')
    result = arrStr.filter(e => e != v)
    return result.join('');
}


console.log(removeFromString('abcd','b'));