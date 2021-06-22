function removeFromString(str, v) {
    let arrStr = str.split('')
    result = arrStr.filter(e => e != v)
    return result.join('');
}

function MinWindowSubstring(strArr) { 

    const phase = strArr[0];
    const strInterval = strArr[1];

    let list = [];
    let lists = [];    

    for (let i = 0; i < phase.length; i++)
    {        
        let firstValue = phase[i];
        let strTemp = strInterval;

        let index = strTemp.indexOf(firstValue)
        if (index > -1) {

            // Just Fix de FN, to realy remove
            strTemp = removeFromString(strTemp,firstValue);
            list.push(firstValue);            

            for (let j = i+1; j < phase.length; j++)
            {            
                let nextValue = phase[j];
    
                index = strTemp.indexOf(nextValue)
                list.push(nextValue);
    
                if (index > -1) {
                    strTemp = removeFromString(strTemp,nextValue)                
                }
    
                if (strTemp.length == 0) {
                    console.log(firstValue, nextValue, list);
                    lists.push(list.join(''));
                    list = [];
                    j == phase.length;
                    strTemp = strInterval;
                }
                        
            }
        }    
        
    }

    return lists   
}
     
console.log(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]));

//aksfaje
