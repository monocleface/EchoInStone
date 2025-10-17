# EchoInStone

오디오 파일에서 발화자 세그먼트를 전사, 기록 및 정렬하도록 설계된 포괄적인 오디오 처리 도구로 정확하고 충실한 Transcription을 달성하는데 중점을 두고 있습니다.
Youtube 동영상과 팟캐스트를 포함한 다양한 오디오 소스를 지원하고, 속도보다 정밀도와 안정성을 우선시하는 유연한 오디오 데이터 처리 파이프라인을 제공합니다.

## 특징

- **Transcription**: 자동 음성 인식(ASR) 모델을 사용하여 오디오 파일을 텍스트로 변환합니다, `Whisper Large v3 Turbo`.
- **Diarization**: 모델을 사용하여 오디오 파일에서 서로 다른 화자를 식별하고 분리합니다, `Pyannote Speaker Diarization 3.1`.
- **Alignment**: Whisper와 Pyannote의 출력에 맞춰 효율적이고 정확하도록 맞춤화된 알고리즘을 사용하여 전사된 텍스트를 해당 오디오 세그먼트에 맞춥니다, `SpeakerAlignement`.
- **Flexible and Extensible Pipeline**: 새로운 모델이나 처리 단계를 조직된 파이프라인에 쉽게 통합합니다, `AudioProcessingOrchestrator`.

## 설치

### 필수 조건

- Python 3.11 or higher
- Poetry (dependency management tool)
- ffmpeg (required for audio processing)

> Note: `ffmpeg` 은 시스템 PATH에 설치되어 있어야 합니다.
> 직접 설치하거나 패키지 관리자를 이용해 설치하세요:
> - On macOS: `brew install ffmpeg`
> - On Ubuntu/Debian: `sudo apt install ffmpeg`
> - On Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### 단계

1. **저장소 복제**:
   ```bash
   git clone https://github.com/monocleface/EchoInStone.git
   cd EchoInStone
   ```

2. **Poetry를 이용하여 종속성 성치**:
   ```bash
   poetry install
   ```

3. **로깅 설정** (optional):
   - 로깅 구성은 콘솔과 파일(`app.log`) 모두에 출력하도록 설정되어 있습니다. 로깅 설정은 `logging_config.py`에서 수정할 수 있습니다.

