class Singleton {

    static instance;
    message;
    /**
     * In JavaScript consider this method as the 'getInstance'
     */
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        Singleton.instance = this;
    }

    /**
     * @return {string}
     */
    getValue() {
        return Singleton.instance.message;
    }

    /**
     * @param {string} value
     * @return {void}
     */
    setValue(value) {
        Singleton.instance.message = value;
    }
}
