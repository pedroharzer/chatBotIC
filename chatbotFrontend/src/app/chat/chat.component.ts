import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Injectable, Injector, OnInit } from '@angular/core';

import { Message } from '../models/message.model'

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss'],
  changeDetection: ChangeDetectionStrategy.Default
})
export class ChatComponent implements OnInit {

  teste: any;
  messageArray: Array<Message>;

  constructor(
              private changeDetector: ChangeDetectorRef) {  
    let initialMessage = new Message("Bem vindo(a) ao Chatbot do Instituto de Computação UFBA! Em que posso ajudar?", Message.typeAnswer);
    this.messageArray = [initialMessage];
  }

  ngOnInit(): void {
  }

  addMessage(message: Message): void {
    //let newMessage = new Message(message, style);
    this.messageArray = [...this.messageArray, message];
    //this.messageArray.push({message: message, style: style});
    this.changeDetector.detectChanges();
    console.log(this.messageArray);
  }

}
