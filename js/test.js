let objOne = { a: 1, b: 2 }
let objTwo = { a: 1, b: 2 }

const isEqual = (...objects) => objects.every(obj => JSON.stringify(obj) === JSON.stringify(objects[0]));




console.log(isEqual(objOne, objTwo));