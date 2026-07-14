class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let open = '([{'
        let close =  ')]}'
        let stack = []
        for (let i = 0; i < s.length; i++) {
            if (open.includes(s[i])) {
                stack.push(s[i])
            }
            if (close.includes(s[i])) {
                let lastOpen = open[close.indexOf(s[i])]
                let topBracket = stack.pop()
                if (lastOpen != topBracket) return false
            }
        }
        return stack.length === 0
    }
}
