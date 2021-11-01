export class Message {

    static typeQuestion = 'question';
    static typeAnswer = 'answer';
    static typeSuggestion = 'suggestion';

    message: string;
    style: string;
    suggestions: Array<string>;

    constructor(message: string,
                style: string,
                suggestions: Array<string> = []){
        this.message = message;
        this.style = style;
        this.suggestions = suggestions;
    }

    public setSuggestions(input: any) {
        this.suggestions = input;
    }

    public getSuggestions(): any {
        return this.suggestions;
    }
}