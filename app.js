const maquinas = {
    1904: "PrismaTex",
    1604: "PrismaJet",
    1602: "Mutoh",
}
    

function preencherSelectMaquinas(objectMaquinas,tagHTMLSelect){
    // let selectMaquinas = .getElementById("imaquinas")
    for (let maquina in objectMaquinas) {
        let selectMaquina = document.createElement("option");
        let valorMaquina = objectMaquinas[maquina.toString()]
        selectMaquina.value = maquina
        selectMaquina.text = valorMaquina
        tagHTMLSelect.append(selectMaquina)
    }
}


function calcularMetrosFaltantes(metros,porcentagemAtual){
    let pCem = (porcentagemAtual /100)
    let metrosImpressos = pCem * metros
    let metrosFaltantes = metros - metrosImpressos
    return metrosFaltantes
}

 



let selectMaquinas = document.getElementById("imaquinas")
preencherSelectMaquinas(maquinas,selectMaquinas)

document.addEventListener("submit", (e)=>{
    e.preventDefault()
    let maquinaSelecionada = selectMaquinas.options[selectMaquinas.selectedIndex].text
    let inpPorcentagemImpressao = parseInt(document.querySelector("#iporcenteagem").value);
    let quantidadeMetros = parseFloat(document.querySelector("#imetros").value);
    const metrosFaltantes = calcularMetrosFaltantes(metros=quantidadeMetros,porcentagemAtual=inpPorcentagemImpressao)
    
    if(maquinaSelecionada !== NaN && quantidadeMetros !== NaN){
        switch (maquinaSelecionada){
            case "PrismaTex":
                console.log(metrosFaltantes)
                break 
            case "PrismaJet":
                console.log(metrosFaltantes)
                break 
            case "Mutoh":
                console.log(metrosFaltantes)
                break  
            default:
                0


        }
    }
    console.log(maquinaSelecionada)
    
})
