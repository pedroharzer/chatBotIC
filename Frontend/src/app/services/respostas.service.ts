import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable()
export class RespostasService {
    constructor(private http: HttpClient) {
        
    }
}