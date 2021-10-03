export class Message {

    static typeQuestion = 'question';
    static typeAnswer = 'answer';

    message: string;
    style: string;

    constructor(message: string,
                style: string){
        this.message = message;
        this.style = style;
    }
}