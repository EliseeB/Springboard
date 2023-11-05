const countZeroes = arr => {
    let leftIndex = 0
    let rightIndex = arr.length - 1

    while (leftIndex <= rightIndex) {
        const mid = Math.floor((leftIndex + rightIndex) / 2)

        if (arr[mid] === 0) {
            
            if (mid === 0 || arr[mid - 1] === 1) {
                return arr.length - mid
            } else {
                rightIndex = mid -1
            }
        } else {
            leftIndex = mid + 1
        }
    }

}


module.exports = countZeroes