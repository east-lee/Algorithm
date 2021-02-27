function solution(n, record) {
    var answer = [];
    var check = [[],[],[],[],[],[],[],[],[]]
    
    for (let i=0;i<record.length;i++){
        var new_arr = record[i].split(' ')
        var j = parseInt(new_arr[0])-1
        var name = new_arr[1]
        if (check[j].includes(name)){
            continue
        } else if (check[j].length===5) {
            check[j].splice(0,1)
            check[j].push(name)
        } else if (check[j]) {
            check[j].push(name)
        }                 
    }
    
    for (let m=0;m<n;m++){
        var result_arr = check[m]
        for (let k=0;k<result_arr.length;k++){
            answer.push(result_arr[k])
        }
    }

    
    return answer;
}