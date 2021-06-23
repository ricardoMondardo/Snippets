function removeFromString(str, index) {
    let result = '';
    for (let i in str) if (i != index) result += str[i];
    return result;
}

function MinWindowSubstring(strArr) { 

    const phase = strArr[0];
    const strInterval = strArr[1];

    let list = []; 
    let result = phase;

    for (let i = 0; i < phase.length; i++)
    {        
        let firstValue = phase[i];
        let strTemp = strInterval;

        let index = strTemp.indexOf(firstValue)
        if (index > -1) {

            strTemp = removeFromString(strTemp,index);
            list.push(firstValue);            

            for (let j = i+1; j < phase.length; j++)
            {            
                let nextValue = phase[j];
    
                index = strTemp.indexOf(nextValue)                
                if (strInterval.length > 1) list.push(nextValue);
    
                if (index > -1) {
                    strTemp = removeFromString(strTemp,index)                
                }
    
                // When all is found
                if (strTemp.length == 0) {
                    if (list.length >= strInterval.length) {                        
                        if (list.length < result.length) {
                            result = list.join('')
                        }              
                    }
                    list = [];
                    strTemp = strInterval;
                    j = phase.length;
                }
                        
            }
        }    
        
    }
    return result   
}
     
console.log(MinWindowSubstring(["ahffaksfajeeubsne", "a"]));
//aksfaje
