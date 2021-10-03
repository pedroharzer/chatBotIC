import { ChangeDetectorRef, Component, Injector, OnInit, ViewChild } from '@angular/core';

import { ChatComponent } from '../chat/chat.component';
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

  teste = '';

  @ViewChild(ChatComponent) private chatComponent: any;

  constructor(injector: Injector,
              private cdr: ChangeDetectorRef) {
    this._chatbotService = injector.get(ChatbotService);  
  }

  ngOnInit(): void {
  }

  onEnviar(): void {
    let me = this;

    let input = this.inputText;
    if (this.inputText && this.inputText.trim() != ""){
      let newMessage = new Message(this.inputText, Message.typeQuestion);
      this.inputText = '';
      this.chatComponent.addMessage(newMessage);
      this.cdr.detectChanges();

      me._chatbotService.postEntrada(input).subscribe(response => { 
        let newMessage = new Message((response as any).resposta, Message.typeAnswer);
        this.chatComponent.addMessage(newMessage);
        this.cdr.detectChanges();
        
        console.log((response as any).resposta);
      } );
    }
  }

}
