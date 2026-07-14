class Solution {
  /**
   * @param {string} s
   * @return {boolean}
   */
  isValid(s) {
    const open  = '([{';
    const close = ')]}';
    const stack = [];

    for (let i = 0; i < s.length; i++) {
      const char = s[i];

      if (open.includes(char)) {
        // opening bracket → push
        stack.push(char);

      } else if (close.includes(char)) {
        // closing bracket → must match last opener
        const expectedOpen = open[ close.indexOf(char) ];
        const lastOpen     = stack.pop();

        if (lastOpen !== expectedOpen) {
          return false;
        }
        // ignore any other characters
      }
    }

    // ensure no unmatched opens remain
    return stack.length === 0;
  }
}
