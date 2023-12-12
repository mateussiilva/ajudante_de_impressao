#!/usr/bin/env nodejs


const configuracoesImpressoras = {
    "1604": 9,
    "1602": 17,
    "1904": 58,
};
const MINUTOS = 60;

function calcularTempoImpressao(metros_por_minuto, metros) {
    return Math.ceil(metros / metros_por_minuto * 60)
}


function TempoDeImpressão() {
    let metrosImpressao = parseFloat(document.querySelector("#imetros").value);
    let impressoraSelecionada = document.querySelector("#iimpressoras").value;
    for (impresora in configuracoesImpressoras) {
        if (impresora === impressoraSelecionada) {
            let metrosPorMinuto = configuracoesImpressoras[impresora]
            alert(`${calcularTempoImpressao(metrosPorMinuto, metrosImpressao)} minutos`)
        }
    }

}