## MobileNeRF with Hash Encoding

### 1. 데이터셋 파일 경로

  코드 경로: ./ <br>
  데이터 경로: ./datasets <br>
  학습된 모델의 경로: ./weights <br>
  샘플 경로: ./samples <br>

****


### 2. 설치

      conda create --name mobilenerf python=3.10 -y; conda activate mobilenerf
      conda install pip; pip install --upgrade pip
      pip install -r requirements.txt
      pip install tqdm
      pip install -U "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
      pip install flax==0.5.1
      pip install -U "jax[cuda12_pip]"==0.4.13 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
      
****

### 3. 학습 (Shell script)
 
      sh test.sh {데이터명}

****


### 4. 참고

* Original src.: https://github.com/google-research/jax3d/tree/main/jax3d/projects/mobilenerf
* Hash Encoding: https://github.com/NVlabs/instant-ngp.git
      
      
<br>
