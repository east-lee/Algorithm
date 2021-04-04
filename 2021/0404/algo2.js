function solution(needs, r) {
    var answer = needs.length;    
    if (r === needs.length) {
        return answer
    }
    
    
    const getSubsets = function (arr,r) {
        let flag = new Array(arr.length).fill(false); 
        const subSets = []
        
        const subSet = function DFS (depth) {
            if (depth === arr.length) {
                const subSet = arr.filter((value,index) => flag[index])                 
                if (subSet.length === (needs[0].length)-r) {
                    subSets.push(subSet);    
                }
                return
            }
            flag[depth] = true
            subSet(depth+1)
            flag[depth] = false
            subSet(depth+1)
        }
        subSet(0)
        return subSets
    }
    
    
    var robots_num = []
    for (let i=0;i<needs[0].length;i++){ robots_num.push(i)}
    
    var pos_subSet = getSubsets(robots_num,r)    
    
    let max_cnt = 0
    
    for (var i = 0; i<pos_subSet.length;i++) {
        let last_break_check = false
        let check_cnt = needs.length
        
        for (var j = 0; j<needs.length;j++){
            let break_check =false
            for (var k = 0; k<pos_subSet[i].length;k++) {
                if (needs[j][pos_subSet[i][k]]) {
                    check_cnt -= 1
                    break_check = true
                    break
                }
            }
            if (break_check && check_cnt < max_cnt) {
                last_break_check = true
                break
            }
            
        }        
        if (!last_break_check && max_cnt < check_cnt) {
            max_cnt = check_cnt
        }
    }
    
    answer = max_cnt
    
    return answer;
}