# Detecção de Câncer de Mama

### Descrição do Projeto:

O diagnóstico precoce é crucial para o sucesso do tratamento do câncer de mama. Com o nosso projeto inovador, estamos capacitando médicos e profissionais de saúde com uma ferramenta poderosa que utiliza dados numéricos precisos de tumores/nódulos para identificar potenciais casos de câncer em estágios iniciais. Isso não apenas aumenta as taxas de sucesso do tratamento, mas também reduz a necessidade de intervenções mais agressivas, proporcionando uma melhor qualidade de vida às pacientes.

No âmbito mais amplo, nossa pesquisa contribui para uma sociedade mais saudável e resiliente. O impacto de uma detecção mais precisa e precoce do câncer de mama se estende para além dos indivíduos, influenciando políticas de saúde pública e sistemas de cuidados médicos. Ao fornecer uma ferramenta acessível e eficaz, estamos pavimentando o caminho para uma abordagem mais proativa à saúde, onde o foco está na prevenção e no bem-estar geral.

### USO:
Lemnbre-se que para utilizar o projeto a API do mesmo deve esta alocada em algum serviçio de nuvem como por exemplo AWS ou AZURE,
Minha indicação é que voce utilize a biblioteca Request do Python com o seguintes codigos:
![image](https://github.com/omarcos0708/Deteccao-de-Cancer-de-Mama/assets/101226989/111c0ac5-43c0-4f53-8819-5d2e25823ded)

Alem disso é bom ter em mente as features que foram escolhidas para o modelo que no caso deste lhe dou o seguinte exemplo de uso:
```json
  {
"radius_mean": 17.99,
"texture_mean": 10.38,
"perimeter_mean": 122.8,
"area_mean": 1001,
"smoothness_mean": 0.1184,
"compactness_mean": 0.2776,
"concavity_mean": 0.3001,
"concavepoints_mean": 0.1471,
"symmetry_mean": 0.2419,
"fractal_dimension_mean": 0.07871,
  }
```
### Requerimentos:

As seguintes bibliotecas foram utilizadas no processo de contrução do modelo:

![image](https://github.com/omarcos0708/Deteccao-de-Cancer-de-Mama/assets/101226989/8dbb35a4-e557-49cc-bb19-880c40a42f75)

### Resultados:
#### Matriz de confusão:
![image](https://github.com/omarcos0708/Deteccao-de-Cancer-de-Mama/assets/101226989/6ae843b8-4db3-49ff-831c-4988b43d1acf)
#### Loss e Acurácia
![image](https://github.com/omarcos0708/Deteccao-de-Cancer-de-Mama/assets/101226989/c5fdda35-da0d-47d6-8c6e-a95defc83323)
A Matriz de confusão demonstra muito bem a peformace do modelo com dados que nunca haviam sido vistos pelo menos, estatisticamente o modelo performa de maneira precisa e é sim possivel utilizar suas saidas/respostas para diagnóstico de cancer de mama baseado nas metricas e medidas dos tumores ou nódulos.

Outras Métricas como o Loss e Acuracia descrevem a precisao e erros do modelo, ja que o mesmo se trata de um modelo de classificação a Acuracia é a principal metrica de avaliação alem da matiz de confusão
