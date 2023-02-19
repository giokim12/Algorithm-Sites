function solution(array) {
    var s = array.sort((a,b) => a-b)
    var len = array.length
    var mid = parseInt(len/2)
    var answer = array[mid];
    return answer;
}