4. **Hugging Face Token 구성**:

  - Hugging Face 토큰을 추가해야 합니다. 아래의 단계를 따라해주세요:
     1. [Hugging Face Settings](https://huggingface.co/settings/tokens) 으로 이동.
     2. "New token" 을 클릭.
     3. 생성된 토큰을 복사하여 `EchoInStone/config.py` 파일에 아래와 같이 붙여넣습니다:

```python
# EchoInStone/config.py

# Hugging Face authentication token
HUGGING_FACE_TOKEN = "your_token_here"
```
401 Client Error: Unauthorized for url: https://huggingface.co/openai/whisper-large-v3-turbo/resolve/main/processor_config.json 에러가 발생하면 아래를 수행하시면 됩니다.

콘솔에서,

```
$huggingface-cli login
```
키 입력 커서가 나오면, 위 토큰을 입력하고 y를 누르시면 동작됩니다.

## Usage

### Basic Example

Youtube 동영상을 필사하고 Dizarization을 하려면 다음 명령을 실행하세요:

```bash
poetry run python main.py <audio_input_url>
```

- `<audio_input_url>`: 오디오 입력(YouTube, podcast, or direct audio file)의 URL 입니다.

### Command-Line Arguments

- **`--output_dir`**: 출력 파일을 저장할 디렉토리입니다. 기본값은 `"results"` 입니다.
  ```bash
  poetry run python main.py <audio_input_url> --output_dir <output_directory>
  ```

- **`--transcription_output`**: 전사 출력 파일 이름입니다. 기본값은 `"speaker_transcriptions.json"` 입니다.
  ```bash
  poetry run python main.py <audio_input_url> --transcription_output <output_filename>
  ```

### 예시

- **유투브 동영상을 Transcribe하고 기록하세요**:
  ```bash
  poetry run python main.py "https://www.youtube.com/watch?v=plZRCMx_Jd8"
  ```

- **팟캐스트를 Transcribe하고 기록하세요**:
  ```bash
  poetry run python main.py "https://radiofrance-podcast.net/podcast09/rss_13957.xml"
  ```

- **직접 MP3 파일을 Transcribe하고 기록하세요**:
  ```bash
  poetry run python main.py "https://media.radiofrance-podcast.net/podcast09/25425-13.02.2025-ITEMA_24028677-2025C53905E0006-NET_MFC_D378B90D-D570-44E9-AB5A-F0CC63B05A14-21.mp3"
  ```

## 테스팅

신뢰성을 보장하고 회귀를 방지하기 위해 단위 테스트와 BDD 테스트를 모두 포함하는 테스트를 합니다.

### 모든 테스트 수행

모든 테스트(unit tests and BDD tests)를 실행하려면 다음을 수행합니다:
```bash
poetry run pytest tests/ features/ -v
```

### 유형별 테스트 수행

**단위 테스트** (기능 구현 테스트):
```bash
poetry run pytest tests/ -v
```

**BDD 테스트** (행동 시나리오):
```bash
poetry run pytest features/ -v
```

### 테스트 커버리지

커버리지 보고서 생성:
```bash
poetry run pytest tests/ features/ --cov=Whisper_Pyannote_Sample --cov-report html
```

디렉토리(`htmlcov/`)에 테스트 커버리지 보고서가 생성됩니다.

### 테스트 구조

- **`tests/`**: 개별 구성 요소와 기능을 검증하는 단위 테스트
  - `test_audio_downloader.py`: URL/파일 다운로드 기능 테스트
  - `test_downloader_factory.py`: 다운로더 선택에 대한 테스트
  - `test_integration.py`: 전체 워크플로우에 대한 통합 테스트

- **`features/`**: 사용자 중심 동작을 설명하는 BDD 테스트
  - `downloader.feature`: 다운로더 선택 시나리오
  - `audio_download.feature`: 오디오 다운로드 기능 시나리오
  - `successful_download.feature`: 다운로드 성공 시나리오
  - `invalid_url.feature`: 오류 처리 시나리오
  - `transcription_output.feature`: Transcription 출력 검증

### 테스트 예제

테스트 모음은 아래를 포함한 다양한 시나리오를 다룹니다:
- YouTube video downloads
- Podcast RSS feed processing
- Direct MP3/audio file URLs (including RFI radio content)
- Local file processing
- Network error handling
- Header authentication for restricted URLs

모든 테스트는 회귀를 방지하고 다양한 입력 유형에서 오디오 다운로드 기능이 올바르게 작동하는지 확인하도록 설계되었습니다.

## Configuration

### Logging

로깅은 콘솔과 파일 (`app.log`) 모두에 메시지를 출력하도록 구성되어 있습니다. 파일(`logging_config.py`)에서 로깅 수준과 형식을 조정할 수 있습니다.

### Models

- **Transcription Model**: 기본 전사 모델(`openai/whisper-large-v3-turbo`) 입니다. 초기화 시 매개변수(`model_name`) 파라메터(`WhisperAudioTranscriber`)를 수정하여 변경할 수 있습니다.
- **Diarization Model**: 기본 분할 모델(`pyannote/speaker-diarization-3.1`)입니다. 클래스의 모델 로딩 코드(`PyannoteDiarizer`)를 수정하여 변경할 수 있습니다.

## Contributing

참여를 환영합니다. 다음 단계를 따라주세요:

1. 저장소(https://github.com/jeanjerome/EchoInStone)를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature-branch`).
3. 변경 사항을 적용하고 커밋합니다 (`git commit -am 'Add new feature'`).
4. 푸시합니다 (`git push origin feature-branch`).
5. 새로운 풀 리퀘스트를 만듭니다.

## License

이 프로젝트는 MIT 라이선스가 부여됩니다. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- 이 프로젝트에서 사용된 다양한 라이브러리와 모델을 제공해 준 오픈 소스 커뮤니티에 감사드립니다.
- 이 프로젝트를 가능하게 하는 모델과 도구의 기여자와 유지 관리자에게 특별히 감사 드립니다.

## Contact

질문이나 제안 사항이 있으시면 이슈를 작성해주세요.
