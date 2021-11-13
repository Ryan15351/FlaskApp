function AddCarrinho(produto, qtd, valor, posicao)
{

    localStorage.setItem("poduto" + posicao, produto);
    localStorage.setItem("qtd" + posicao, qtd);
    valor = valor * qtd;
    localStorage.setItem("valor" + posicao, valor);
    alert("O produto " + produto + " foi adicionado ao carrinho");


};


