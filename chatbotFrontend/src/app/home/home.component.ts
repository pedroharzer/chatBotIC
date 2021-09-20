import { Component, Injector, OnInit } from '@angular/core';

import { ChatComponent } from '../chat/chat.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  inputText: any;

  _chatComponent: ChatComponent;

  constructor(injector: Injector) {
    this.inputText = "";
    this._chatComponent = injector.get(ChatComponent);
  }

  ngOnInit(): void {
  }

  onEnviar(): void {
    this._chatComponent.addMessage("testando");
  }

}
