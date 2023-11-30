#!/usr/bin/env nodejs


const MINUTOS = 60;
const METROS_MUTOH = 9;
const METROS_JET = 17;
const METROS_TEX = 58;
class CalcularImpressao{
    constructor(nomeMaquina,metrosPorHora=null){
        this.name = nomeMaquina
        this.metroPorHora = metrosPorHora
        get
    }

    tempoDeImpressao(metros){
        switch (this.name){
            case "mutoh":
                return Math.round((metros * MINUTOS) / METROS_MUTOH) 
            case "prismajet":
                return Math.round((metros * MINUTOS) / METROS_JET) 
            case "prismatex":
                return Math.round((metros * MINUTOS) / METROS_TEX) 

        }
    }
}


const calculadora = new CalcularImpressao("prismajet")
let tempo_de_impressao = calculadora.tempoDeImpressao(17)
console.log(tempo_de_impressao)