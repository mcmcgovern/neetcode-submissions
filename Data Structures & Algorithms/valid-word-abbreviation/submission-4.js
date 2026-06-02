class Solution {
    /**
     * @param {string} word
     * @param {string} abbr
     * @return {boolean}
     */
    validWordAbbreviation(word, abbr) {
        // parse abbreviation
        let wpointer = 0;
        let apointer = 0;

        while (wpointer < word.length && apointer < abbr.length) {
            const currentWChar = word.charAt(wpointer);
            const currentAChar = abbr.charAt(apointer);
            if (currentWChar === currentAChar) {
                wpointer++;
                apointer++;
            } else if (currentAChar >= '0' && currentAChar <= '9') {
                const digitBeginIndex = apointer;
                if (currentAChar === '0') return false; //cannot have leading zeros
                while (abbr.charAt(apointer) >= '0' && abbr.charAt(apointer) <= '9') {
                    apointer++;
                }
                const digitsToSkip = Number.parseInt(abbr.slice(digitBeginIndex, apointer+1));
                console.log(digitsToSkip);
                if (wpointer + digitsToSkip <= word.length) {
                    wpointer += digitsToSkip;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }

        return wpointer === word.length && apointer === abbr.length;
    }
}
