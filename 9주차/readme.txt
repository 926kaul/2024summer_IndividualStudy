1주차
Chat GPT와 GPT plugin, custom GPT의 알려진 Vulnerability Search and Study, 상황 재현, request와 response 추적

2주차
Custom GPT에서 발생 가능한 privacy problem에 대한 paper study and summary, 실제 실험해봄
Su, Dongxun, et al. "Gpt store mining and analysis." arXiv preprint arXiv:2405.10210 (2024). https://arxiv.org/abs/2405.10210 

3주차
Custom GPT에서 발생할 수 있는 Security Threat을 paper를 참고하여 다시 분류
Guanhong Tao, Siyuan Cheng, Zhuo Zhang, Junmin Zhu, Guangyu Shen, and Xiangyu Zhang. 2023. Opening A Pandora’s Box: Things You Should Know in the Era of Custom GPTs. arXiv preprint arXiv:2401.00905 (2023) https://arxiv.org/abs/2401.00905 
Account를 통한 Authentication을 요구하는 GPT을 따라하는 Phishing GPT에 대한 문제를 확인하기 위해 직접 Phishing GPT와 Phshing Website를 제작
GPT store에서 사용률로 상위권을 차지하는 AI Humanizer라는 GPT를 모방해 Phishing GPT와 website를 제작; 제 3자의 입장에서 자체 테스트 해보았을때 원본과 구분하기 어려웠음
Phishing webiste를 통해 server에서 victim의 ID와 password를 얻을 수 있었음

4주차
custom GPT에서 XSS를 일으키기 위한 html, js execution이 실패함 (chat GPT는 python interpreter만 지원)
Knowledge file의 download link를 제공하기 위해서는 custom GPT가 python을 지원해야 한다는 사실을 실험을 통해 알아냄
실제 GPT store에 malicious custom GPT가 있는지 조사하기 위해 custom GPT들의 instruction과 knowledge file을 추출하는 방법을 고민함
GPT store에 서로 유사한 GPT들이 많다는 사실에 따라 이들을 선별하고 malicious한 GPT인지 조사하기 위한 방법 고민함

5주차
Top10 ranked GPT와 그와 유사한 GPT들에 대한 Manual inspection을 진행함
custom GPT로부터 추출한 Instruction들에서 malicious한 keyword가 포함되는지에 따라 분류하고 manual 조사함
많은 GPT가 instruction 제공을 거절했는데, 이 문제를 Base64로 encoded된 prompts를 활용하면서 해결 (Jailbreaking)
Crawling을 통해 GPT store에 있는 custom GPT의 instruction을 automatic extraction

6주차
Top500 GPT와 그와 이름이 유사한 GPT 최대 5개에 대한 instruction 등의 data 수집
instruction에 있는 URL들도 추출, 분류
GPT와 URL을 통한 promotion을 하는 GPT가 있는지 의심

7주차
Top500 GPTs와 realtive GPTs의 url에 변화가 있는지 감시 (promotion checking), 변화 없었음
URL들 중 malicious website가 있는지 manual 검사, 의심스러운 url이나 기능에 따라 분류
1159개의 GPT들의 instruction 사이에 유사도; top500 GPT와 relative GPT 사이에 유사도의 분포를 조사 (TF-IDF vector의 cosine simularity)
유사도 분포를 통해 유사도 0.6을 기준으로 잡고, 이보다 큰 유사도를 가진 GPT들을 수동 조사하여 Copycat GPT들을 찾음

8주차
GPT들의 instruction에 포함된 url들을 매일 추출하여 monitoring하였지만 sample 내에서는 변화가 없었음
PI DINGHAI, xxyyai.com, Sora 등 다수의 copycat GPT developer로 관찰된 developer를 조사하고 의도를 파악해봄
selfmade GPT에 대한 홍보; 특정 website traffic 증가; 다른 GPT의 custom 혹은 pirate version; user conversation 수집 등을 목적으로 하는 것으로 의심됨
google calendar와 연동된 GPT를 만들고, 여기서 외부 API로 access token을 유출해 외부에서 user의 google calendar에 접근하는 것을 시도함
GPT에게 google calendar와 똑같은 request를 명령; 외부 API로 payload가 access token인 request를 보내라 명령; Python code를 통한 GPT storage의 access token 접근을 시도 했으나 모두 실패함

9주차
copycat GPT developer인 Sora와 그 GPT들에 연동되있는 chat-prompt.com이 의심되어 조사함
약 6개의 copycat GPT들이 대상이 되었으며 각 GPT들의 instructino 조사와 chat-prompt.com로 request하는 trigger를 알아봄
GPT들의 API schema를 통해 chat-prompt.com API가 user conversation을 수집하기 위함임을 알아냄
추가적으로 chat-prompt.com의 response는 특정 GPT나 website에 대한 홍보 목적으로 보임
google calendar와 연동된 GPT에서 OAuth과 API schema의 구조를 수정하였지만 access token leakage에는 개선이 안됨
