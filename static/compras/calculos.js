const pagina = window.location.href.split("/");
const zip = (a, b) => a.map((k, i) => [k, b[i]]);
$(document).ready(function() {
    
    if (pagina.includes("change") || pagina.includes("add")){
        //reordenar divs
        $(".field-valor_imposto").insertAfter(".inline-related");
        $(".field-valor_total").insertAfter(".field-valor_imposto");

        //calcular valor
        $(".field-valor > input").keydown(calcular);
        $(".field-quantidade > input").keydown(calcular);
        $(".inline-deletelink").click(calcular);
        let porcentagem_impostos = $("#id_porcentagem_impostos");
        let valor_impostos = $(".field-valor_imposto").find("p");
        let valor_total = $(".field-valor_total").find("p");
        function calcular(){
            setTimeout(function(){
                var lista_valores = [];
                var lista_quantidades = [];
                $(".field-valor > input").each(function(index) {
                    lista_valores.push(parseFloat($(this).val()))
                });
                $(".field-quantidade > input").each(function(index) { 
                    lista_quantidades.push(parseFloat($(this).val()));
                });
                let produtos = zip(lista_valores, lista_quantidades);
                console.log("produtos", produtos);
                let valor = 0;
                for (let p of produtos) { 
                    console.log(p);
                    valor = valor + (p[0] * p[1] || 0);
                }
                console.log(valor);
                let valor_imposto = (valor * porcentagem_impostos.val()/100).toFixed(2);
                valor_impostos.html("R$ " + valor_imposto);
                let valor_total_calculado = (parseFloat(valor) + parseFloat(valor_imposto)).toFixed(2);
                valor_total.html("R$ " + valor_total_calculado);
            }, 200);
        }

        porcentagem_impostos.keydown(calcular);
        calcular();
    }
});