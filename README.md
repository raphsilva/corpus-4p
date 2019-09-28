# Córpus de opiniões em português sobre produtos eletrônicos para sumarização contrastiva

Este repositório contém um córpus que foi construído para testar métodos de sumarização contrastiva de opinião, que é uma tarefa que visa comparar duas entidades por meio de resumos de textos opinativos sobre elas. Houve anotação manual de informações sobre as opiniões contidas em cada sentença, sendo cada opinião indicada por seu aspecto e polaridade: o aspecto é a característica do produto que a opinião avalia e a polaridade indica se a opinião é positiva ou negativa. As 642 sentenças do córpus foram coletadas de 542 comentários opinativos publicados por compradores no site Buscapé e se referem a quatro produtos diferentes: dois aparelhos de telefone móvel e dois modelos de câmera. O córpus foi estendido por meio da criação de entidades fictícias que contêm sentenças das entidades reais selecionadas com diferentes estratégias, para, com isso, simular outras possibilidades de conjuntos de textos opinativos. Formaram-se dois pares de entidades reais e seis pares fictícios. 

## Conteúdo

Este repositório contém dois diretórios que são versões diferentes do mesmo córpus: o diretório `clean` contém uma versão limpa e estendida para uso geral, e o diretório `whole` contém toda a informação extraída do site, incluindo informações inúteis para a tarefa de sumarização contrastiva (devidamente marcadas como tal). 

### Dataset 

A versão para leitura automática do conjunto de dados contém 16 arquivos em formato JSON. Cada arquivo contém opiniões sobre uma entidade. As entidades D1a, D1b, D2a e D2b são reais e as demais são fictícias, formadas a partir de subconjuntos das sentenças das entidades reais. O formato dos arquivos é como no exemplo abaixo. As opiniões da sentença são representadas por uma palavra identificando o aspecto e um número identificando a polaridade: 100 para positivo, -100 para negativo e 0 para neutro. Opiniões irrelevantes não estão presentes nesses conjuntos.

```
{
    "data": [
        {
            "id": 3,
            "opinions": [
                [
                    "PRODUTO",
                    100
                ],
                [
                    "CÂMERA",
                    100/home/raphusp/Dropbox/Mestrado/Implementations/contrastive-summarization/Kim
                ]
            ],
            "sentence": "Ótimo celular. Câmera excelente."
        },
        {
            "id": 18,
            "opinions": [
                [
                    "PRODUTO",
                    -100
                ],
                [
                    "DESIGN",
                    -100
                ],
                [
                    "OUTRO",
                    -100
                ]
            ],
            "sentence": "Produto deixa a desejar, bordas metalicas riscam com facilidade, botão home então nem se fala."
        },
    ],
    "meta": {
        "Crawl date": "17/may/2018 ",
        "ID": "11",
        "Product": "Smartphone Samsung Galaxy S7 SM-G930 32GB",
        "Source": "www.buscape.com.br/smartphone-samsung-galaxy-j5-prime-sm-g570m",
        "Total of opinions": "755",
        "Total of reviews": "221",
        "Total of sentences": "641",
        "Type": "Celular"
    }
}
```


### Annotation

O diretório de anotação contém todos os dados extraídos da fonte e as informações inseridas pelos anotadores. Ela contém arquivos para os quatro produtos cujos comentários foram coletados.

Além dos conjuntos de dados, o diretório contém o script que foi usado para transformar os dados anotados em seu formato final.
