function findRotationCount(arr) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    // If the array is sorted and not rotated, return 0
    if (arr[left] <= arr[right]) {
      return left;
    }

    const mid = Math.floor((left + right) / 2);
    const next = (mid + 1) % arr.length;
    const prev = (mid + arr.length - 1) % arr.length;

    if (arr[mid] <= arr[next] && arr[mid] <= arr[prev]) {
      return mid;
    }

    if (arr[mid] <= arr[right]) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return -1; // Return -1 if the input array is empty or invalid
}

module.exports = findRotationCount