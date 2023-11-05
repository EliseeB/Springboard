function findRotatedIndex(arr, num) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === num) {
      return mid;
    }

    // Check if the left half is sorted
    if (arr[left] <= arr[mid]) {
      if (arr[left] <= num && num < arr[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    // Check if the right half is sorted
    else {
      if (arr[mid] < num && num <= arr[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return -1; // If the value is not found in the array
}



module.exports = findRotatedIndex