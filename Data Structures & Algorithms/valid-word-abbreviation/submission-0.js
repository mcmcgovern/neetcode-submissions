class Solution {
    /**
     * @param {string} word
     * @param {string} abbr
     * @return {boolean}
     */
    validWordAbbreviation(word, abbr) {
        if (word === abbr) return true;

        let a = 0, w = 0;
        while (a < abbr.length && w < word.length) {
            if (word.charAt(w) === abbr.charAt(a)) {
                a++;
                w++;
                continue;
            }
            if (!isDigit(abbr.charAt(a)) && abbr.charAt(a) !== word.charAt(w)) {
                return false;
            }
            if (abbr.charAt(a) === '0') return false;

            let skip = 0;
            while (a < abbr.length && isDigit(abbr.charAt(a))) {
                // JS concatenation will treat as strings
                skip = Number(skip + abbr.charAt(a));
                a++;
            }
            w += skip;
        }

        return a === abbr.length && w === word.length;
    }
}

function isDigit(char) {
    return char >= '0' && char <= '9';
}