import { Component, Injectable, Injector, OnInit } from '@angular/core';

import { ChatbotService } from '../service/chatbot.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
@Injectable({
  providedIn: 'root'
})
export class ChatComponent implements OnInit {

  _chatbotService: ChatbotService;

  teste: any;
  messageArray: Array<any>;

  constructor(injector: Injector) {
    this._chatbotService = injector.get(ChatbotService);
    this.messageArray = [
      {message: "Bem vindo(a) ao Chatbot do Instituto de Computação UFBA! Em que posso ajudar?", style: "answer"}
    ];
  }

  ngOnInit(): void {
    let me = this;
    me._chatbotService.postEntrada().subscribe(response => { 
      me.teste = (response as any).resposta;
      console.log(me.teste);
    } );
  }

  addMessage(message: string): void {
    console.log("addMessage: " + message);
  }

}
