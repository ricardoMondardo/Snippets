function findFrequence(arr) {
    let result = {};
    for (i in arr)
    {
        if (result[arr[i]] == null) {
            result[arr[i]] = 1
        } else {
            result[arr[i]] += 1
        }
    }
    return result
}

function MinWindowSubstring(strArr) { 

    const arrPhase = strArr[0].split("");
    const arrInterval = strArr[1].split("");

    let frequanceInterval = findFrequence(arrInterval)
    let intervals = []


    let intervalPartial = {};

    console.log(Array.isArray(arrPhase));

    for (let i = 0; i < arrPhase.length; i++)
    {
        intervalPartial = frequanceInterval;
        if (intervalPartial[arrPhase[i]] != null) intervalPartial[arrPhase[i]] = -1;
        for (let j = i; j < arrPhase.length; j++)
        {
            if (intervalPartial[arrPhase[j]] != null) intervalPartial[arrPhase[j]] = -1;
            console.log(intervalPartial)
        }
        
    }

    return frequanceInterval   
}
     
console.log(MinWindowSubstring(["ahffaksfajeeubsnea", "jefaa"]));