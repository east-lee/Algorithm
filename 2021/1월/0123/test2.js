function solution(m, v) {
    var answer = 0;
    var check = []
    
    for (let i=0;i<v.length;i++){
        var block = v[i]
        if (check.length===0){
            check.push(block)
        } else{
            for (let j=check.length-1;j>=0;j--){
            var now_len = check[j] 
            if (now_len+block>m) {
                if (check[j+1]){
                    check[j+1] += block    
                } else {
                    check[j+1] = block
                }
                
                break
            } else {
                if (j===0) {
                    check[j] += block
                }
            }
            }      
        }        
    }
    answer = check.length

    return answer;
}