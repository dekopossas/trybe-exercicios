const assert = require('assert');

const numbers = (myArray) => {
    for (let i = 0; i < myArray.length; i += 1) {
      if (typeof myArray[i] !== 'number') {
        return false;
      }
    }
    return true;
};

assert.equal(numbers([1, 2, 3, 4, 5]), true);
assert.equal(numbers([1, 2, '3', 4, 5]), false);
assert.equal(numbers([' ']), false);
assert.equal(numbers([1, 'a', 3]), false);
