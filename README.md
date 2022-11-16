# DOTORY

GPT2 기반의 동화 생성을 구현한 창업팀 프로젝트입니다.

동화를 한 문장씩 이어서 생성하여 지정한 테마 배경의 스토리를 창작하는 머신 구현을 목표로 하였습니다.

입력 문장 뒤에 연결되는 3가지 문장을 생성한 후 그 중 하나를 택하고, 또 3가지 문장을 생성한 후 선택하는 반복 방식의 task입니다.

![서비스 화면 예시2](https://user-images.githubusercontent.com/55081331/202189372-c888fd9d-d94e-48af-b521-c9618ef6a892.png)


## Tried Tech

업로드한 노트북 파일과 같이, 3가지 방식을 시도하였습니다.
- GPT2 생성 + 번역
- GPT2 생성 + 번역 + Similarity
- **KoGPT2 생성** --> SOTA!

#### GPT2 생성

OpenAI에서 오픈한 GPT2는 다국어로 학습된 모델이긴 하나 영어에서 가장 높은 완성도를 보이므로, 영어 동화 데이터로 전이학습을 시킨 후 생성하도록 하였습니다.

#### 번역

영어로 생성된 문장을 카카오 번역 API를 사용하여 번역해주는 과정을 사용했습니다.

#### Similarity

생성에만 의존하기 어려운 완성도를 보여, 유사도 기반으로 보유하고 있는 동화 데이터 사전에서 문장을 선택하여 출력하는 과정을 사용했습니다.

#### KoGPT2 생성

SKT에서 오픈한 KoGPT2를 한글 동화 데이터로 학습시킬 경우, 영어로 생성한 후 번역을 거치는 것보다 문체도 자연스럽고, 문맥 측면에서도 떨어지지 않는 성능을 보였습니다.


## Best Result

한국어 NLG에서는 KoGPT2가 가장 우수한 성능을 보였습니다. 하지만 모델 학습만으로는 부족한 완성도를 다양한 단계를 거쳐 높이도록 하였습니다.

먼저 서비스 기획 의도에 따라 테마와 등장인물 이름을 선택한 후 이를 반영한 문장이 생성될 수 있도록, **테마 라벨링과 등장인물 마스킹** 작업을 시행하였습니다.

테마명과 등장인물 마스킹은 **special token**으로 추가하였고, 생성된 문장 안에 있는 등장인물 마스킹 토큰은 지정한 이름으로 바꿔주는 작업을 거치도록 하였습니다. (이 때 알맞은 조사 매칭이 필요합니다 : [replace_name 함수](https://github.com/Seyoung-Jung/DOTORY/blob/main/kogpt2.ipynb))

또한 동화에서 등장하면 곤란한 단어들을 모아 사전을 만들어 출력 전에 **필터링**을 거치도록 하였습니다.

#### Ex 1) 테마 : 숲속, 등장인물 : 토끼, 호랑이

![최종 생성 예시_숲속](https://user-images.githubusercontent.com/55081331/202189748-ea1c70cb-edda-4da9-b6a5-3696e293eba4.png)

#### Ex 2) 테마 : 왕국, 등장인물 : 공주, 왕자

![최종 생성 예시_왕국](https://user-images.githubusercontent.com/55081331/202189812-b2a094a0-4701-46e0-9526-d84fcd0c285f.png)

#### Ex 3) 테마 : 마을, 등장인물 : 도현, 민시

![최종 생성 예시_마을](https://user-images.githubusercontent.com/55081331/202192361-1450b996-9649-412a-b1f1-bc45bbd03c28.jpg)


## Total Code

서버 연결을 포함한 서비스 전체 코드는 아래 레포지에 있습니다.

창업팀 레포지 : https://github.com/dotory-space

Inference on server code : https://github.com/dotory-space/dotory_fairy_tale_generator


## Reference

- https://github.com/SKT-AI/KoGPT2
- https://huggingface.co/HScomcom/gpt2-fairytales?text=Once+upon+a+time%2C
- https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e

