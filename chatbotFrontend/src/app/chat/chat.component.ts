import { ChangeDetectorRef, Component, Injectable, Injector, OnInit } from '@angular/core';

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

  constructor(injector: Injector,
              private changeDetector: ChangeDetectorRef) {
    this._chatbotService = injector.get(ChatbotService);
    this.messageArray = [{message: "test message 1", style: "answer"}];
  }

  ngOnInit(): void {
    let me = this;

    me._chatbotService.postEntrada().subscribe(response => { 
      me.teste = (response as any).resposta;
      console.log(me.teste);
    } );
  }

  addMessage(message: string, style: string): void {
    this.messageArray = [...this.messageArray, {message: message, style: style}];
    this.changeDetector.detectChanges();
    console.log(this.messageArray);
  }

}
