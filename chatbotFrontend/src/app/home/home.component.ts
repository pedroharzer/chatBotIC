import { Component, Injector, OnInit } from '@angular/core';

import { ChatbotService } from '../service/chatbot.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  _chatbotService: ChatbotService;

  teste: any;

   constructor(injector: Injector) {
   this._chatbotService = injector.get(ChatbotService);
 }

 ngOnInit(): void {
   let me = this;
   me._chatbotService.postEntrada().subscribe(response => { 
     me.teste = (response as any).resposta;
     console.log(me.teste);
   } );
  }

}
