# SmartBabySitter(SBS) 

//2019-08-13 
//This file is guide to install YOLO.
//Plus, There are error which I faced with and also solution.
//
//By Dahyun Kim, Doooomdooom



##★ 참고 사이트(Reference site) ★

    https://reyrei.tistory.com/19 (필자는 본 블로그를 토대로 진행하였음. I mainly refered this site.) 
    https://reyrei.tistory.com/16

##★ 설치 환경(Environment) ★

    Visual Studio 2017 (작성일 기준으로 2019버전은 안되는걸로 알고있음. maximum ver = 2017)
    

##★ 설치 방법(Way to install) ★
###1) CUDA 설치하기 (https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)

    10.0 (10.1 안됨), 9.0, 8.0 등 본인의 컴퓨터 환경에 맞는 버전 설치
    ' the graphics driver could not find compatible graphics hardware cuda ' 다음과 같은 경고문 발생 시, 그래픽 카드 버전 확인 및 해당 버전 설치 필요
    
    - You have to install CUDA(10.1 (X), 10.0 or 9.0 or 8.0..etc) that is suitable your PC environment.  
    ' the graphics driver could not find compatible graphics hardware cuda ' When you met this caustion, you have to check your graphic card and install corresponding version. 

###2) 쿠다 툴킷 문서 활성화 (예제)하기 (file:///C:/Program%20Files/NVIDIA%20GPU%20Computing%20Toolkit/CUDA/v10.0/doc/html/cuda-quick-start-guide/index.html#windows-local)

    .sln 파일 활성화 시키기  (안해도 됩니다!!)
    
    - Activate .sln file. ( You don't have to do this course! )

###3) cuDNN 설치 (https://developer.nvidia.com/rdp/cudnn-download)

    설치한 CUDA의 버전에 맞는 cuDNN 설치해야함. 공식 문서대로 따라해야함. 
    필자는 cuDNN의 압축을 해제하고 모든 폴더를 아래 경로에 삽입하였음.
    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
    
    - You have to install cuDNN which correspond to CUDA version. 
    I unpacked cuDNN and inserted all the folders in the path below.
    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
   
- 수정중 -
