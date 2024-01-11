## pose

### 1. 데이터셋 파일 경로

  코드 경로: ./ <br>
  데이터 및 학습된 모델 경로: ./data <br>
  NIA 데이터셋 정리 (원본 + 세그멘테이션/큐브 라벨 포맷): ./new_dataset <br>
  배경 영상 (학습 시 다양한 배경 증강을 위해 활용): ./BG <br>

****


### 2. .Json 파일 -> .txt 파일 변환 및 test.txt, train.txt 생성 (각티슈[tissue] 예시)

  * data = "tissue"
  
      python making_txtlabels.py
      
****

### 3. 데이터셋 학습 (각티슈[tissue] 예시)

* 학습할 카테고리별로 실행
 
      python train.py \
      --datacfg data/tissue.data \
      --modelcfg cfg/yolo-pose.cfg \
      --initweightfile cfg/darknet19_448.conv.23 \
      --pretrain_num_epochs 15

****

### 4. 학습된 모델 테스트 (각티슈[tissue] 예시)

* 공개된 학습 모델 테스트
      
      python valid.py \
      --datacfg data/tissue.data \
      --modelcfg cfg/yolo-pose.cfg \
      --weightfile data/tissue/model.weights
      
****


### 5. 참고

* Original src.: https://github.com/google-research/jax3d/tree/main/jax3d/projects/mobilenerf
      
      https://www.dropbox.com/s/lvmr4ssdyo2ham3/singleshotpose-master.zip?dl=0
      
<br>
