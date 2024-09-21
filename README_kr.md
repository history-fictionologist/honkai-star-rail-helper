# honkai-star-rail-helper

`honkai-star-rail-helper`는 비디오 게임 [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail)의 캐릭터 데이터, 스킬 및 유물 추천을 관리하고 처리하기 위해 설계된 유틸리티입니다. 입력 파일을 읽고 캐릭터 정보 및 스킬 세트와 같은 다양한 속성을 처리하며, 결과를 정리된 형식으로 출력합니다. 입력 데이터는 [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) 저장소의 공식 업데이트 패키지에서 가져오며, 출력은 버전별 폴더에 저장되어 쉽게 관리할 수 있습니다.

## 최신 캐릭터 테이블
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION        | THE_HUNT | ERUDITION | HARMONY | NIHILITY      | PRESERVATION | ABUNDANCE |
| ----------- | ------ | ------------------ | -------- | --------- | ------- | ------------- | ------------ | --------- |
| PHYSICAL    | 5      | clara|player|yunli | boothill | argenti   | robin   |               |              |           |
| PHYSICAL    | 4      |                    | sushang  |           | hanya   | luka          |              | natasha   |
| FIRE        | 5      | sam                | topaz    | himeko    |         | jiaoqiu       | player2      | lingsha   |
| FIRE        | 4      | hook               |          |           | asta    | guinaifen     |              | gallagher |
| ICE         | 5      | jingliu            | yanqing  |           | ruanmei |               | gepard       |           |
| ICE         | 4      | misha              |          | herta     |         | pela          | mar7th       |           |
| LIGHTENING  | 5      |                    |          | jingyuan  |         | acheron|kafka |              | bailu     |
| LIGHTENING  | 4      | arlan              | moze     | serval    | tingyun |               |              |           |
| WIND        | 5      | blade              | feixiao  |           | bronya  | blackswan     |              | huohuo    |
| WIND        | 4      |                    | danheng  |           |         | sampo         |              |           |
| QUANTUM     | 5      |                    | seele    | jade      | sparkle | silverwolf    | fuxuan       |           |
| QUANTUM     | 4      | xueyi              |          | qingque   |         |               |              | lynx      |
| IMAGINARY   | 5      | danhengil          | drratio  |           | player3 | welt          | aventurine   | luocha    |
| IMAGINARY   | 4      |                    | mar7th2  |           | yukong  |               |              |           |
<!-- CHARACTER_TABLE_END -->

## 주요 기능
- 캐릭터 데이터, CV, 스킬 세트 및 유물 추천을 자동으로 다운로드합니다.
- 데이터를 버전별 입력/출력 디렉토리로 처리하고 정리합니다.
- 각 새 업데이트에 대해 명령줄에서 버전 번호를 구성할 수 있습니다.

## 요구 사항

다음을 확인하십시오:
- **Python 3.8+** (`python3 --version`으로 확인).
- `requirements.txt`에 나열된 필수 Python 패키지.

## 설치

1. **리포지토리 클론:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(선택 사항) 가상 환경 생성 및 활성화:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows의 경우: venv\Scriptsctivate
   ```

3. **종속성 설치 (현재 추가 종속성 필요 없음):**
   ```bash
   # 현재는 종속성을 설치할 필요가 없으나, 추후 필요 시:
   # pip install -r requirements.txt
   ```

## 사용법

### 도구 실행
   `src/` 디렉토리로 이동한 후 원하는 버전 번호로 메인 스크립트를 실행합니다:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - `<version_number>`을 현재 버전으로 교체하십시오 (예: `2.5`).
   - 파일 다운로드를 건너뛰려면 `--skip-download` 플래그를 추가하십시오.

   입력 파일은 `input/{version}` 폴더에 다운로드되며, 출력은 `output/{version}` 폴더에 저장됩니다.

### 사용 예시

- 버전 `2.5`로 스크립트를 실행하고 파일을 다운로드하려면:
  ```bash
  python3 main.py --version 2.5
  ```

- 버전 `2.5`로 스크립트를 실행하고 파일 다운로드를 건너뛰려면:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- 버전 `2.5`로 스크립트를 실행하고 특정 언어(예: EN 및 JP)에 대한 파일을 다운로드하려면:
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## 기여하기

기여를 환영합니다! 다음과 같은 방법으로 기여할 수 있습니다:
- 새로운 기능이나 버그 수정을 위한 풀 리퀘스트 제출.
- 문제 트래커를 통해 문제 보고.
- 모든 기여는 테스트 및 관련 문서를 포함해야 합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.
