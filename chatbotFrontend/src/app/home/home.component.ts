import { ChangeDetectorRef, Component, Injector, OnInit } from '@angular/core';

import { Message } from '../models/message.model'
import { ChatbotService } from '../service/chatbot.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  _chatbotService: ChatbotService;

  inputText: any;
  messageArray: Array<Message>;

  constructor(injector: Injector,
              private cdr: ChangeDetectorRef) {
    this._chatbotService = injector.get(ChatbotService);

    let initialMessage = new Message("Bem vindo(a) ao Chatbot do Instituto de Computação UFBA! Em que posso ajudar?", Message.typeAnswer);
    this.messageArray = [initialMessage];
  }

  ngOnInit(): void {
  }

  onEnviar(): void {
    let me = this;

    let input = me.inputText;
    if (me.inputText && me.inputText.trim() != ""){
      let newMessage = new Message(me.inputText, Message.typeQuestion);
      me.inputText = '';
      me.addMessage(newMessage);
      me.cdr.detectChanges();

      me._chatbotService.postEntrada(input).subscribe(response => { 
        let newMessage = new Message((response as any).resposta, Message.typeAnswer, (response as any).sugestoes);
        me.addMessage(newMessage);
        me.cdr.detectChanges();
      } );
    }
  }

  onSuggestion(question: string): void {
    console.log("askSuggestion " + question);
    let me = this;

    let newMessage = new Message(question, Message.typeQuestion);
    me.addMessage(newMessage);
    me.cdr.detectChanges();

    me._chatbotService.postEntrada(question).subscribe(response => {
      let newMessage = new Message((response as any).resposta, Message.typeAnswer, (response as any).sugestoes);
      me.addMessage(newMessage);
      me.cdr.detectChanges();
    });
  }

  addMessage(message: Message): void {
    this.messageArray = [...this.messageArray, message];
    this.cdr.detectChanges();
  }

}
